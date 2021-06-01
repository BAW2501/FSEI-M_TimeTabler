import time
from pathlib import Path

from openpyxl import load_workbook
from openpyxl.styles import Font, Alignment

from Solver import *
from resources import *


def excel_export(promo_list: list[Promotion],path:str,example:str=r"../test/result.xlsx"):
    # saving solution to an excel file
    export_workbook = load_workbook(filename=Path(example))

    for promo in promo_list:
        for sect in promo.list_section:
            EDT_sheet = export_workbook.copy_worksheet(export_workbook["template"])
            EDT_sheet.title = f'{promo.level}_{sect.number}'
            EDT_sheet["A5"] = f"Emploi du {promo.level}"
            nb_row = sect.nb_group
            for day in sect.EDT:
                for slot in day:
                    if len(slot.sessions) > nb_row:
                        nb_row = len(slot.sessions)
            # print(EDT_sheet[7][1].value)
            for j, day in enumerate(sect.EDT, start=1):
                for k, slot in enumerate(day, start=2):
                    slot.sessions.sort(key=lambda s: s.attendance.number)
                    for session_index, session in enumerate(slot.sessions, start=1):
                        # print(j * 7 + i,k)
                        nb_row = max(9, sect.nb_group)
                        start_session_index = (j - 1) * nb_row + session_index + 7
                        end_session_index = j * nb_row + session_index - 1 + 7
                        if nb_row > 9:
                            EDT_sheet.insert_rows(end_session_index - 2, nb_row - 9)
                        if session.session_type == SessionType.Cour:
                            EDT_sheet.merge_cells(start_row=start_session_index, start_column=k,
                                                  end_row=end_session_index,
                                                  end_column=k)
                            EDT_sheet.cell(start_session_index, k).font = Font(bold=True)
                            EDT_sheet.cell(start_session_index, k).alignment = Alignment(wrap_text=True,
                                                                                         horizontal='center',
                                                                                         vertical='center')
                        EDT_sheet.cell(start_session_index, k).value = str(session)
    del export_workbook["template"]
    export_workbook.save(path or 'FSEI_Mosta_EDT.xlsx')


def get_data(xlsx):
    modules_dict = {}
    promos_dict = {}
    professors_dict = {}
    # using the data in the test file to check the validity of the data model
    # the code looks bad but it's only test code
    workbook = load_workbook(filename=Path(xlsx), read_only=True)
    Module_sheet = workbook['Modules']
    promos_sheet = workbook['Promos']
    rooms_sheet = workbook['Rooms']
    for promo_row in promos_sheet.iter_rows(min_row=2, values_only=True):
        promo_name, nb_section, nb_group, group_effective, mod_start, mod_end = promo_row
        promos_dict[promo_name] = Promotion(promo_name)
        promos_dict[promo_name].list_section = [Section(i + 1) for i in range(nb_section)]
        for section in promos_dict[promo_name].list_section:
            section.list_group = [Group(i + 1, group_effective) for i in range(nb_group // nb_section)]
            nb_group -= nb_group // nb_section
            nb_section -= 1
        for module_row in Module_sheet.iter_rows(min_row=mod_start, max_row=mod_end, min_col=2, values_only=True):
            # print(module_row)
            mod = Module(module_row[0], module_row[1], module_row[2] or 0, module_row[3] or 0, module_row[4] or 0)
            modules_dict[module_row[0]] = mod
            cour_str, td_str, tp_str = module_row[5], module_row[6], module_row[7]
            if cour_str:
                cour_profs_strings = cour_str.split(",")
                cour_profs = []
                for prof_string in cour_profs_strings:
                    name = prof_string.split("(")[0]
                    times = int(prof_string[prof_string.find("(") + 1].split(")")[0])
                    cour_profs.extend([Professor(name) for _ in range(times * mod.nb_cour)])
                for sect_i in promos_dict[promo_name].list_section:
                    sect_i.add_required_sessions(
                        [(cour_profs.pop(), sect_i, mod, SessionType.Cour) for _ in range(mod.nb_cour)])
            if td_str:
                td_profs_strings = td_str.split(",")
                td_profs = []
                for prof_string in td_profs_strings:
                    name = prof_string.split("(")[0]
                    times = int(prof_string[prof_string.find("(") + 1].split(")")[0])
                    td_profs.extend([Professor(name) for _ in range(times * mod.nb_td)])
                for sect_i in promos_dict[promo_name].list_section:
                    for group in sect_i.list_group:
                        sect_i.add_required_sessions(
                            [(td_profs.pop(), group, mod, SessionType.Td) for _ in range(mod.nb_td)])
            if tp_str:
                tp_profs_strings = tp_str.split(",")
                tp_profs = []
                for prof_string in tp_profs_strings:
                    name = prof_string.split("(")[0]
                    times = int(prof_string[prof_string.find("(") + 1].split(")")[0])
                    tp_profs.extend([Professor(name) for _ in range(times * mod.nb_tp)])
                for sect_i in promos_dict[promo_name].list_section:
                    for group in sect_i.list_group:
                        sect_i.add_required_sessions(
                            [(tp_profs.pop(), group, mod, SessionType.Tp) for _ in range(mod.nb_tp)])
                    sect_i.required_sessions.sort(key=lambda s: s[3].value)
    # *room == room_name, room_type, capacity = room
    rooms_list = [(Room(*room)) for room in rooms_sheet.iter_rows(min_row=2, values_only=True)]
    return modules_dict, promos_dict, professors_dict, rooms_list


if __name__ == '__main__':
    start = time.perf_counter()
    modules, promos, professors, rooms = get_data(r"../test/Resources.xlsx")
    promos = list(promos.values())
    data_shows = [DataShow(promos[:10]) for _ in range(4)]
    data_shows.extend([DataShow(promos[13:15]) for _ in range(2)])
    physic = promos[10:13] + [promos[-1]]
    data_shows.extend([DataShow(physic) for _ in range(2)])
    fsei_mosta = Faculty("FSEI-MOSTA", promos, rooms, data_shows)

    end = time.perf_counter()
    print("Time for import from excel +:", format((end - start) * 1000, ".2f"), "ms")
    start = time.perf_counter()

    # promos.reverse()
    problem_emploi_du_temp = PET(fsei_mosta)
    number_assignments = sum(len(session_list) for session_list in problem_emploi_du_temp.sessions_list)
    problem_emploi_du_temp.add_hard_constraint(ProfessorAvailability())
    problem_emploi_du_temp.add_hard_constraint(StudentAvailability())
    problem_emploi_du_temp.add_hard_constraint(RoomAvailability())
    problem_emploi_du_temp.add_hard_constraint(ThreeConsecutiveMaxSessions())
    problem_emploi_du_temp.add_hard_constraint(TwoCourPerDayMax())
    # very inefficient to add this
    problem_emploi_du_temp.add_hard_constraint(UniqueSessionDaily())
    #

    if problem_emploi_du_temp.solve():
        end = time.perf_counter()
        print("successfully generated EDT(", number_assignments, " assignments) in",
              format((end - start) * 1000, ".2f"), "ms")
    else:
        print("nope debug more")
    # promos.reverse()
    start = time.perf_counter()
    excel_export(list(promos),"")
    end = time.perf_counter()
    print("exported to excel in", format((end - start) * 1000, ".2f"), "ms")