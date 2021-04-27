import abc
from abc import ABC, abstractmethod
from copy import deepcopy

from resources import *


class Constraint(ABC):
    @staticmethod
    def satisfied(res: LimitedResource, day: int, slot: int) -> bool:
        ...


class HardConstraint(ABC):
    def __init__(self, section_timetables: list[Section], section_canvases: list[list[Module]]) -> None:
        super().__init__()
        self.section_timetables = section_timetables
        self.section_canvases = section_canvases

    @abc.abstractmethod
    def satisfied(self, seance: Session, day: int, slot: int) -> bool:
        ...


class SoftConstraint(ABC):
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


# TODO i only have one prof per assignment atm so better implement that later

class PET:
    def __init__(self, promos: list[Promotion]) -> None:
        # flattening the variables and assignments which are
        # the promos with their edt and their canvas which are their domains
        self.section_list: list[Section] = [section for promo in promos for section in promo.list_section]
        self.canvas_list: list[list[Module]] = [deepcopy(promo.canvas) for promo in promos for _ in
                                                promo.list_section]
        self.sessions_list:list[list[(Module,)]]
        self.hard_constraints: list[HardConstraint] = []
        self.soft_constraints: list[SoftConstraint] = []

    def add_hard_constraint(self, constraint: HardConstraint) -> None:
        self.hard_constraints.append(constraint)

    def add_soft_constraint(self, constraint: SoftConstraint) -> None:
        self.soft_constraints.append(constraint)

    def consistent(self, seance: Session, day: int, slot: int) -> bool:
        available = [ProfessorAvailability.satisfied(seance.prof, day, slot),
                     StudentAvailability.satisfied(seance.attendance, day, slot),
                     RoomAvailability.satisfied(seance.room, day, slot)]
        return all(available)

    def all_assigned(self) -> bool:
        for canvas in self.canvas_list:
            for module in canvas:
                unassigned = [module.nb_cour is not 0,
                              module.nb_td is not 0,
                              module.nb_tp is not 0]
                if any(unassigned):
                    return False
        return True

    def first_available_slot(self) -> TimeSlot:
        """ iterates over the sections  and finds the first available timeslot"""
        for sect in self.section_list:
            for day_index in range(days_per_week):
                for slot_index in range(timeslots_per_day):
                    if not sect.EDT[day_index][slot_index].is_full:
                        return sect.EDT[day_index][slot_index]

        raise Exception("not enough timeslots to assign all sessions")

    # https://github.com/davecom/ClassicComputerScienceProblemsInPython/blob/master/Chapter3/csp.py
    # https://github.com/davecom/ClassicComputerScienceProblemsInPython/blob/master/Chapter3/queens.py
    def solve(self) -> bool:
        if self.all_assigned():
            return True
        slot = self.first_available_slot()
