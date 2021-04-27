from pathlib import Path

from openpyxl import load_workbook

from resources import *

if __name__ == '__main__':
    workbook = load_workbook(filename=Path(r"../test/Resources.xlsx"))
    Module_sheet = workbook['Modules']
    professor_sheet = workbook['Professors']
    groups_sheet = workbook['L3']
    rooms_sheet = workbook['Rooms']
    modules = dict()
    professors = dict()
    rooms = dict()
    sectionL3 = Section()

    for value in Module_sheet.iter_rows(min_row=31, max_row=37, min_col=2, max_col=6, values_only=True):
        mod = Module(value[0], value[1], value[2] or 0, value[3] or 0, value[4] or 0)
        modules[value[0]] = mod

    for value in professor_sheet.iter_rows(min_row=2, values_only=True):
        # print(value)
        module_name, cour_prof, td_prof, tp_prof = value
        modules[module_name].assign_cour_prof(Professor(cour_prof))
        modules[module_name].assign_td_prof(Professor(td_prof))
        modules[module_name].assign_tp_prof(Professor(tp_prof))
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

    # pprint(promoL3.EDT)

    # problem_emploi_du_temp = PET(promos)
