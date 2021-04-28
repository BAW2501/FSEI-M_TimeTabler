import re
from pathlib import Path
from pprint import pprint

from openpyxl import load_workbook

from resources import *


def parse_assignment(assignment_str: str):
    regex = r"(\w+)\(([*0-9,]+[0-9]*)+\)"
    matches = re.finditer(regex, assignment_str)
    assignment: set[(str, list[int])] = set()

    for match in matches:
        prof = match.group(1)
        temp = match.group(2).split(",")
        if temp[0] == '*':
            attendance = list(range(1, 8))
        else:
            attendance = [int(intger) for intger in temp]
        assignment.add((Professor(prof), attendance))
    return assignment


if __name__ == '__main__':
    # using the data in the test file to check the validity of the data model
    # the code looks bad but it's only test code
    workbook = load_workbook(filename=Path(r"../test/Resources.xlsx"))
    Module_sheet = workbook['Modules']
    professor_sheet = workbook['Professors']
    groups_sheet = workbook['L3']
    rooms_sheet = workbook['Rooms']
    modules = dict()
    professors = dict()
    rooms = dict()
    sectionL3 = Section()

    for module_row in Module_sheet.iter_rows(min_row=31, max_row=37, min_col=2, max_col=6, values_only=True):
        mod = Module(module_row[0], module_row[1], module_row[2] or 0, module_row[3] or 0, module_row[4] or 0)
        modules[module_row[0]] = mod

    for assignment_row in professor_sheet.iter_rows(min_row=2, values_only=True):
        # print(value)
        module_name, cour_assignment, td_assignment, tp_assignment = assignment_row
        if cour_assignment is not None:
            modules[module_name].assign_cour_prof(parse_assignment(cour_assignment))
        if td_assignment is not None:
            modules[module_name].assign_td_prof(parse_assignment(td_assignment))
        if tp_assignment is not None:
            modules[module_name].assign_tp_prof(parse_assignment(tp_assignment))

    for group_row in groups_sheet.iter_rows(min_row=2, values_only=True):
        group_name, effective = group_row
        sectionL3.add_group(Group(group_name, effective))

    for room in rooms_sheet.iter_rows(min_row=2, values_only=True):
        room_name, room_type, capacity = room
        rooms[room_name] = Room(room_name, room_type, capacity)
        print(room_name, room_type, capacity)

    promoL3 = Promotion("L3")
    promoL3.add_section(sectionL3)
    promoL3.canvas = list(modules.values())

    promos = [promoL3]

    for module in promoL3.canvas:
        pprint(module)

    # pprint(promoL3.EDT)

    # problem_emploi_du_temp = PET(promos)
