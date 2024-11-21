import csv
import json
from dataclasses import asdict, fields,is_dataclass
from typing import Any, TypeVar

from Def import (
    DataShow,
    Faculty,
    Group,
    Level,
    Module,
    PendingSession,
    Professor,
    Room,
    RoomType,
    Section,
    SessionType,
)

# Constants
CSV_PATHS = {
    "levels": "promos.csv",
    "curriculum": "curiculum.csv",
    "rooms": "rooms.csv",
}

DATASHOW_COUNT = 8
DEFAULT_SEMESTER = 2
ROOM_TYPE_MAPPING = {
    1: RoomType.AMPHI,
    2: RoomType.TU,
    3: RoomType.LAB,
}


def split_groups_into_sections(
    all_groups: list[Group], section_count: int,
) -> list[list[Group]]:
    """Splits groups into n sections trying to maintain even distribution"""
    if not all_groups or section_count <= 0:
        return []
    k, m = divmod(len(all_groups), section_count)
    return [
        all_groups[i * k + min(i, m) : (i + 1) * k + min(i + 1, m)]
        for i in range(section_count)
    ]


def parse_int_safely(value: str) -> int:
    """Converts string to integer, returns 0 for invalid inputs"""
    try:
        return int(value.strip())
    except (ValueError, AttributeError):
        return 0


def create_numbered_groups(group_count: int, student_count: int) -> list[Group]:
    """Creates sequentially numbered groups with specified student count"""
    if group_count <= 0 or student_count <= 0:
        return []
    return [Group(number=i + 1, effective=student_count) for i in range(group_count)]


def parse_curriculum_row(row: list[str]) -> Module | None:
    """Creates module from CSV row with format: [_, name, abbr, lectures, tutorials, labs, ...]"""
    if len(row) < 6:
        return None
    _, name, abbr, n_lectures, n_tutorials, n_labs, *_ = row
    name = name.strip()
    abbr = abbr.strip()
    if not name or not abbr:
        return None
    return Module(
        name=name,
        abbreviation=abbr,
        semester=DEFAULT_SEMESTER,
        number_of_lectures=parse_int_safely(n_lectures),
        number_of_tutorials=parse_int_safely(n_tutorials),
        number_of_labs=parse_int_safely(n_labs),
    )


def create_curriculum(curriculum_data: list[list[str]]) -> list[Module]:
    """Creates list of modules from curriculum CSV data, skipping invalid rows"""
    return [
        module
        for row in curriculum_data
        if (module := parse_curriculum_row(row)) is not None
    ]


def assign_curriculum_to_levels(
    levels: list[Level], level_table: list[list[str]], curriculum: list[Module],
) -> list[Level]:
    """Maps curriculum modules to levels using index ranges from level table"""
    if not levels or not level_table or not curriculum:
        return levels

    for i, row in enumerate(level_table):
        if len(row) < 2 or i >= len(levels):
            continue
        start_idx = parse_int_safely(row[-2]) - 1
        end_idx = parse_int_safely(row[-1]) - 1
        if start_idx >= 0 and end_idx >= start_idx:
            levels[i].curriculum = curriculum[start_idx:end_idx]
    return levels


def create_rooms(rooms_data: list[list[str]]) -> list[Room]:
    """Creates rooms from CSV data with format: [name, type_index, capacity]"""
    rooms: list[Room] = []
    for row in rooms_data:
        if len(row) < 3:
            continue
        name, type_index, capacity = row
        name = name.strip()
        if not name:
            continue

        type_idx = parse_int_safely(type_index)
        if type_idx not in ROOM_TYPE_MAPPING:
            continue

        room_capacity = parse_int_safely(capacity)
        if room_capacity <= 0:
            continue

        rooms.append(
            Room(
                name=name, room_type=ROOM_TYPE_MAPPING[type_idx], capacity=room_capacity,
            ),
        )
    return rooms


def extract_professor_names(curriculum_table: list[list[str]]) -> set[str]:
    """Extracts unique, non-empty professor names from curriculum assignments"""
    prof_set = set()
    for row in curriculum_table:
        if len(row) < 9:  # Check minimum required fields
            continue
        _, _, _, _, _, _, prof_lecture, prof_tu, prof_lab = row[:9]

        for prof_list in [prof_lecture.strip(), prof_tu.strip(), prof_lab.strip()]:
            if not prof_list:
                continue
            for prof in prof_list.split(","):
                name = prof.split("(")[0].strip()
                if name:
                    prof_set.add(name)
    return prof_set


def get_professors(curriculum_table: list[list[str]]) -> list[Professor]:
    """Creates professor objects from unique names in curriculum"""
    return [Professor(name=name) for name in extract_professor_names(curriculum_table)]


def find_professor(professors: list[Professor], prof_name: str) -> Professor | None:
    """Finds professor by case-insensitive name match"""
    if not prof_name:
        return None
    prof_name = prof_name.strip().lower()
    return next(
        (prof for prof in professors if prof.name.strip().lower() == prof_name), None,
    )


def parse_professor_assignments(
    professors: list[Professor], assignments: str,
) -> list[tuple[Professor, int]]:
    """Parses professor assignment string format: 'name1(count1),name2(count2),...'"""
    assignment_pairs: list[tuple[Professor, int]] = []
    assignments = assignments.strip()
    if not assignments:
        return assignment_pairs

    for assign in assignments.split(","):
        assign = assign.strip()
        if not assign or "(" not in assign or not assign.endswith(")"):
            continue

        name, count_str = assign.rsplit("(", 1)
        name = name.strip()
        count = parse_int_safely(count_str[:-1])

        professor = find_professor(professors, name)
        if professor and count > 0:
            assignment_pairs.append((professor, count))

    return assignment_pairs


def create_session(
    attendance: Section | Group,
    professor: Professor,
    module: Module,
    session_type: SessionType,
) -> PendingSession:
    """Creates a pending session with given parameters"""
    return PendingSession(
        attendance=attendance, prof=professor, module=module, session_type=session_type,
    )


def distribute_professors_to_attendances(
    professor_assignments: list[tuple[Professor, int]],
    attendances: list[Section] | list[Group],
) -> list[tuple[Professor, Section | Group]]:
    """Pairs professors with their assigned sections/groups based on count"""
    if not professor_assignments or not attendances:
        return []

    flattened_profs = [
        prof for prof, count in professor_assignments for _ in range(count)
    ]

    if len(flattened_profs) != len(attendances):
        return []

    return list(zip(flattened_profs, attendances, strict=False))


def create_lecture_sessions(
    level: Level,
    module: Module,
    professor_assignments: str,
    professors: list[Professor],
    lecture_count: int,
) -> list[PendingSession]:
    """Creates lecture sessions for a module"""
    sessions: list[PendingSession] = []
    assignments = parse_professor_assignments(professors, professor_assignments)
    prof_section_pairs = distribute_professors_to_attendances(
        assignments, level.list_section,
    )

    for _ in range(lecture_count):
        for professor, section in prof_section_pairs:
            sessions.append(
                create_session(section, professor, module, SessionType.LECTURE),
            )
    return sessions


def create_group_sessions(
    level: Level,
    module: Module,
    professor_assignments: str,
    professors: list[Professor],
    session_count: int,
    session_type: SessionType,
) -> list[PendingSession]:
    """Creates tutorial or lab sessions for a module"""
    sessions: list[PendingSession] = []
    assignments = parse_professor_assignments(professors, professor_assignments)

    groups = [group for section in level.list_section for group in section.list_group]

    prof_group_pairs = distribute_professors_to_attendances(assignments, groups)

    for _ in range(session_count):
        for professor, group in prof_group_pairs:
            sessions.append(create_session(group, professor, module, session_type))
    return sessions


def find_module_row(
    curriculum_table: list[list[str]], module_name: str, starting_from: int,
) -> tuple[int, list[str]]:
    """Finds a module's row in curriculum table starting from given index"""
    for i, row in enumerate(curriculum_table[starting_from:], start=starting_from):
        if row[1].strip().lower() == module_name.strip().lower():
            return i, row
    raise ValueError(f"Module {module_name} not found")


def create_sessions(
    levels: list[Level], professors: list[Professor], curriculum_table: list[list[str]],
) -> list[Level]:
    """Creates all required sessions for each level and module"""
    current_row = 0

    for level in levels:
        all_sessions: list[PendingSession] = []

        for module in level.curriculum:
            try:
                current_row, row = find_module_row(
                    curriculum_table, module.name, current_row,
                )
            except ValueError:
                continue

            if len(row) < 9:  # Check minimum required fields
                continue

            (
                _,
                _,
                _,
                n_lectures,
                n_tutorials,
                n_labs,
                prof_lecture,
                prof_tu,
                prof_lab,
                *_,
            ) = row

            lecture_count = parse_int_safely(n_lectures)
            tutorial_count = parse_int_safely(n_tutorials)
            lab_count = parse_int_safely(n_labs)

            # Create different types of sessions
            all_sessions.extend(
                create_lecture_sessions(
                    level, module, prof_lecture.strip(), professors, lecture_count,
                ),
            )

            all_sessions.extend(
                create_group_sessions(
                    level,
                    module,
                    prof_tu.strip(),
                    professors,
                    tutorial_count,
                    SessionType.TU,
                ),
            )

            all_sessions.extend(
                create_group_sessions(
                    level,
                    module,
                    prof_lab.strip(),
                    professors,
                    lab_count,
                    SessionType.LAB,
                ),
            )

        level.required_sessions = all_sessions

    return levels


def load_csv(file_path: str) -> list[list[str]]:
    """Loads and returns CSV data, skipping the header row"""
    with open(file_path, encoding="utf-8") as f:
        reader = csv.reader(f)
        table = list(reader)
    return table[1:]  # Skip header row


def create_levels(promos: list[list[str]]) -> list[Level]:
    """Creates Level objects from promotion data rows"""
    promotions: list[Level] = []

    for p_name, n_sections, n_groups, n_students, *_ in promos:
        groups = create_numbered_groups(int(n_groups), int(n_students))
        groups_per_sections = split_groups_into_sections(groups, int(n_sections))
        sections = [
            Section(number=i + 1, list_group=groups_per_sections[i])
            for i in range(int(n_sections))
        ]
        promotions.append(Level(name=p_name, list_section=sections))
    return promotions


def data_parser() -> Faculty:
    """Loads and processes all scheduling data"""
    # Get base path for CSV files
    base_path = __file__.replace("LoadData.py", "")

    # Load CSV data
    levels_table = load_csv(f"{base_path}{CSV_PATHS['levels']}")
    curriculum_table = load_csv(f"{base_path}{CSV_PATHS['curriculum']}")
    rooms_table = load_csv(f"{base_path}{CSV_PATHS['rooms']}")

    # Process data
    levels = create_levels(levels_table)
    curriculum = create_curriculum(curriculum_table)
    levels = assign_curriculum_to_levels(levels, levels_table, curriculum)
    rooms = create_rooms(rooms_table)
    datashows = [DataShow() for _ in range(DATASHOW_COUNT)]
    professors = get_professors(curriculum_table)
    levels = create_sessions(levels, professors, curriculum_table)

    fsei = Faculty(name="FSEI-MOSTA")
    fsei.list_datashows = datashows
    fsei.list_rooms = rooms
    fsei.list_profs = professors
    fsei.list_promo = levels

    return fsei


T = TypeVar("T")


# Global cache to store instances by their _id
_DATACLASS_INSTANCE_CACHE: dict[str, Any] = {}

def dataclass_from_dict(klass: type[T], d: dict[str, Any]) -> T:
    """
    Recursively convert a dictionary into a dataclass, using caching to prevent duplicate instances.

    Args:
        klass: The dataclass type to create.
        d: The dictionary to convert.

    Returns:
        An instance of the dataclass with the dictionary values.
    """
    # Handle None or non-dict inputs
    if d is None or not isinstance(d, dict):
        return d  # Return as-is if not a dictionary

    # Check if the input has an '_id' and it's already in the cache
    instance_id = d.get('_id')
    if instance_id and instance_id in _DATACLASS_INSTANCE_CACHE:
        return _DATACLASS_INSTANCE_CACHE[instance_id]

    try:
        # Get the field types of the dataclass
        fieldtypes = {f.name: f.type for f in fields(klass)} # type: ignore

        # Prepare kwargs for dataclass initialization
        kwargs = {}
        for f, value in d.items():
            if f not in fieldtypes:
                continue  # Skip fields not in the dataclass

            field_type = fieldtypes[f]

            # Handle nested dataclasses and lists of dataclasses
            if hasattr(field_type, "__origin__") and field_type.__origin__ is list: # type: ignore
                # Get the type of list elements
                element_type = field_type.__args__[0] # type: ignore

                # If the list contains dataclasses, recursively convert each element
                if is_dataclass(element_type):
                    kwargs[f] = [dataclass_from_dict(element_type, item) for item in value] # type: ignore
                else:
                    kwargs[f] = value
            elif is_dataclass(field_type):
                # If it's a nested dataclass, recursively convert
                kwargs[f] = dataclass_from_dict(field_type, value) # type: ignore
            else:
                # Simple type, direct assignment
                kwargs[f] = value

        # Create the instance
        instance = klass(**kwargs)

        # Cache the instance if it has an '_id'
        if hasattr(instance, '_id') and instance._id: # type: ignore
            _DATACLASS_INSTANCE_CACHE[instance._id] = instance # type: ignore

        return instance

    except Exception as e:
        raise ValueError(f"Error converting dictionary to {klass.__name__}: {e}")

    
def load_data_from_json(file_path: str = '',json_file:dict[str,Any] = {}) -> Faculty:
    # if both both are available or not available raise error
    if file_path == '' and json == {}:
        raise Exception("No file path or JSON data provided.")
    if file_path != '':
        with open(file_path, encoding="utf-8") as f:
            json_file = json.load(f)
    fac = dataclass_from_dict(Faculty, json_file)
    return fac


if __name__ == "__main__":
    fsei = data_parser()
    fsei_as_dict = asdict(fsei)
    # save as json
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(fsei_as_dict, f, indent=4)
