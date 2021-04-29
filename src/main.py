import re
from pathlib import Path
from pprint import pprint
from openpyxl import load_workbook
from resources import *


def parse_assignment(promo: Promotion, session_type: SessionType, assignment_str: str) -> None:
    regex = r"(\w+)\(([*0-9,]+[0-9]*)+\)"
    matches = re.finditer(regex, assignment_str)

    for match in matches:
        prof = match.group(1)
        temp = match.group(2).split(",")
        if session_type == SessionType.Cour:
            if temp[0] == '*':
                attendance = list(range(1, len(promo.list_section) + 1))
            else:
                attendance = [int(section_index) for section_index in temp]
            for attendance_index in attendance:
                if sect_found := promo.find_section(attendance_index):
                    sect_found.add_required_session((Professor(prof), sect_found, session_type))
        else:
            # they are tds or tps
            if temp[0] == '*':
                attendance = list(range(1, promo.nb_group + 1))
            else:
                attendance = [int(group_index) for group_index in temp]
            for group_index in attendance:
                if sect_found := promo.find_group(group_index):
                    group = sect_found.list_group[group_index - 1]
                    sect_found.add_required_session((Professor(prof), group, session_type))


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
    sectionL3 = Section(1)

    for group_row in groups_sheet.iter_rows(min_row=2, values_only=True):
        group_name, effective = group_row
        sectionL3.add_group(Group(group_name, effective))

    for module_row in Module_sheet.iter_rows(min_row=31, max_row=37, min_col=2, max_col=6, values_only=True):
        mod = Module(module_row[0], module_row[1], module_row[2] or 0, module_row[3] or 0, module_row[4] or 0)
        modules[module_row[0]] = mod

    promoL3 = Promotion("L3")
    promoL3.add_section(sectionL3)
    promoL3.canvas = list(modules.values())

    for assignment_row in professor_sheet.iter_rows(min_row=2, values_only=True):
        # print(value)
        module_name, cour_assignment, td_assignment, tp_assignment = assignment_row
        if cour_assignment is not None:
            parse_assignment(promoL3, SessionType.Cour, cour_assignment)
        if td_assignment is not None:
            parse_assignment(promoL3, SessionType.Td, td_assignment)
        if tp_assignment is not None:
            parse_assignment(promoL3, SessionType.Tp, tp_assignment)

    for room in rooms_sheet.iter_rows(min_row=2, values_only=True):
        room_name, room_type, capacity = room
        rooms[room_name] = Room(room_name, room_type, capacity)
        # print(room_name, room_type, capacity)

    promos = [promoL3]

    # pprint(promoL3.EDT)

    # problem_emploi_du_temp = PET
    for sect in promoL3.list_section:
        for assign in sect.required_sessions:
            pprint(assign)
    print(len(promoL3.list_section[0].required_sessions))
