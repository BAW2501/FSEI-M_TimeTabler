# -*- coding: utf-8 -*-
import os
import sys

from Gui_files.inputDiags import *
from Gui_files.ui_window import *
from resources import *


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
        self.promos = [
            {"Name": "MI", "Number of Sections": 2, "Number of Groups": 14, "Effective per Group": 25},
            {"Name": "L2 Info", "Number of Sections": 1, "Number of Groups": 9, "Effective per Group": 25},
            {"Name": "L3 Info", "Number of Sections": 1, "Number of Groups": 7, "Effective per Group": 25}]

        self.profs = ["Abid M.", "Bahnes N.", "Benameur", "Benhamed", "Benidris F.Z", "Bensalloua", "Bentaouza C",
                      "Besnassi", "Bessaoud K.", "Betouati", "Bouzebiba", "Delali A.", "Djahafi", "Djebbara R.",
                      "Filali F.", "Habib Zahmani", "Hamami", "Hassaine", "Henni F", "Henni K.", "Hocine N.",
                      "Kaid Slimane", "Kenniche A.", "Khelifa N.", "Khiat", "Labdelli", "Laredj A.", "M. Andasmas M",
                      "M. Belarbi Lakehal", "M. Belhamiti Omar", "M. Benchehida", "M. Benyatou Kamel", "M. Benzidane",
                      "M. Fettouch Houari", "M. Ghezzar Med", "M. Kaid", "M. Kaid Med", "M. Medeghri Ahmed",
                      "M. Menad Abdallah", "M. Mohammedi Mustapha", "M. Ould Ali M", "M.Ould Ali", "Maghni Sandid Z.",
                      "Mechaoui M.D.G", "Mekemmeche", "Menad", "Meroufel B.", "Midoun M.", "Miroud",
                      "Mlle Ali Merina.H", "Mlle Amina Ferraoun", "Mlle Benaouad", "Mlle Bouzid",
                      "Mlle Dj. Bensikaddour", "Mlle Ferraoun A.", "Mlle Hamou Maamar.M", "Mlle Lakeb Ouda",
                      "Mlle Zelmat Souhila", "Mme Ablaoui", "Mme Belmouhoub-Ould Ali", "Mme Bendahmane Hafida",
                      "Mme Bendehmane H", "Mme Bouabdelli", "Mme Diala.H", "Mme Kaisserli", "Mme Limam", "Mme Saidani",
                      "Mme Tabharit", "Moumen M.", "Moussa M.", "Mr Bouzit H", "Sehaba K.", ]
        self.rooms = [{"Name": "amphi1", "Capacity": 150, "RoomType": 1},
                      {"Name": "amphi4", "Capacity": 300, "RoomType": 1},
                      {"Name": "S1", "Capacity": 30, "RoomType": 2}
                      ]
        self.modules = [[{"Name": "Algorithmique et structure de données 1", "abriv": "ASD1", "nb_cour": 1, "nb_td": 1,
                          "nb_tp": 1}],
                        [{"Name": " Programmation orienté objet", "abriv": "POO", "nb_cour": 1, "nb_td": 0,
                          "nb_tp": 1}],
                        [{"Name": "Intelligence Artificielle", "abriv": "IA", "nb_cour": 1, "nb_td": 0, "nb_tp": 1}]]
        self.module_assignments = [
            [[{"prof_name": 18, "number": 2, "type": 1}]],
            [[{"prof_name": 0, "number": 1, "type": 1}]],
            [[{"prof_name": 11, "number": 1, "type": 1}]]
        ]
        self.datashows = [{"id": "ds1", "allocated": [0, 1]}]
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
        self.faculty = Faculty("FSEI-MOSTA")

    def bind(self):

        self.ui.promo_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.professor_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.room_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.modules_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.modules_assign_table.horizontalHeader(
        ).setSectionResizeMode(QHeaderView.Stretch)
        self.ui.datashows_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.timetable_tableview.horizontalHeader(
        ).setSectionResizeMode(QHeaderView.Stretch)
        self.ui.timetable_tableview.verticalHeader(
        ).setSectionResizeMode(QHeaderView.Stretch)
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

        self.load_promo_data()
        self.load_prof_data()
        self.load_room_data()
        self.load_module_data()
        self.load_assign_data()
        self.load_datashow_data()
        self.ui.spec_ribbon.currentChanged.connect(self.on_spec_tab_change)
        self.ui.ribbon.currentChanged.connect(self.on_ribbon_tab_change)
        # self.ui.verticalLayout_15.removeWidget(self.ui.timetable_tableview)
        # self.ui.verticalLayout_15.addWidget(self.ui.timetable_tableview)

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
            for j, v in enumerate(promo.values()):
                self.ui.promo_table.setItem(i, j, QTableWidgetItem(str(v)))

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
                    promo_canvas[j] = [assign for assign in promo_canvas[j] if assign["prof_name"] != index]
                    for assign in promo_canvas[j]:
                        if assign["prof_name"] > index:
                            assign["prof_name"] -= 1

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

            diag.name.setText(self.ui.room_table.item(index, 0).text())
            diag.capacitySpinBox.setValue(int(self.ui.room_table.item(index, 1).text()))
            diag.typecomboBox.setCurrentIndex(int(self.ui.room_table.item(index, 2).text()))

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
            there_is_assignments_for_each_module_for_each_promo = [len(assign) != 0
                                                                   for promo_assignments in self.module_assignments
                                                                   for assign in promo_assignments]
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
                for promo in self.promos:
                    self.ui.pick_promo_comboBox_TT.addItem(promo["Name"])
                self.refresh_section_combo()

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
                    msg_str += "some or all modules are missing prof assignments\n"

                QMessageBox.information(self, "", msg_str)
        elif i == 4:
            QMessageBox.information(self, "", "statistics incoming")

    def refresh_section_combo(self):
        promo_index = self.ui.pick_promo_comboBox_TT.currentIndex()
        sections_range = range(1, self.promos[promo_index]["Number of Sections"] + 1)
        self.ui.pick_section_comboBox.clear()
        self.ui.pick_section_comboBox.addItems([str(section_index) for section_index in sections_range])

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

    def update_options(self):
        # this should be done asynchronously for each option but i'm lazy
        self.number_of_days_per_week_input = self.ui.days_per_week_spinBox.value()
        self.number_of_slots_per_day_input = self.ui.slots_perday_spinBox.value()
        self.slot_duration_input = self.ui.slot_duration_spinBox.value()
        self.starting_day_input = self.ui.starting_day_comboBox.currentIndex()
        self.professor_availability_constraint_checked = self.ui.professoravailability_checkBox.isChecked()
        self.student_availability_constraint_checked = self.ui.studentavailability_checkBox.isChecked()

        self.room_availability_constraint_checked = self.ui.roomavailability_checkBox.isChecked()
        self.three_consecutive_sessions_constraint_checked = self.ui.threeconsecutivemaxsessions_checkBox.isChecked()
        self.two_cour_per_day_max_constraint_checked = self.ui.twocourderdaymax_checkBox.isChecked()
        self.unique_session_daily_constraint_checked = self.ui.uniquesessiondaily_checkBox.isChecked()

    def delete_datashow(self):
        index = self.ui.datashows_table.selectedIndexes()
        if index:
            index = index[0].row()  # cause single selection
            self.ui.datashows_table.removeRow(index)
            self.datashows.pop(index)

    def timetable_input(self, mi):
        row = mi.row()
        column = mi.column()
        print(row, column)

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
                promo.list_section[i].list_group = groups_in_promo[i:i + groups_per_section]

        # making a list of modules and making a list of assignments
        list_canvases = []
        for promo_index, promo_canvas in enumerate(self.modules):
            canvas = [Module(*module.values()) for module in promo_canvas]
            list_canvases.append(canvas)
            for module_index, module in enumerate(canvas):
                self.generate_cour_sessions(canvas, module_index, promo_index, promo_list)
                self.generate_td_sessions(canvas, module_index, promo_index, promo_list)
                self.generate_tp_sessions(canvas, module_index, promo_index, promo_list)
        rooms_list = [(Room(*room.values())) for room in self.rooms if name,]

    def generate_tp_sessions(self, canvas, module_index, promo_index, promo_list):
        assignments = self.module_assignments[promo_index][module_index]
        tp_assign = [assign for assign in assignments if assign["type"] == SessionType.Tp.value]
        profs = []
        sessions_per_week = 0
        for assignment in tp_assign:
            name = self.profs[assignment["prof_name"]]
            sections_taught = assignment["number"]
            sessions_per_week = canvas[module_index].nb_tp
            profs = [Professor(name) for _ in range(sections_taught * sessions_per_week)]
        for sect in promo_list[promo_index].list_section:
            for group in sect.list_group:
                sect.add_required_sessions(
                    [(profs.pop(0), group, canvas[module_index], SessionType.Tp) for _ in
                     range(sessions_per_week)])
        assert len(profs) == 0

    def generate_td_sessions(self, canvas, module_index, promo_index, promo_list):
        assignments = self.module_assignments[promo_index][module_index]
        td_assign = [assign for assign in assignments if assign["type"] == SessionType.Td.value]
        profs = []
        sessions_per_week = 0
        for assignment in td_assign:
            name = self.profs[assignment["prof_name"]]
            sections_taught = assignment["number"]
            sessions_per_week = canvas[module_index].nb_td
            profs = [Professor(name) for _ in range(sections_taught * sessions_per_week)]
        for sect in promo_list[promo_index].list_section:
            for group in sect.list_group:
                sect.add_required_sessions(
                    [(profs.pop(0), group, canvas[module_index], SessionType.Td) for _ in
                     range(sessions_per_week)])
        assert len(profs) == 0

    def generate_cour_sessions(self, canvas, module_index, promo_index, promo_list):
        assignments = self.module_assignments[promo_index][module_index]
        cour_assign = [assign for assign in assignments if assign["type"] == SessionType.Cour.value]

        profs = []
        sessions_per_week = 0
        for assignment in cour_assign:
            name = self.profs[assignment["prof_name"]]
            sections_taught = assignment["number"]
            sessions_per_week = canvas[module_index].nb_cour
            profs = [Professor(name) for _ in range(sections_taught * sessions_per_week)]
        for sect in promo_list[promo_index].list_section:
            sect.add_required_sessions([(profs.pop(0), sect, canvas[module_index], SessionType.Cour) for _ in
                                        range(sessions_per_week)])
        assert len(profs) == 0


if __name__ == "__main__":
    app = QApplication(sys.argv)
    os.chdir("Gui_files")

    window = MainWindow()
    window.bind()
    window.show()

    sys.exit(app.exec())
