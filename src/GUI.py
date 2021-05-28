# -*- coding: utf-8 -*-
import os
import sys

from Gui_files.inputDiags import *
from Gui_files.ui_window import *


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

        self.load_promo_data()
        self.load_prof_data()
        self.load_room_data()
        self.load_module_data()
        self.load_assign_data()
        self.load_datashow_data()
        self.ui.spec_ribbon.currentChanged.connect(self.on_spec_tab_change)

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
            # print(self.profs)
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
            if len(self.promos) == 0 or len(self.modules) == 0:
                self.ui.assignements_tab.setEnabled(False)
                self.ui.modules_assign_table.setRowCount(0)
                self.ui.assign_pick_promo_assign_comboBox.clear()

                QMessageBox.information(self, "",
                                        "in order to assign modules to promos and modules u must first have promos")
            else:
                self.ui.assign_pick_promo_assign_comboBox.clear()
                self.ui.module_picker_comboBox.clear()
                for promo in self.promos:
                    self.ui.assign_pick_promo_assign_comboBox.addItem(promo["Name"])
                self.refresh_modules_combo()
                self.ui.assignements_tab.setEnabled(True)

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
                #print(self.datashows,index)
        else:
            QMessageBox.about(self, "Error", "Please select a row")

    def delete_datashow(self):
        index = self.ui.datashows_table.selectedIndexes()
        if index:
            index = index[0].row()  # cause single selection
            self.ui.datashows_table.removeRow(index)
            self.datashows.pop(index)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    os.chdir("Gui_files")

    window = MainWindow()
    window.bind()
    window.show()

    sys.exit(app.exec())
