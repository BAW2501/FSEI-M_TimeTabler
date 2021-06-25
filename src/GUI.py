# -*- coding: utf-8 -*-
import datetime
import os
import pickle
import sys

import main
import resources
from Gui_files.inputDiags import *
from Gui_files.ui_window import *
from Solver import *


def session_type_from_int(task):
    if task == 1:
        return "Lecture"
    elif task == 2:
        return "TD"
    else:
        return "TP"


def room_type_from_int(task):
    if task == 1:
        return "Amphi"
    elif task == 2:
        return "TD"
    else:
        return "TP"


class MainWindow(QMainWindow):
    def __init__(self):

        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.current_project_file = None
        self.promos = []
        self.profs = []
        self.rooms = []
        self.modules = []
        self.module_assignments = []
        self.datashows = []
        self.number_of_days_per_week_input = 5
        self.number_of_slots_per_day_input = 7
        self.slot_duration_input = 60
        self.starting_day_input = 1
        self.professor_availability_constraint_checked = True
        self.student_availability_constraint_checked = True

        self.room_availability_constraint_checked = True
        self.three_consecutive_sessions_constraint_checked = False
        self.two_cour_per_day_max_constraint_checked = False
        self.unique_session_daily_constraint_checked = False
        self.min_prof_days_constraint_checked = False
        self.cours_first_constraint_checked = False
        self.faculty = Faculty("FSEI-MOSTA")
        self.problem_emploi_du_temp = None

    def bind(self):

        self.ui.promo_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.professor_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.room_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.modules_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.modules_assign_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.datashows_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.timetable_tableview.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.timetable_tableview.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.pick_promo__modules_comboBox.setCurrentIndex(0)

        self.ui.promo_add_pushbutton.clicked.connect(self.promo_input)
        self.ui.promo_edit__pushbutton.clicked.connect(self.edit_promo)
        self.ui.promo_remove_pushbutton.clicked.connect(self.delete_promo)
        self.ui.prof_add_pushbutton.clicked.connect(self.prof_input)
        self.ui.prof_edit_pushbutton.clicked.connect(self.edit_prof)
        self.ui.prof_remove_pushbutton.clicked.connect(self.delete_prof)
        self.ui.room_add_pushbutton.clicked.connect(self.room_input)
        self.ui.room_edit_pushbutton.clicked.connect(self.edit_room)
        self.ui.room_remove_pushbutton.clicked.connect(self.delete_room)
        self.ui.module_add_pushbutton.clicked.connect(self.module_input)
        self.ui.module_edit_pushbutton.clicked.connect(self.edit_module)
        self.ui.module_remove_pushbutton.clicked.connect(self.delete_module)
        self.ui.assignment_add_pushbutton.clicked.connect(self.assign_input)
        self.ui.assignment_edit_pushbutton.clicked.connect(self.edit_assign_data)
        self.ui.assignment_remove_pushbutton.clicked.connect(self.delete_assign_data)
        self.ui.datashow_add_pushbutton.clicked.connect(self.datashow_input)
        self.ui.datashow_edit_pushbutton.clicked.connect(self.edit_datashow)
        self.ui.datashow_remove_pushbutton.clicked.connect(self.delete_datashow)

        self.ui.pick_promo__modules_comboBox.currentIndexChanged.connect(self.load_module_data)
        self.ui.assign_pick_promo_assign_comboBox.currentIndexChanged.connect(self.refresh_modules_combo)

        self.ui.assign_pick_promo_assign_comboBox.currentIndexChanged.connect(self.load_assign_data)
        self.ui.module_picker_comboBox.currentIndexChanged.connect(self.load_assign_data)

        self.ui.pick_promo_comboBox_TT.currentIndexChanged.connect(self.refresh_section_combo)
        self.ui.timetable_tableview.doubleClicked.connect(self.timetable_input)
        self.ui.pick_section_comboBox.currentIndexChanged.connect(self.load_timetable_data)
        self.ui.pick_promo_comboBox_TT.currentIndexChanged.connect(self.load_timetable_data)

        self.ui.days_per_week_spinBox.valueChanged.connect(self.update_options)
        self.ui.slots_perday_spinBox.valueChanged.connect(self.update_options)
        self.ui.slot_duration_spinBox.valueChanged.connect(self.update_options)
        self.ui.starting_day_comboBox.currentIndexChanged.connect(self.update_options)
        self.ui.professoravailability_checkBox.stateChanged.connect(self.update_options)
        self.ui.studentavailability_checkBox.stateChanged.connect(self.update_options)
        self.ui.roomavailability_checkBox.stateChanged.connect(self.update_options)
        self.ui.threeconsecutivemaxsessions_checkBox.stateChanged.connect(self.update_options)
        self.ui.twocourderdaymax_checkBox.stateChanged.connect(self.update_options)
        self.ui.uniquesessiondaily_checkBox.stateChanged.connect(self.update_options)
        self.ui.CoursFirst.stateChanged.connect(self.update_options)
        self.ui.MinProfDays.stateChanged.connect(self.update_options)

        self.load_promo_data()
        self.load_prof_data()
        self.load_room_data()
        self.load_module_data()
        self.load_assign_data()
        self.load_datashow_data()
        self.ui.spec_ribbon.currentChanged.connect(self.on_spec_tab_change)
        self.ui.ribbon.currentChanged.connect(self.on_ribbon_tab_change)
        self.ui.save_project_pushButton.clicked.connect(self.save_project_file)
        self.ui.open_project_pushButton.clicked.connect(self.open_project_file)
        self.ui.new_project_pushButton.clicked.connect(self.get_new_file_path)

        # self.ui.verticalLayout_15.removeWidget(self.ui.timetable_tableview)
        # self.ui.verticalLayout_15.addWidget(self.ui.timetable_tableview)
        self.ui.generate_pushButton.setEnabled(True)
        self.ui.generate_pushButton.clicked.connect(self.generate_timetable)
        self.ui.export_excel_pushButton.clicked.connect(self.export_excel_file)
        self.update_options()

    def open_project_file(self):
        file_path = self.get_open_file_path()
        self.current_project_file = file_path
        with open(file_path, 'rb') as f:
            self.promos, self.profs, self.modules, self.module_assignments, self.rooms, self.datashows = pickle.load(f)
        # print(self.promos)
        self.load_module_data()
        self.load_promo_data()
        self.load_prof_data()
        self.load_assign_data()
        self.load_room_data()
        self.load_datashow_data()

    def get_save_file_path(self):
        save_path, ok = QFileDialog.getSaveFileUrl(self, "save TPP file ", '', "TimeTableProject (*.TTP)")
        if ok:
            return save_path.toLocalFile()
        else:
            return None

    def get_open_file_path(self):
        open_path, ok = QFileDialog.getOpenFileUrl(self, "open TPP file ", '', "TimeTableProject (*.TTP)")
        return open_path.toLocalFile() if ok else None

    def get_new_file_path(self):
        open_path, ok = QFileDialog.getSaveFileUrl(self, "save TPP file ", '', "TimeTableProject (*.TTP)")
        self.current_project_file = open_path.toLocalFile() if ok else None
        with open(self.current_project_file, 'wb') as f:
            pickle.dump([], f)

    def save_project_file(self):
        file_path = self.current_project_file or self.get_save_file_path()
        with open(file_path, 'wb') as f:
            pickle.dump([self.promos, self.profs, self.modules, self.module_assignments, self.rooms, self.datashows], f)

    def promo_input(self):
        diag = PromoInputDialog()
        diag.setModal(True)
        if diag.exec():
            row = diag.get_inputs()
            insert_row_index = self.ui.promo_table.rowCount()
            self.modules.append([])
            self.module_assignments.append([])

            self.ui.promo_table.insertRow(insert_row_index)
            for j, v in enumerate(row):
                self.ui.promo_table.setItem(
                    insert_row_index, j, QTableWidgetItem(str(v)))
            self.promos.append({'Name': row[0], 'Number of Sections': row[1], 'Number of Groups': row[2],
                                'Effective per Group': row[3]})

    def load_promo_data(self):
        self.ui.promo_table.setRowCount(len(self.promos))

        for i, promo in enumerate(self.promos):
            self.ui.promo_table.setItem(i, 0, QTableWidgetItem(promo["Name"]))
            self.ui.promo_table.setItem(i, 1, QTableWidgetItem(str(promo["Number of Sections"])))
            self.ui.promo_table.setItem(i, 2, QTableWidgetItem(str(promo['Number of Groups'])))
            self.ui.promo_table.setItem(i, 3, QTableWidgetItem(str(promo['Effective per Group'])))

    def edit_promo(self):
        index = self.ui.promo_table.selectedIndexes()
        if index:
            index = index[0].row()  # cause single selection
            diag = PromoInputDialog()

            diag.name.setText(self.ui.promo_table.item(index, 0).text())
            diag.numberOfSectionsSpinBox.setValue(
                int(self.ui.promo_table.item(index, 1).text()))
            diag.numberOfGroupsSpinBox.setValue(
                int(self.ui.promo_table.item(index, 2).text()))
            diag.effectivePerGroupSpinBox.setValue(
                int(self.ui.promo_table.item(index, 3).text()))

            diag.setModal(True)
            if diag.exec():
                for j, v in enumerate(diag.get_inputs()):
                    self.ui.promo_table.setItem(
                        index, j, QTableWidgetItem(str(v)))

            data = diag.get_inputs()
            # pprint(self.promos)
            self.promos[index] = {'Name': data[0], 'Number of Sections': data[1], 'Number of Groups': data[2],
                                  'Effective per Group': data[3]}
        else:
            QMessageBox.about(self, "Error", "Please select a row")

    def delete_promo(self):
        index = self.ui.promo_table.selectedIndexes()
        if index:
            index = index[0].row()  # cause single selection
            self.ui.promo_table.removeRow(index)
            self.promos.pop(index)
            self.modules.pop(index)
            self.module_assignments.pop(index)
            for ds in self.datashows:
                # updating indexes upon removal
                ds["allocated"] = [x if x < index else x - 1 for x in ds["allocated"] if x != index]

            self.load_datashow_data()

        else:
            QMessageBox.about(self, "Error", "Please select a row")

    def prof_input(self):
        diag = ProfInputDialog()
        diag.setModal(True)
        if diag.exec():
            name = diag.get_inputs()
            insert_row_index = self.ui.professor_table.rowCount()
            self.ui.professor_table.insertRow(insert_row_index)
            self.ui.professor_table.setItem(
                insert_row_index, 0, QTableWidgetItem(name))
            self.profs.append(name)
            # print(self.profs)

    def load_prof_data(self):
        self.ui.professor_table.setRowCount(len(self.profs))
        for i, prof in enumerate(self.profs):
            self.ui.professor_table.setItem(i, 0, QTableWidgetItem(prof))
            # print(prof)
            # self.ui.promo_table.setItem(i, j, QTableWidgetItem(str(v)))

    def edit_prof(self):
        index = self.ui.professor_table.selectedIndexes()
        if index:
            index = index[0].row()  # cause single selection
            diag = ProfInputDialog()

            diag.name.setText(self.ui.professor_table.item(index, 0).text())
            diag.setModal(True)
            if diag.exec():
                self.ui.professor_table.setItem(
                    index, 0, QTableWidgetItem(diag.get_inputs()))

            # pprint(self.promos)

            self.profs[index] = diag.get_inputs()
            # print(self.profs)
        else:
            QMessageBox.about(self, "Error", "Please select a row")

    def delete_prof(self):
        index = self.ui.professor_table.selectedIndexes()
        if index:
            index = index[0].row()  # cause single selection
            self.ui.professor_table.removeRow(index)
            self.profs.pop(index)
            for i, promo_canvas in enumerate(self.module_assignments):
                for j, module in enumerate(promo_canvas):
                    promo_canvas[j] = [assignment for assignment in promo_canvas[j] if assignment["prof_name"] != index]
                    for assignment in promo_canvas[j]:
                        if assignment["prof_name"] > index:
                            assignment["prof_name"] -= 1

            print(self.module_assignments)
        else:
            QMessageBox.about(self, "Error", "Please select a row")

    def load_room_data(self):
        self.ui.room_table.setRowCount(len(self.rooms))
        for i, room in enumerate(self.rooms):
            self.ui.room_table.setItem(i, 0, QTableWidgetItem(room["Name"]))
            self.ui.room_table.setItem(i, 1, QTableWidgetItem(str(room["Capacity"])))
            self.ui.room_table.setItem(i, 2, QTableWidgetItem(room_type_from_int(room["RoomType"])))

    def room_input(self):
        diag = RoomInputDialog()
        diag.setModal(True)
        if diag.exec():
            row = diag.get_inputs()
            insert_row_index = self.ui.room_table.rowCount()
            self.ui.room_table.insertRow(insert_row_index)
            for j, v in enumerate(row):
                self.ui.room_table.setItem(
                    insert_row_index, j, QTableWidgetItem(str(v)))
            self.rooms.append(
                {'Name': row[0], 'Capacity': row[1], 'RoomType': row[2]})

    def edit_room(self):
        index = self.ui.room_table.selectedIndexes()
        if index:
            index = index[0].row()  # cause single selection
            diag = RoomInputDialog()

            diag.name.setText(self.rooms[index]["Name"])
            diag.capacitySpinBox.setValue(self.rooms[index]["Capacity"])
            diag.typecomboBox.setCurrentIndex(self.rooms[index]["RoomType"] - 1)

            diag.setModal(True)
            if diag.exec():
                name, cap, room_int = diag.get_inputs()
                self.ui.room_table.setItem(index, 0, QTableWidgetItem(name))
                self.ui.room_table.setItem(index, 1, QTableWidgetItem(str(cap)))
                self.ui.room_table.setItem(index, 2, QTableWidgetItem(room_type_from_int(room_int)))

            data = diag.get_inputs()
            # pprint(self.promos)
            self.rooms[index] = {'Name': data[0], 'Capacity': data[1], 'RoomType': data[2]}
        else:
            QMessageBox.about(self, "Error", "Please select a row")

    def delete_room(self):
        index = self.ui.room_table.selectedIndexes()
        if index:
            index = index[0].row()  # cause single selection
            self.ui.room_table.removeRow(index)
            self.rooms.pop(index)
        else:
            QMessageBox.about(self, "Error", "Please select a row to delete")

    def module_input(self):
        diag = ModuleInputDialog()
        diag.setModal(True)
        if diag.exec():
            row = diag.get_inputs()
            insert_row_index = self.ui.modules_table.rowCount()
            self.ui.modules_table.insertRow(insert_row_index)
            for j, v in enumerate(row):
                self.ui.modules_table.setItem(
                    insert_row_index, j, QTableWidgetItem(str(v)))
            promo_index = self.ui.pick_promo__modules_comboBox.currentIndex()
            self.modules[promo_index].append(
                {"Name": row[0], "abriv": row[1], "nb_cour": row[2], "nb_td": row[3], "nb_tp": row[4]})
            self.module_assignments[promo_index].append([])

    def edit_module(self):
        index = self.ui.modules_table.selectedIndexes()
        if index:
            index = index[0].row()  # cause single selection
            diag = ModuleInputDialog()

            diag.name.setText(self.ui.modules_table.item(index, 0).text())
            diag.abriv.setText(self.ui.modules_table.item(index, 1).text())
            diag.numberOfLecturesSpinBox.setValue(
                int(self.ui.modules_table.item(index, 2).text()))
            diag.numberOfTDsSpinBox.setValue(
                int(self.ui.modules_table.item(index, 3).text()))
            diag.numberOfTPsSpinBox.setValue(
                int(self.ui.modules_table.item(index, 4).text()))

            diag.setModal(True)
            if diag.exec():
                for j, v in enumerate(diag.get_inputs()):
                    self.ui.modules_table.setItem(
                        index, j, QTableWidgetItem(str(v)))

            data = diag.get_inputs()
            promo_index = self.ui.pick_promo__modules_comboBox.currentIndex()

            self.modules[promo_index][index] = {"Name": data[0], "abriv": data[1], "nb_cour": data[2], "nb_td": data[3],
                                                "nb_tp": data[4]}
        else:
            QMessageBox.about(self, "Error", "Please select a row")

    def delete_module(self):
        index = self.ui.modules_table.selectedIndexes()
        if index:
            index = index[0].row()  # cause single selection
            self.ui.modules_table.removeRow(index)
            promo_index = self.ui.pick_promo__modules_comboBox.currentIndex()
            self.modules[promo_index].pop(index)
            self.module_assignments[promo_index].pop(index)
        else:
            QMessageBox.about(self, "Error", "Please select a row")

    def load_module_data(self):
        if self.promos:
            promo_index = self.ui.pick_promo__modules_comboBox.currentIndex()
            # print(promo_index)
            self.ui.modules_table.setRowCount(len(self.modules[promo_index]))
            for i, module in enumerate(self.modules[promo_index]):
                for j, v in enumerate(module.values()):
                    self.ui.modules_table.setItem(i, j, QTableWidgetItem(str(v)))
                    # print(i,j,str(v))

    def on_spec_tab_change(self, i):
        # for modules we need promos
        if i == 3:
            if len(self.promos) == 0:
                self.ui.modules_tab.setEnabled(False)
                self.ui.modules_table.setRowCount(0)
                self.ui.pick_promo__modules_comboBox.clear()
                QMessageBox.information(
                    self, "", "in order to assign modules to promos u must first have promos")
            else:
                self.ui.pick_promo__modules_comboBox.clear()
                for promo in self.promos:
                    self.ui.pick_promo__modules_comboBox.addItem(promo["Name"])
                self.ui.modules_tab.setEnabled(True)
        elif i == 4:
            if len(self.promos) == 0 or any(len(modules) == 0 for modules in self.modules) or len(self.profs) == 0:
                self.ui.assignements_tab.setEnabled(False)
                self.ui.modules_assign_table.setRowCount(0)
                self.ui.assign_pick_promo_assign_comboBox.clear()

                QMessageBox.information(self, "", "in order to assign modules to promos and modules u must first have"
                                                  " promos and each promo must have at least one module")
            else:
                self.ui.assign_pick_promo_assign_comboBox.clear()
                self.ui.module_picker_comboBox.clear()
                for promo in self.promos:
                    self.ui.assign_pick_promo_assign_comboBox.addItem(promo["Name"])
                self.refresh_modules_combo()
                self.ui.assignements_tab.setEnabled(True)
        elif i == 5:
            if len(self.promos) == 0:
                self.ui.datashows_tab.setEnabled(False)
                self.ui.datashows_table.setRowCount(0)
                QMessageBox.information(self, "", "in order to add data shows to promos  u must first have at least one"
                                                  " promo")
            else:
                self.ui.datashows_tab.setEnabled(True)

    def on_ribbon_tab_change(self, i):
        if i == self.ui.ribbon.indexOf(self.ui.timetable_tab):
            there_is_promos = len(self.promos) != 0
            there_is_profs = len(self.profs) != 0
            there_is_rooms = len(self.rooms) != 0
            there_is_modules_for_each_promo = [len(modules_of_a_promo) != 0 for modules_of_a_promo in self.modules]
            there_is_assignments_for_each_module_for_each_promo = [len(assignment) != 0
                                                                   for promo_assignments in self.module_assignments
                                                                   for assignment in promo_assignments]
            conditions_to_generate = [
                there_is_promos,
                there_is_profs,
                there_is_rooms,
                *there_is_modules_for_each_promo,
                *there_is_assignments_for_each_module_for_each_promo
            ]
            if all(conditions_to_generate):
                self.ui.timetable_tab.setEnabled(True)
                self.ui.pick_promo_comboBox_TT.clear()
                self.ui.pick_promo_comboBox_TT.addItems([promo["Name"] for promo in self.promos])
                self.refresh_section_combo()
                self.update_faculty_data()

            else:
                # print(conditions_to_generate)
                self.ui.timetable_tab.setEnabled(False)
                msg_str = ""
                if not there_is_promos:
                    msg_str += "there are no promos\n"
                if not there_is_profs:
                    msg_str += "there are no profs\n"
                if not there_is_rooms:
                    msg_str += "there are no rooms\n"
                if not all(there_is_modules_for_each_promo):
                    msg_str += "some or all of the promos are missing modules\n"
                if not all(there_is_assignments_for_each_module_for_each_promo):
                    for i in range(len(self.module_assignments)):
                        for j in range(len(self.module_assignments[i])):
                            if len(self.module_assignments[i][j]) == 0:
                                msg_str += "the module called " + self.modules[i][j][
                                    "Name"] + " is missinng assigned profs\n"
                QMessageBox.information(self, "", msg_str)
        elif i == 4:
            print("debug message")
        self.ui.timetable_tableview.clearContents()

    def update_faculty_data(self):
        print("updated here")
        resources.timeslots_per_day = self.number_of_slots_per_day_input
        resources.days_per_week = self.number_of_days_per_week_input

        promo, room, ds ,professors = self.build_data_model()
        # TODO sort earlier probably fixes it
        self.faculty.list_promo = promo
        #self.faculty.list_promo.sort(key= lambda a: a.effective,reverse=True)
        self.faculty.list_rooms = room
        self.faculty.list_datashows = ds
        # TODO MAKE EDIT FLAG HERE
        self.problem_emploi_du_temp = PET(self.faculty)
        # print(sum(len(session_list) for session_list in problem_emploi_du_temp.sessions_list))
        self.problem_emploi_du_temp.list_of_profs = professors
        if self.professor_availability_constraint_checked:
            self.problem_emploi_du_temp.add_hard_constraint(ProfessorAvailability())
        if self.student_availability_constraint_checked:
            self.problem_emploi_du_temp.add_hard_constraint(StudentAvailability())
        if self.room_availability_constraint_checked:
            self.problem_emploi_du_temp.add_hard_constraint(RoomAvailability())
        if self.three_consecutive_sessions_constraint_checked:
            self.problem_emploi_du_temp.add_hard_constraint(ThreeConsecutiveMaxSessions())
        if self.two_cour_per_day_max_constraint_checked:
            self.problem_emploi_du_temp.add_hard_constraint(TwoCourPerDayMax())
        if self.unique_session_daily_constraint_checked:
            self.problem_emploi_du_temp.add_hard_constraint(UniqueSessionDaily())
        if self.cours_first_constraint_checked:
            self.problem_emploi_du_temp.add_soft_constraint(CoursFirst())
        if self.min_prof_days_constraint_checked:
            self.problem_emploi_du_temp.add_soft_constraint(MinProfDays(self.problem_emploi_du_temp.section_list))

    def generate_timetable(self):
        # for prof in self.profs:
        #     sum=0
        #     index =self.profs.index(prof)
        #     for promo in self.module_assignments:
        #         for module in promo:
        #             for assignment in module:
        #                 if assignment["prof_name"]==index:
        #                     sum+=assignment["number"]
        #     print(index,prof,sum)
        try:
            # for section in self.problem_emploi_du_temp.section_list:

            # section.required_sessions.sort(key= lambda x:x[3].value)
            # print(section.required_sessions)
            if self.problem_emploi_du_temp.solve():
                days = sum(1 if not all(day) else 0 for prof in self.problem_emploi_du_temp.list_of_profs for day in prof.available )
                print(days)
                self.load_timetable_data()
            else:
                print("messed up somewhere")
        except Exception as e:
            QMessageBox.about(self, "Error", str(e))

    def refresh_section_combo(self):
        promo_index = self.ui.pick_promo_comboBox_TT.currentIndex()
        sections_range = range(1, self.promos[promo_index]["Number of Sections"] + 1)
        self.ui.pick_section_comboBox.clear()
        self.ui.pick_section_comboBox.addItems([str(section_index) for section_index in sections_range])
        self.ui.pick_section_comboBox.setCurrentIndex(0)

    def assign_input(self):

        diag = AssignModuleInputDialog(self.profs)
        diag.setModal(True)
        if diag.exec():
            row = diag.get_inputs()
            insert_row_index = self.ui.modules_assign_table.rowCount()
            self.ui.modules_assign_table.insertRow(insert_row_index)

            self.ui.modules_assign_table.setItem(insert_row_index, 0, QTableWidgetItem(self.profs[row[0]]))
            self.ui.modules_assign_table.setItem(insert_row_index, 1, QTableWidgetItem(str(row[1])))
            self.ui.modules_assign_table.setItem(insert_row_index, 2, QTableWidgetItem(session_type_from_int(row[2])))
            promo_index = self.ui.assign_pick_promo_assign_comboBox.currentIndex()
            module_index = self.ui.module_picker_comboBox.currentIndex()
            self.module_assignments[promo_index][module_index].append(
                {"prof_name": row[0], "number": row[1], "type": row[2]})

    def refresh_modules_combo(self):
        promo_index = self.ui.assign_pick_promo_assign_comboBox.currentIndex()
        self.ui.module_picker_comboBox.clear()
        for module in self.modules[promo_index]:
            self.ui.module_picker_comboBox.addItem(module["Name"])

    def load_assign_data(self):
        promo_index = self.ui.assign_pick_promo_assign_comboBox.currentIndex()
        module_index = self.ui.module_picker_comboBox.currentIndex()
        # print(promo_index)
        if self.module_assignments:
            self.ui.modules_assign_table.setRowCount(len(self.module_assignments[promo_index][module_index]))
            for i, task in enumerate(self.module_assignments[promo_index][module_index]):
                self.ui.modules_assign_table.setItem(i, 0, QTableWidgetItem(self.profs[task['prof_name']]))
                self.ui.modules_assign_table.setItem(i, 1, QTableWidgetItem(str(task['number'])))
                session_type = session_type_from_int(task["type"])
                self.ui.modules_assign_table.setItem(i, 2, QTableWidgetItem(session_type))

    def edit_assign_data(self):
        index = self.ui.modules_assign_table.selectedIndexes()
        promo_index = self.ui.assign_pick_promo_assign_comboBox.currentIndex()
        module_index = self.ui.module_picker_comboBox.currentIndex()
        if index:
            self._extracted_from_edit_assign_data_6(promo_index, module_index, index)
        else:
            QMessageBox.about(self, "Error", "Please select a row")

    def _extracted_from_edit_assign_data_6(self, promo_index, module_index, index):
        index = index[0].row()  # cause single selection
        diag = AssignModuleInputDialog(self.profs)
        name, val, session_type = self.module_assignments[promo_index][module_index][index].values()
        session_type -= 1

        diag.SelectProfComboBox.setCurrentIndex(name)
        diag.CardinalitySpinBox.setValue(val)
        diag.type_sessionComboBox.setCurrentIndex(session_type)
        diag.setModal(True)
        if diag.exec():
            row = diag.get_inputs()
            self.ui.modules_assign_table.setItem(index, 0, QTableWidgetItem(self.profs[row[0]]))
            self.ui.modules_assign_table.setItem(index, 1, QTableWidgetItem(str(row[1])))
            self.ui.modules_assign_table.setItem(index, 2, QTableWidgetItem(session_type_from_int(row[2])))
            self.module_assignments[promo_index][module_index][index] = {"prof_name": row[0], "number": row[1],
                                                                         "type": row[2]}

    def delete_assign_data(self):
        index = self.ui.modules_assign_table.selectedIndexes()
        if index:
            index = index[0].row()  # cause single selection
            promo_index = self.ui.assign_pick_promo_assign_comboBox.currentIndex()
            module_index = self.ui.module_picker_comboBox.currentIndex()
            self.ui.modules_assign_table.removeRow(index)
            self.module_assignments[promo_index][module_index].pop(index)
        else:
            QMessageBox.about(self, "Error", "Please select a row")

    def datashow_input(self):
        diag = DataShowInputDialog(self.promos)
        diag.setModal(True)
        if diag.exec():
            name, allocations = diag.get_inputs()
            # print(name,allocations)
            str_allocations = [self.promos[i]["Name"] for i in allocations]
            insert_row_index = self.ui.datashows_table.rowCount()
            self.ui.datashows_table.insertRow(insert_row_index)
            self.ui.datashows_table.setItem(insert_row_index, 0, QTableWidgetItem(name))
            self.ui.datashows_table.setItem(insert_row_index, 1, QTableWidgetItem(",".join(str_allocations)))
            self.datashows.append({"id": name, "allocated": allocations})

    def load_datashow_data(self):
        self.ui.datashows_table.setRowCount(len(self.datashows))
        for i, ds in enumerate(self.datashows):
            name, allocations = ds.values()
            allocations = [self.promos[i]["Name"] for i in allocations]
            self.ui.datashows_table.setItem(i, 0, QTableWidgetItem(name))
            self.ui.datashows_table.setItem(i, 1, QTableWidgetItem(",".join(allocations)))

    def edit_datashow(self):
        index = self.ui.datashows_table.selectedIndexes()
        if index:
            index = index[0].row()  # cause single selection
            diag = DataShowInputDialog(self.promos)

            diag.id.setText(self.datashows[index]["id"])
            for i in self.datashows[index]["allocated"]:
                diag.promoCheckboxes[i].setEnabled(True)
            diag.setModal(True)
            if diag.exec():
                name, allocations = diag.get_inputs()
                str_allocations = [self.promos[i]["Name"] for i in allocations]
                self.ui.datashows_table.setItem(index, 0, QTableWidgetItem(name))
                self.ui.datashows_table.setItem(index, 1, QTableWidgetItem(",".join(str_allocations)))
                self.datashows[index] = {"id": name, "allocated": allocations}
                # print(self.datashows,index)
        else:
            QMessageBox.about(self, "Error", "Please select a row")

    def generate_days_slots(self):
        days_str = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        start = datetime.datetime(100, 1, 1, 8, 30, 0)
        starting_index = self.ui.starting_day_comboBox.currentIndex()
        slot_duration = self.ui.slot_duration_spinBox.value()
        slots_len = self.ui.slots_perday_spinBox.value()

        result_days = [days_str[(i + starting_index) % len(days_str)] for i in range(len(days_str))]
        result_slots = []
        for _ in range(1, slots_len + 1):
            end = start + datetime.timedelta(minutes=slot_duration)
            result_slots.append(start.strftime('%H:%M') + " - " + end.strftime('%H:%M'))
            start = end
        return result_days, result_slots

    def update_options(self):
        # this should be done asynchronously for each option but i'm lazy
        self.number_of_days_per_week_input = self.ui.days_per_week_spinBox.value()
        self.number_of_slots_per_day_input = self.ui.slots_perday_spinBox.value()
        self.ui.timetable_tableview.setRowCount(self.number_of_days_per_week_input)
        self.ui.timetable_tableview.setColumnCount(self.number_of_slots_per_day_input)
        self.ui.timetable_tableview.setHorizontalHeaderLabels([])
        self.slot_duration_input = self.ui.slot_duration_spinBox.value()
        self.starting_day_input = self.ui.starting_day_comboBox.currentIndex()
        self.professor_availability_constraint_checked = self.ui.professoravailability_checkBox.isChecked()
        self.student_availability_constraint_checked = self.ui.studentavailability_checkBox.isChecked()

        self.room_availability_constraint_checked = self.ui.roomavailability_checkBox.isChecked()
        self.three_consecutive_sessions_constraint_checked = self.ui.threeconsecutivemaxsessions_checkBox.isChecked()
        self.two_cour_per_day_max_constraint_checked = self.ui.twocourderdaymax_checkBox.isChecked()
        self.unique_session_daily_constraint_checked = self.ui.uniquesessiondaily_checkBox.isChecked()
        self.cours_first_constraint_checked = self.ui.CoursFirst.isChecked()
        self.min_prof_days_constraint_checked = self.ui.MinProfDays.isChecked()

    def delete_datashow(self):
        index = self.ui.datashows_table.selectedIndexes()
        if index:
            index = index[0].row()  # cause single selection
            self.ui.datashows_table.removeRow(index)
            self.datashows.pop(index)

    def timetable_input(self, mi):
        row = mi.row()
        column = mi.column()
        # print(row, column)
        promo_index = self.ui.pick_promo_comboBox_TT.currentIndex()
        section_index = self.ui.pick_section_comboBox.currentIndex()
        diag = SessionSetterInputDialog(self.problem_emploi_du_temp, self.faculty, promo_index, section_index, row,
                                        column)
        diag.setModal(True)
        if diag.exec():
            self.load_timetable_data()
            # # print(name,allocations)
            # str_allocations = [self.promos[i]["Name"] for i in allocations]
            # insert_row_index = self.ui.datashows_table.rowCount()
            # self.ui.datashows_table.insertRow(insert_row_index)
            # self.ui.datashows_table.setItem(insert_row_index, 0, QTableWidgetItem(name))
            # self.ui.datashows_table.setItem(insert_row_index, 1, QTableWidgetItem(",".join(str_allocations)))
            # self.datashows.append({"id": name, "allocated": allocations})

    def build_data_model(self):
        # making all the promo objects
        promo_list = [Promotion(p["Name"]) for p in self.promos]
        # adding sections to each of the promos
        for i, promo in enumerate(promo_list):
            promo.list_section = [Section(i + 1) for i in range(self.promos[i]["Number of Sections"])]
        # giving each section an close to even split of groups
        for promo_index, promo in enumerate(promo_list):
            number_of_sections = self.promos[promo_index]["Number of Sections"]
            Number_of_Groups = self.promos[promo_index]["Number of Groups"]
            group_effective = self.promos[promo_index]["Effective per Group"]

            groups_in_promo = [Group(i + 1, group_effective) for i in range(Number_of_Groups)]
            # fancy ceiling function nothing to see here
            groups_per_section = Number_of_Groups // number_of_sections + bool(Number_of_Groups % number_of_sections)
            for i in range(0, Number_of_Groups, groups_per_section):
                valid_index = i // groups_per_section
                promo.list_section[valid_index].add_groups(groups_in_promo[i:i + groups_per_section])

        # making a list of modules and making a list of assignments
        list_canvases = []
        professors = [Professor(prof_name) for prof_name in self.profs]
        for promo_index, promo_canvas in enumerate(self.modules):
            canvas = [Module(*module.values()) for module in promo_canvas]
            list_canvases.append(canvas)
            promo_list[promo_index].canvas = canvas
            for module_index, module in enumerate(canvas):
                self.generate_cour_sessions(canvas, module_index, promo_index, promo_list,professors)
                self.generate_td_sessions(canvas, module_index, promo_index, promo_list,professors)
                self.generate_tp_sessions(canvas, module_index, promo_index, promo_list,professors)
        # making a list of all the rooms
        rooms_list = [Room(room["Name"], room["RoomType"], room["Capacity"]) for room in self.rooms]
        # making a list of all the data-shows
        data_shows_list = [DataShow([promo_list[i] for ds in self.datashows for i in ds["allocated"]])]
        # finally return it all
        return promo_list, rooms_list, data_shows_list,professors

    def generate_tp_sessions(self, canvas, module_index, promo_index, promo_list,professors):
        assignments = self.module_assignments[promo_index][module_index]
        tp_assign = [assignment for assignment in assignments if assignment["type"] == SessionType.Tp.value]
        profs = []
        sessions_per_week = 0
        for assignment in tp_assign:
            sections_taught = assignment["number"]
            sessions_per_week = canvas[module_index].nb_tp
            profs.extend([professors[assignment["prof_name"]] for _ in range(sections_taught * sessions_per_week)])
        for sect in promo_list[promo_index].list_section:
            for group in sect.list_group:
                sect.add_required_sessions(
                    [(profs.pop(0), group, canvas[module_index], SessionType.Tp) for _ in
                     range(sessions_per_week)])
        assert len(profs) == 0

    def generate_td_sessions(self, canvas, module_index, promo_index, promo_list,professors):
        assignments = self.module_assignments[promo_index][module_index]
        td_assign = [assignment for assignment in assignments if assignment["type"] == SessionType.Td.value]
        profs = []
        sessions_per_week = 0
        for assignment in td_assign:
            sections_taught = assignment["number"]
            sessions_per_week = canvas[module_index].nb_td
            profs.extend([professors[assignment["prof_name"]] for _ in range(sections_taught * sessions_per_week)])
        for sect in promo_list[promo_index].list_section:
            for group in sect.list_group:
                sect.add_required_sessions(
                    [(profs.pop(0), group, canvas[module_index], SessionType.Td) for _ in
                     range(sessions_per_week)])
        assert len(profs) == 0

    def generate_cour_sessions(self, canvas, module_index, promo_index, promo_list,professors):
        assignments = self.module_assignments[promo_index][module_index]
        cour_assign = [assignment for assignment in assignments if assignment["type"] == SessionType.Cour.value]

        profs = []
        sessions_per_week = 0
        for assignment in cour_assign:
            sections_taught = assignment["number"]
            sessions_per_week = canvas[module_index].nb_cour
            profs.extend([professors[assignment["prof_name"]] for _ in range(sections_taught * sessions_per_week)])
        for sect in promo_list[promo_index].list_section:
            sect.add_required_sessions([(profs.pop(0), sect, canvas[module_index], SessionType.Cour) for _ in
                                        range(sessions_per_week)])
        assert len(profs) == 0

    def load_timetable_data(self):
        # self.ui.timetable_tableview.clear()
        promo_index = self.ui.pick_promo_comboBox_TT.currentIndex()
        section_index = self.ui.pick_section_comboBox.currentIndex()
        section_index = 0 if section_index < 0 else section_index
        # print(promo_index, section_index)
        font = QFont()
        font.setPointSize(8)
        self.ui.timetable_tableview.setRowCount(self.number_of_days_per_week_input)
        self.ui.timetable_tableview.setColumnCount(self.number_of_slots_per_day_input)
        vertical_headers, horizontal_headers = self.generate_days_slots()
        self.ui.timetable_tableview.setVerticalHeaderLabels(vertical_headers)
        self.ui.timetable_tableview.setHorizontalHeaderLabels(horizontal_headers)
        self.ui.timetable_tableview.horizontalHeader().setFont(font)
        self.ui.timetable_tableview.verticalHeader().setFont(font)
        font.setPointSize(7)
        if self.faculty.list_promo and self.problem_emploi_du_temp:
            timetable_index = sum(promo.nb_section for promo in self.faculty.list_promo[0:promo_index]) + section_index
            timetable_needed = self.problem_emploi_du_temp.section_list[timetable_index].EDT
            for i, day in enumerate(timetable_needed):
                for j, slot in enumerate(day):
                    slot.sessions.sort(key=lambda s: s.attendance.number)
                    if slot.sessions and slot.sessions[0].session_type == SessionType.Cour:
                        font.setBold(True)
                    else:
                        font.setBold(False)
                    cell_str = "\n".join(str(session) for session in slot.sessions)
                    item = QTableWidgetItem(cell_str)
                    item.setFont(font)
                    self.ui.timetable_tableview.setItem(i, j, item)

    def export_excel_file(self):
        save_path = QFileDialog.getSaveFileUrl(self, "Save Timetables", 'c:\\', "excel file (*.xlsx)")
        print(save_path[0].toLocalFile())
        if save_path[0].toLocalFile():
            main.excel_export(self.faculty.list_promo, save_path[0].toLocalFile(), example=r"../../test/result.xlsx")
            main.excel_prof_export(self.problem_emploi_du_temp.section_list, self.profs, save_path[0].toLocalFile())
            main.excel_room_availability_export(self.problem_emploi_du_temp.list_of_rooms, save_path[0].toLocalFile())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    os.chdir("Gui_files")

    window = MainWindow()
    window.bind()
    window.show()

    sys.exit(app.exec())

    # TODO OPTIONAL FEATURE custom sessions adding after TT generation
    # TODO OPTIONAL FEATURE generate professor TT in excel export
    # TODO OPTIONAL FEATURE add Professor soft unavailable times for preference
