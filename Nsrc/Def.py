from dataclasses import dataclass, field
from enum import Enum
from uuid import uuid4

"""Models for university course scheduling system"""

# Constants
TIME_SLOTS_PER_DAY = 6
DAYS_PER_WEEK = 5


def get_new_uuid() -> str:
    return str(uuid4())


# Enumerations
class RoomType(str, Enum):
    AMPHI = "Amphi"
    TU = "TUTORIAL"
    LAB = "LABORATORY"


class SessionType(str, Enum):
    LECTURE = "LECTURE"
    TU = "TUTORIAL"
    LAB = "LABORATORY"


@dataclass(kw_only=True)
class BaseClass:
    _id: str = field(default_factory=get_new_uuid)


class LimitedResource(BaseClass):
    availability_matrix: list[list[bool]] = [
        [True for _ in range(TIME_SLOTS_PER_DAY)] for _ in range(DAYS_PER_WEEK)
    ]


@dataclass(kw_only=True)
class Room(LimitedResource):
    name: str
    room_type: RoomType
    capacity: int


@dataclass(kw_only=True)
class Professor(LimitedResource):
    name: str


@dataclass(kw_only=True)
class Module(BaseClass):
    name: str
    abbreviation: str
    semester: int
    number_of_lectures: int
    number_of_tutorials: int
    number_of_labs: int


@dataclass(kw_only=True)
class Group(LimitedResource):
    number: int
    effective: int


@dataclass(kw_only=True)
class Section(LimitedResource):
    number: int
    list_group: list[Group] = field(default_factory=list)


@dataclass(kw_only=True)
class PendingSession(BaseClass):
    prof: Professor
    attendance: Section | Group
    module: Module
    session_type: SessionType


@dataclass(kw_only=True)
class Session(BaseClass):
    attendance: Group | Section
    prof: Professor
    module: Module
    room: Room
    session_type: SessionType


@dataclass(kw_only=True)
class Level(BaseClass):
    name: str
    curriculum: list[Module] = field(default_factory=list)
    list_section: list[Section] = field(default_factory=list)
    required_sessions: list[PendingSession] = field(default_factory=list)
    schedule: list[list[list[list[Session]]]] = field(default_factory=list)
    # first list for sessions,slots,days,sections
    # schedule[i] is the week schedule for section i
    # schedule[i][j] is the schedule for day j in section i
    # schedule[i][j][k] is the sessions for slot k in day j in section i
    # schedule[i][j][k][l] is the session l in slot k in day j in section i


@dataclass(kw_only=True)
class DataShow(LimitedResource):
    pass


@dataclass(kw_only=True)
class Faculty(BaseClass):
    name: str
    list_promo: list[Level] = field(default_factory=list)
    list_rooms: list[Room] = field(default_factory=list)
    list_datashows: list[DataShow] = field(default_factory=list)
    list_profs: list[Professor] = field(default_factory=list)

    @property
    def number_students(self):
        return sum(
            group.effective
            for level in self.list_promo
            for section in level.list_section
            for group in section.list_group
        )

    @property
    def number_professors(self):
        return len(self.list_profs)

    @property
    def number_rooms(self):
        return len(self.list_rooms)
