from enum import Enum
from functools import lru_cache
from typing import Union

# this is temporary this will be later taken as class arguments
timeslots_per_day = 8
days_per_week = 5


# TODO make a mock up solver function
# TODO  implement multiple teacher per type of session cause you can only set one for now


class LimitedResource:
    def __init__(self, days: int = days_per_week, slots_per_day: int = timeslots_per_day) -> None:
        super().__init__()
        self.days: int = days
        self.slots_per_day: int = slots_per_day
        self.available: list = [[True] * self.slots_per_day] * self.days

    def is_available_on(self, day: int, slot_number: int) -> bool:
        return self.available[day][slot_number]

    def set_busy_on(self, day: int, slot_number: int) -> None:
        self.available[day][slot_number] = False


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


@lru_cache(maxsize=None)
class Professor(LimitedResource):
    def __init__(self, name: str) -> None:
        super().__init__()
        self.name: str = name
        self.session_volume: int = 9

    def __str__(self) -> str:
        return self.name


class Module:
    def __init__(self, name: str, abbreviation: str, nb_cours: int, nb_td: int, nb_tp: int) -> None:
        super().__init__()
        self.name: str = name
        self.abbreviation: str = abbreviation
        self.nb_cour: int = nb_cours
        self.nb_td: int = nb_td
        self.nb_tp: int = nb_tp
        self.cour_profs: set[Professor] = set()
        self.td_profs: set[Professor] = set()
        self.tp_profs: set[Professor] = set()

    def assign_cour_prof(self, prof: Professor) -> None:
        if prof.name is not None:
            self.cour_profs.add(prof)

    def assign_td_prof(self, prof: Professor) -> None:
        if prof.name is not None:
            self.td_profs.add(prof)

    def assign_tp_prof(self, prof: Professor) -> None:
        if prof.name is not None:
            self.tp_profs.add(prof)


class Group(LimitedResource):
    def __init__(self, number: int, effective: int) -> None:
        super().__init__()
        self.number: int = number
        self.effective: int = effective


class Section(LimitedResource):

    def __init__(self) -> None:
        super().__init__()
        self.EDT: list[list[TimeSlot]] = [[TimeSlot(day_index, slot_index) for slot_index in range(timeslots_per_day)]
                                          for day_index in range(days_per_week)]
        self.list_group: list[Group] = []

    def add_group(self, gr: Group) -> None:
        self.list_group.append(gr)

    @property
    def nb_group(self) -> int:
        return len(self.list_group)

    @property
    def effective(self):
        return sum(group.effective for group in self.list_group)

    def is_available_on(self, day: int, slot_number: int) -> bool:
        return all([group.is_available_on(day, slot_number) for group in self.list_group])

    def set_busy_on(self, day: int, slot_number: int) -> None:
        for group in self.list_group:
            group.set_busy_on(day, slot_number)


Attendance = Union[Group, Section]


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


class Department:
    list_promo: list[Promotion] = []

    def __init__(self, name: str) -> None:
        super().__init__()
        self.name: str = name

    def add_promo(self, promo: Promotion) -> None:
        self.list_promo.append(promo)

    @property
    def nb_promo(self) -> int:
        return len(self.list_promo)


class Session:

    def __init__(self, attendance: Attendance, prof: Professor, s: Room, session_type: SessionType) -> None:
        super().__init__()
        self.attendance: Union[Group, Section] = attendance
        self.prof: Professor = prof
        self.room: Room = s
        self.session_type: SessionType = session_type


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
        return f"({self.day},{self.slot_number})"
