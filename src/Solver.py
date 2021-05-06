from abc import ABC, abstractmethod

from resources import *


class HardConstraint(ABC):
    # abstract Hard Constraint class
    def __init__(self, section_timetables: list[Section] = None, section_canvases: list[list[Module]] = None) -> None:
        super().__init__()
        self.section_timetables = section_timetables
        self.section_canvases = section_canvases

    @abstractmethod
    def satisfied(self, seance: Session, day: int, slot: int) -> bool:
        ...


class SoftConstraint(ABC):
    # abstract Soft Constraint class
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def satisfied(self, assignment) -> bool:
        ...


class ProfessorAvailability(HardConstraint):
    """a Professor can only teach one session at any given time slot
     so we need to check that """

    # so we need to check if assigning a professor break  this constraint in the method below
    def satisfied(self, seance: Session, day: int, slot: int) -> bool:
        return seance.prof.is_available_on(day, slot)


class RoomAvailability(HardConstraint):
    """a Room can only be used for one session at any given time slot
     so we need to check that """

    # so we need to check if assigning a professor break  this constraint in the method below
    def satisfied(self, seance: Session, day: int, slot: int) -> bool:
        return seance.room.is_available_on(day, slot)


class StudentAvailability(HardConstraint):
    """a group can only be taught one session at any given time slot
     so we need to check that """

    # so we need to check if assigning a professor break  this constraint in the method below
    def satisfied(self, seance: Session, day: int, slot: int) -> bool:
        return seance.attendance.is_available_on(day, slot)


class ThreeConsecutiveMaxSessions(HardConstraint):
    """a group or professor should have at most Three consecutive sessions """

    def satisfied(self, seance: Session, day: int, slot: int) -> bool:
        if slot < 3:
            return True
        if any(seance.prof.available[day][slot - 3:slot]):
            return True
        return False


class TwoCourPerDayMax(HardConstraint):
    def satisfied(self, seance: Session, day: int, slot: int) -> bool:
        if slot < 2 or seance.session_type != SessionType.Cour:
            return True

        cour_count = 0
        attendance: Section = seance.attendance
        for slot in attendance.EDT[day]:
            if slot.sessions and slot.sessions[0].session_type == SessionType.Cour:
                cour_count += 1

        return cour_count < 2


def assign(possible_session, section, day, slot):
    section.EDT[day][slot].add_session(possible_session)
    possible_session.prof.set_busy_on(day, slot)
    possible_session.room.set_busy_on(day, slot)
    possible_session.attendance.set_busy_on(day, slot)
    if possible_session.session_type == SessionType.Cour:
        section.EDT[day][slot].is_full = True
    if len(section.EDT[day][slot].sessions) == section.nb_group // 2 + 1:
        section.EDT[day][slot].is_full = True
    # pprint(section.EDT)


def unassign(possible_session, section, day, slot):
    section.EDT[day][slot].sessions.pop()
    possible_session.prof.set_available_on(day, slot)
    possible_session.room.set_available_on(day, slot)
    possible_session.attendance.set_available_on(day, slot)
    section.EDT[day][slot].is_full = False


class PET:
    """ this problem is a constraint satisfaction problem
    which in we have a set of variables in this example the set to time tables
    and a set of domains in this examples the sessions(les seances) one for each variable
    and we have to assign the variables a value from their respective domain """

    def __init__(self, promos: list[Promotion], rooms: list[Room]) -> None:

        # our variables
        self.section_list: list[Section] = [section for promo in promos for section in promo.list_section]
        # the domains but not in usable form
        # self.canvas_list: list[list[Module]] = [deepcopy(promo.canvas) for promo in promos for _ in
        #                                       promo.list_section]
        # our actual domains  not implemented yet until i clear up the type of input i'll be getting from the user
        self.sessions_list: list[list[tuple[Professor, Attendance, Module, SessionType]]] = [section.required_sessions
                                                                                             for
                                                                                             promo in promos for section
                                                                                             in
                                                                                             promo.list_section]
        self.list_of_rooms: list[Room] = rooms
        # list of hard and soft constraints pretty self explanatory
        self.hard_constraints: list[HardConstraint] = []
        self.soft_constraints: list[SoftConstraint] = []

    def add_hard_constraint(self, constraint: HardConstraint) -> None:
        self.hard_constraints.append(constraint)

    def add_soft_constraint(self, constraint: SoftConstraint) -> None:
        self.soft_constraints.append(constraint)

    def valid(self, seance: Session, day: int, slot: int) -> bool:
        """ check that the timetable is still valid when inserting a new session  """
        # first check it's physically possible

        # then check it's actually valid according to the hard constraints

        return all([constraint.satisfied(seance, day, slot) for constraint in self.hard_constraints])

    def best_fit_room(self, session_type: SessionType, effective: int, day, slot) -> tuple[Room, LimitedResource]:
        """ find the smallest room that will fit for the session"""

        appropriate_type = []
        if session_type == SessionType.Tp:
            appropriate_type.append(RoomType.tp.value)
        else:
            appropriate_type.append(RoomType.td.value)
        if session_type == SessionType.Cour:
            appropriate_type.append(RoomType.amphi.value)
        # appropriate_rooms = list(filter(lambda room: room.capacity >= effective and room.is_available_on(day, slot)
        #                                             and room.type_salle in appropriate_type, self.list_of_rooms))
        appropriate_rooms = [room for room in self.list_of_rooms if room.capacity >= effective
                             and room.is_available_on(day, slot)
                             and room.type_salle in appropriate_type]
        if appropriate_rooms:
            return min(appropriate_rooms), LimitedResource()
        else:
            return None, None

    def all_assigned(self) -> bool:
        # TODO this will change after i change the domains
        for sect_sessions in self.sessions_list:
            if len(sect_sessions) != 0:
                return False

        return True

    def first_available_slot(self) -> tuple[int, int, int]:
        """ iterates over the sections  and finds the first available timeslot"""
        # TODO to guarantee equity between all promos and sections this should iterate slot by slot rather than
        #  section by section
        for section_index, sect in enumerate(self.section_list):
            for day_index in range(days_per_week):
                for slot_index in range(timeslots_per_day):
                    if not sect.EDT[day_index][slot_index].is_full:
                        return section_index, day_index, slot_index

        raise Exception("not enough timeslots to assign all sessions")

    def solve(self) -> bool:
        if self.all_assigned():
            return True
        section_index, day, slot = self.first_available_slot()
        section = self.section_list[section_index]
        sessions = self.sessions_list[section_index]

        for i, possible_session in enumerate(sessions[:]):

            prof, attendance, module, session_type = possible_session
            # getting room
            room, equipment = self.best_fit_room(session_type, attendance.effective, day, slot)
            # instantiate session object
            possible_session_object = Session(attendance, prof, module, room, session_type)
            if room and self.valid(possible_session_object, day, slot):
                assign(possible_session_object, section, day, slot)
                sessions.pop(i)
                if self.solve():
                    return True
                else:
                    unassign(possible_session_object, section, day, slot)
                    sessions.insert(i, possible_session)
        section.EDT[day][slot].is_full = True
        if self.solve():
            return True
        else:
            return False
