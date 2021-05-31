from enum import Enum
from functools import lru_cache
from typing import Union

# this is temporary this will be later taken as class arguments
timeslots_per_day = 6
days_per_week = 5


class LimitedResource:
    def __init__(self, days: int = days_per_week, slots_per_day: int = timeslots_per_day) -> None:
        super().__init__()
        self.days: int = days
        self.slots_per_day: int = slots_per_day
        self.available: list = [[True for _ in range(timeslots_per_day)] for _ in range(days_per_week)]

    def is_available_on(self, day: int, slot_number: int) -> bool:
        return self.available[day][slot_number]

    def set_busy_on(self, day: int, slot_number: int) -> None:
        self.available[day][slot_number] = False

    def set_available_on(self, day: int, slot_number: int) -> None:
        self.available[day][slot_number] = True


class RoomType(Enum):
    amphi = 1
    td = 2
    tp = 3


class SessionType(Enum):
    Cour = 1
    Td = 2
    Tp = 3


class Room(LimitedResource):

    def __init__(self, name: str, type_room: RoomType, cap: int) -> None:
        super().__init__()
        self.name: str = name
        self.capacity: int = cap
        self.type_salle: RoomType = type_room

    def __repr__(self) -> str:
        return self.name

    def __eq__(self, other: 'Room') -> bool:
        return self.capacity == other.capacity

    def __ge__(self, other: 'Room') -> bool:
        return self.capacity >= other.capacity

    def __gt__(self, other: 'Room') -> bool:
        return self.capacity > other.capacity

    def __le__(self, other: 'Room') -> bool:
        return self.capacity <= other.capacity

    def __lt__(self, other: 'Room') -> bool:
        return self.capacity <= other.capacity


@lru_cache(maxsize=None)
class Professor(LimitedResource):
    def __init__(self, name: str) -> None:
        super().__init__()
        self.name: str = name
        self.session_volume: int = 9

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f'prof{self.name}'


class Module:
    def __init__(self, name: str, abbreviation: str, nb_cours: int, nb_td: int, nb_tp: int) -> None:
        super().__init__()
        self.name: str = name
        self.abbreviation: str = abbreviation
        self.nb_cour: int = nb_cours
        self.nb_td: int = nb_td
        self.nb_tp: int = nb_tp

    def __repr__(self) -> str:
        return self.abbreviation


class Group(LimitedResource):
    def __init__(self, number: int, effective: int) -> None:
        super().__init__()
        self.number: int = number
        self.effective: int = effective

    def __repr__(self) -> str:
        return f'G{self.number}'


#
class Section(LimitedResource):

    def __init__(self, section_number: int) -> None:
        super().__init__()
        self.number = section_number
        self.EDT: list[list[TimeSlot]] = [[TimeSlot(day_index, slot_index) for slot_index in range(timeslots_per_day)]
                                          for day_index in range(days_per_week)]
        self.list_group: list[Group] = []
        # for example (prof_a,[1,2,3]) means prof_a teaches attendance 1,2,3
        self.required_sessions: list[tuple[Professor, 'Attendance', Module, SessionType]] = list()

    def add_group(self, gr: Group) -> None:
        self.list_group.append(gr)

    def add_required_session(self, tuple_details: tuple[Professor, 'Attendance', Module, SessionType]) -> None:
        self.required_sessions.append(tuple_details)

    def add_required_sessions(self, tuple_list: list[tuple[Professor, 'Attendance', Module, SessionType]]) -> None:
        self.required_sessions.extend(tuple_list)

    @property
    def nb_group(self) -> int:
        return len(self.list_group)

    @property
    def effective(self):
        return sum(group.effective for group in self.list_group)

    def __repr__(self) -> str:
        return f'section {self.number}'

    def is_available_on(self, day: int, slot_number: int) -> bool:
        return all(group.is_available_on(day, slot_number) for group in self.list_group)

    def set_busy_on(self, day: int, slot_number: int) -> None:
        self.available[day][slot_number] = False
        for group in self.list_group:
            group.set_busy_on(day, slot_number)

    def set_available_on(self, day: int, slot_number: int) -> None:
        self.available[day][slot_number] = True
        for group in self.list_group:
            group.set_available_on(day, slot_number)


Attendance = Union[Group, Section]


class DataShow(LimitedResource):
    """ wrapper around limited resource for data shows does  nothing special in particular """

    def __init__(self, allowed: list['Promotion'], days: int = days_per_week,
                 slots_per_day: int = timeslots_per_day) -> None:
        super().__init__(days, slots_per_day)
        self.allowed = allowed


class Promotion:

    def __init__(self, level: str) -> None:
        super().__init__()
        self.level: str = level
        self.list_section: list[Section] = []
        self.canvas: list[Module] = []

    def add_section(self, sct: Section) -> None:
        self.list_section.append(sct)

    @property
    def nb_section(self) -> int:
        return len(self.list_section)

    def add_module(self, module: Module) -> None:
        self.canvas.append(module)

    @property
    def nb_module(self) -> int:
        return len(self.canvas)

    @property
    def nb_group(self) -> int:
        return sum(section.nb_group for section in self.list_section)

    def find_section(self, section_index: int) -> Union[Section, None]:
        for section in self.list_section:
            if section.number == section_index:
                return section
        return None

    def find_group(self, group_index: int) -> Union[Section, None]:
        for sect in self.list_section:
            for group in sect.list_group:
                if group.number == group_index:
                    return sect
        return None


class Faculty:

    def __init__(self, name: str, promos: list[Promotion] = None, rooms: list[Room] = None,
                 datashows: list[DataShow] = None) -> None:
        super().__init__()
        self.name: str = name
        self.list_promo: list[Promotion] = promos
        self.list_rooms: list[Room] = rooms
        self.list_datashows: list[DataShow] = datashows

    def add_promo(self, promo: Promotion) -> None:
        self.list_promo.append(promo)

    @property
    def nb_promo(self) -> int:
        return len(self.list_promo)


class Session:

    def __init__(self, attendance: Attendance, prof: Professor, module: Module, s: Room,
                 session_type: SessionType) -> None:
        super().__init__()
        self.attendance: Union[Group, Section] = attendance
        self.prof: Professor = prof
        self.module = module
        self.room: Room = s
        self.session_type: SessionType = session_type

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Session):
            equal = [self.attendance == o.attendance,
                     self.prof == o.prof,
                     self.module == o.module,
                     self.session_type == o.session_type]
            return all(equal)

    def __repr__(self) -> str:
        return f"{self.room},{self.prof},{self.attendance},{self.module},{self.session_type}"

    def __str__(self) -> str:
        return f"{self.module}, {self.session_type.name.upper()}/ {self.attendance}, {self.room.name}, {self.prof.name}"


class TimeSlot:

    def __init__(self, day: int, slot_number: int) -> None:
        super().__init__()
        self.day: int = day
        self.slot_number: int = slot_number
        self.sessions: list[Session] = []
        self.is_full: bool = False

    def add_session(self, seance: Session) -> None:
        self.sessions.append(seance)

    @property
    def is_empty(self) -> bool:
        return len(self.sessions) == 0

    def __repr__(self) -> str:
        return self.sessions.__repr__()
