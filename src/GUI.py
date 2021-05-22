# -*- coding: utf-8 -*-
import os
import sys

from Gui_files.inputDiags import *
from Gui_files.ui_window import *


class MainWindow(QMainWindow):
    def __init__(self):

        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.promos = [
            {"Name": "MI", "Number of Sections": 2, "Number of Groups": 14, "Effective per Group": 25},
            {"Name": "L2I", "Number of Sections": 1, "Number of Groups": 9, "Effective per Group": 25},
            {"Name": "L3I", "Number of Sections": 1, "Number of Groups": 7, "Effective per Group": 25}]

        self.profs = ["miroud", "bessaoud", "henni"]
        self.rooms = [{"Name": "amphi1", "Capacity": 150, "RoomType": 1},
                      {"Name": "amphi4", "Capacity": 300, "RoomType": 1},
                      {"Name": "S1", "Capacity": 30, "RoomType": 2}

                      ]

    def bind(self):

        self.ui.promo_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.professor_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.room_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.modules_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.modules_assign_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.datashows_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.timetable_tableview.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.timetable_tableview.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.ui.promo_add_pushbutton.clicked.connect(self.promo_input)
        self.ui.promo_edit__pushbutton.clicked.connect(self.edit_promo)
        self.ui.promo_remove_pushbutton.clicked.connect(self.delete_promo)
        self.ui.prof_add_pushbutton.clicked.connect(self.prof_input)
        self.ui.prof_edit_pushbutton.clicked.connect(self.edit_prof)
        self.ui.prof_remove_pushbutton.clicked.connect(self.delete_prof)
        self.ui.room_add_pushbutton.clicked.connect(self.room_input)
        self.ui.room_edit_pushbutton.clicked.connect(self.edit_room)
        self.ui.room_remove_pushbutton.clicked.connect(self.delete_room)


        self.load_promo_data()
        self.load_prof_data()
        self.load_room_data()

    def promo_input(self):
        diag = PromoInputDialog()
        diag.setModal(True)
        if diag.exec():
            row = diag.getInputs()
            insert_row_index = self.ui.promo_table.rowCount()
            self.ui.promo_table.insertRow(insert_row_index)
            for j, v in enumerate(row):
                self.ui.promo_table.setItem(insert_row_index, j, QTableWidgetItem(str(v)))
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
            diag.numberOfSectionsSpinBox.setValue(int(self.ui.promo_table.item(index, 1).text()))
            diag.numberOfGroupsSpinBox.setValue(int(self.ui.promo_table.item(index, 2).text()))
            diag.effectivePerGroupSpinBox.setValue(int(self.ui.promo_table.item(index, 3).text()))

            diag.setModal(True)
            if diag.exec():
                for j, v in enumerate(diag.getInputs()):
                    self.ui.promo_table.setItem(index, j, QTableWidgetItem(str(v)))

            data = diag.getInputs()
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
        else:
            QMessageBox.about(self, "Error", "Please select a row")

    def prof_input(self):
        diag = ProfInputDialog()
        diag.setModal(True)
        if diag.exec():
            name = diag.getInputs()
            insert_row_index = self.ui.professor_table.rowCount()
            self.ui.professor_table.insertRow(insert_row_index)
            self.ui.professor_table.setItem(insert_row_index, 0, QTableWidgetItem(name))
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
                self.ui.professor_table.setItem(index, 0, QTableWidgetItem(diag.getInputs()))

            # pprint(self.promos)

            self.profs[index] = diag.getInputs()
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
            for j, v in enumerate(room.values()):
                self.ui.room_table.setItem(i, j, QTableWidgetItem(str(v)))

    def room_input(self):
        diag = RoomInputDialog()
        diag.setModal(True)
        if diag.exec():
            row = diag.getInputs()
            insert_row_index = self.ui.room_table.rowCount()
            self.ui.room_table.insertRow(insert_row_index)
            for j, v in enumerate(row):
                self.ui.room_table.setItem(insert_row_index, j, QTableWidgetItem(str(v)))
            self.rooms.append({'Name': row[0], 'Capacity': row[1], 'RoomType': row[2]})

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
                for j, v in enumerate(diag.getInputs()):
                    self.ui.room_table.setItem(index, j, QTableWidgetItem(str(v)))

            data = diag.getInputs()
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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    os.chdir("Gui_files")

    window = MainWindow()
    window.bind()
    window.show()

    sys.exit(app.exec_())
