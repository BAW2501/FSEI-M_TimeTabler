import abc
from abc import ABC, abstractmethod
from pprint import pprint

from resources import *


class Constraint(ABC):
    # abstract constraint class
    @staticmethod
    def satisfied(res: LimitedResource, day: int, slot: int) -> bool:
        ...


class HardConstraint(ABC):
    # abstract Hard Constraint class
    def __init__(self, section_timetables: list[Section], section_canvases: list[list[Module]]) -> None:
        super().__init__()
        self.section_timetables = section_timetables
        self.section_canvases = section_canvases

    @abc.abstractmethod
    def satisfied(self, seance: Session, day: int, slot: int) -> bool:
        ...


class SoftConstraint(ABC):
    # abstract Soft Constraint class
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def satisfied(self, assignment) -> bool:
        ...


class ProfessorAvailability(Constraint):
    """a Professor can only teach one session at any given time slot
     so we need to check that """

    # so we need to check if assigning a professor break  this constraint in the method below
    @staticmethod
    def satisfied(prof: Professor, day: int, slot: int) -> bool:
        return prof.is_available_on(day, slot)


class RoomAvailability(Constraint):
    """a Room can only be used for one session at any given time slot
     so we need to check that """

    # so we need to check if assigning a professor break  this constraint in the method below
    @staticmethod
    def satisfied(room: Room, day: int, slot: int) -> bool:
        return room.is_available_on(day, slot)


class StudentAvailability(Constraint):
    """a group can only be taught one session at any given time slot
     so we need to check that """

    # so we need to check if assigning a professor break  this constraint in the method below
    @staticmethod
    def satisfied(g: Group, day: int, slot: int) -> bool:
        return g.is_available_on(day, slot)


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
        self.sessions_list: list[list[(Professor, Attendance, Module, SessionType)]] = [section.required_sessions for
                                                                                        promo in promos for section in
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

        available_and_valid = [ProfessorAvailability.satisfied(seance.prof, day, slot),
                               StudentAvailability.satisfied(seance.attendance, day, slot),
                               RoomAvailability.satisfied(seance.room, day, slot)]
        # then check it's actually valid according to the hard constraints
        # available_and_valid.append(
        #    [hard_constraint.satisfied(seance, day, slot) for hard_constraint in self.hard_constraints])

        return all(available_and_valid)

    def best_fit_room(self, session_type: SessionType, effective: int,day,slot) -> (Room, LimitedResource):
        """ find the smallest room that will fit for the session"""
        rooms_that_fit = list(filter(lambda room: room.capacity >= effective and room.is_available_on(day,slot), self.list_of_rooms))
        if session_type == SessionType.Cour:
            appropriate_rooms = list(
                filter(lambda room: room.type_salle != RoomType.amphi or room.type_salle != RoomType.td,
                       rooms_that_fit))
            return min(appropriate_rooms), LimitedResource()
        else:
            needed = RoomType.td if session_type == SessionType.Td else RoomType.tp
            appropriate_rooms = list(filter(lambda room: room.type_salle != needed,
                                            rooms_that_fit))
            return min(appropriate_rooms), LimitedResource()

    def all_assigned(self) -> bool:
        # TODO this will change after i change the domains
        for sect_sessions in self.sessions_list:
            if len(sect_sessions) != 0:
                return False

        return True

    def first_available_slot(self) -> (int, int, int):
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
        i = 0
        # for i, possible_session in enumerate(sessions):
            # get possible session
        while sessions and i < len(sessions):
            possible_session = sessions[i]
            prof, attendance, module, session_type = possible_session
            # find smalled possible appropriate room
            # TODO  add possibility of using td rooom+ datashow for cours
            # equipment is just a placeholder rn
            room, equipment = self.best_fit_room(session_type, attendance.effective,day,slot)
            # instantiate session object
            possible_session_object = Session(attendance, prof,module, room, session_type)
            if self.valid(possible_session_object, day, slot):
                self.assign(possible_session_object, section, day, slot)
                sessions.pop(i)
                print(len(sessions),"out of 76")
                if self.solve():
                    return True
                else:
                    self.unassign(possible_session_object, section, day, slot)
                    sessions.insert(i, possible_session)
                    i=i+1
            else:
                i=i+1
        self.section_list[section_index].EDT[day][slot].is_full = True
        if self.solve():
            return True

    def assign(self, possible_session, section, day, slot):
        print(day,slot)
        section.EDT[day][slot].add_session(possible_session)
        possible_session.prof.set_busy_on(day, slot)
        possible_session.room.set_busy_on(day, slot)
        possible_session.attendance.set_busy_on(day, slot)
        if possible_session.session_type == SessionType.Cour:
            section.EDT[day][slot].is_full = True
        if len(section.EDT[day][slot].sessions) == section.nb_group:
            section.EDT[day][slot].is_full = True
        # pprint(section.EDT)

    def unassign(self, possible_session, section, day, slot):
        section.EDT[day][slot].sessions.pop()
        possible_session.prof.set_available_on(day, slot)
        possible_session.room.set_available_on(day, slot)
        possible_session.attendance.set_available_on(day, slot)
        section.EDT[day][slot].is_full = False
