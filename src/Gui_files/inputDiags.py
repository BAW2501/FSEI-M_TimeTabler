from PySide6.QtCore import QSortFilterProxyModel, Qt
from PySide6.QtWidgets import *

from src.resources import Session, Room, DataShow


class PromoInputDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Input")
        self.layout = QFormLayout(self)
        self.name = QLineEdit(self)
        self.numberOfSectionsSpinBox = QSpinBox()
        self.numberOfSectionsSpinBox.setValue(1)
        self.numberOfSectionsSpinBox.setMinimum(1)
        self.numberOfGroupsSpinBox = QSpinBox()
        self.numberOfSectionsSpinBox.setValue(1)
        self.numberOfGroupsSpinBox.setMinimum(self.numberOfSectionsSpinBox.value())
        self.effectivePerGroupSpinBox = QSpinBox()
        self.effectivePerGroupSpinBox.setValue(25)
        self.effectivePerGroupSpinBox.setMinimum(1)

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)

        self.layout.addRow("Promo name", self.name)
        self.layout.addRow("numberOfSections", self.numberOfSectionsSpinBox)
        self.layout.addRow("numberOfGroups", self.numberOfGroupsSpinBox)
        self.layout.addRow("effectivePerGroup", self.effectivePerGroupSpinBox)
        self.layout.addWidget(buttonBox)

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

    def get_inputs(self):
        return self.name.text(), self.numberOfSectionsSpinBox.value(), self.numberOfGroupsSpinBox.value(), \
               self.effectivePerGroupSpinBox.value()


class ProfInputDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Input")
        self.layout = QFormLayout(self)
        self.name = QLineEdit(self)

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)

        self.layout.addRow("Prof name", self.name)
        self.layout.addWidget(buttonBox)

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

    def get_inputs(self):
        return self.name.text()


class RoomInputDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Input")
        self.layout = QFormLayout(self)
        self.name = QLineEdit(self)
        self.capacitySpinBox = QSpinBox()
        self.capacitySpinBox.setValue(1)
        self.capacitySpinBox.setMinimum(1)
        self.capacitySpinBox.setMaximum(1000)
        self.typecomboBox = QComboBox(self)
        self.typecomboBox.addItem("Lecture")
        self.typecomboBox.addItem("TD")
        self.typecomboBox.addItem("TP")

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)

        self.layout.addRow("Room name", self.name)
        self.layout.addRow("Room capacity", self.capacitySpinBox)
        self.layout.addRow("Room Type ", self.typecomboBox)
        self.layout.addWidget(buttonBox)

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

    def get_inputs(self):
        return self.name.text(), self.capacitySpinBox.value(), self.typecomboBox.currentIndex() + 1


class ModuleInputDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Input")
        self.layout = QFormLayout(self)
        self.name = QLineEdit(self)
        self.numberOfLecturesSpinBox = QSpinBox()
        self.numberOfLecturesSpinBox.setValue(1)
        self.numberOfLecturesSpinBox.setMinimum(1)
        self.numberOfTDsSpinBox = QSpinBox()
        self.numberOfTDsSpinBox.setValue(1)
        self.numberOfTDsSpinBox.setMinimum(self.numberOfLecturesSpinBox.value())
        self.numberOfTPsSpinBox = QSpinBox()
        self.numberOfTPsSpinBox.setValue(1)
        self.numberOfTPsSpinBox.setMinimum(1)
        self.abriv = QLineEdit(self)

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)

        self.layout.addRow("Module name", self.name)
        self.layout.addRow("Module abriv", self.abriv)
        self.layout.addRow("number Of Lectures", self.numberOfLecturesSpinBox)
        self.layout.addRow("number Of TDs", self.numberOfTDsSpinBox)
        self.layout.addRow("number Of TPs", self.numberOfTPsSpinBox)
        self.layout.addWidget(buttonBox)

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

    def get_inputs(self):
        return self.name.text(), self.abriv.text(), self.numberOfLecturesSpinBox.value(), \
               self.numberOfTDsSpinBox.value(), self.numberOfTPsSpinBox.value()


class ExtendedComboBox(QComboBox):
    def __init__(self, parent=None):
        super(ExtendedComboBox, self).__init__(parent)

        self.setFocusPolicy(Qt.StrongFocus)
        self.setEditable(True)

        # add a filter model to filter matching items
        self.pFilterModel = QSortFilterProxyModel(self)
        self.pFilterModel.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.pFilterModel.setSourceModel(self.model())

        # add 3 completer, which uses the filter model
        self.completer = QCompleter(self.pFilterModel, self)
        # always show all (filtered) completions
        self.completer.setCompletionMode(QCompleter.UnfilteredPopupCompletion)
        self.setCompleter(self.completer)

        # connect signals
        # report this as a linting problem for pyside6
        self.lineEdit().textEdited.connect(self.pFilterModel.setFilterFixedString)
        self.completer.activated.connect(self.on_completer_activated)

    # on selection of an item from the completer, select the corresponding item from combobox
    def on_completer_activated(self, text):
        if text:
            index = self.findText(text)
            self.setCurrentIndex(index)
            self.activated.emit(self.itemText(index))

    # on model change, update the models of the filter and completer as well
    def setModel(self, model):
        super(ExtendedComboBox, self).setModel(model)
        self.pFilterModel.setSourceModel(model)
        self.completer.setModel(self.pFilterModel)

    # on model column change, update the model column of the filter and completer as well
    def setModelColumn(self, column):
        self.completer.setCompletionColumn(column)
        self.pFilterModel.setFilterKeyColumn(column)
        super(ExtendedComboBox, self).setModelColumn(column)


class AssignModuleInputDialog(QDialog):
    def __init__(self, profs, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Input")
        self.layout = QFormLayout(self)
        self.CardinalitySpinBox = QSpinBox()
        self.CardinalitySpinBox.setValue(1)
        self.CardinalitySpinBox.setMinimum(1)
        self.SelectProfComboBox = ExtendedComboBox(self)
        self.SelectProfComboBox.addItems(profs)
        self.type_sessionComboBox = QComboBox(self)
        self.type_sessionComboBox.addItem("Lecture")
        self.type_sessionComboBox.addItem("TD")
        self.type_sessionComboBox.addItem("TP")
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)

        self.layout.addRow("Prof ", self.SelectProfComboBox)
        self.layout.addRow("Number of Allocated Groups/sections", self.CardinalitySpinBox)
        self.layout.addRow("Type of assignment", self.type_sessionComboBox)
        self.layout.addWidget(buttonBox)

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

    def get_inputs(self):
        return self.SelectProfComboBox.currentIndex(), self.CardinalitySpinBox.value(), \
               self.type_sessionComboBox.currentIndex() + 1


class DataShowInputDialog(QDialog):

    def __init__(self, promos, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Input")
        self.layout = QFormLayout(self)
        self.id = QLineEdit(self)
        self.promoCheckboxes = []

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)

        self.layout.addRow("datashow ID", self.id)
        for promo in promos:
            current_box = QCheckBox(self)
            self.promoCheckboxes.append(current_box)
            self.layout.addRow(promo["Name"], current_box)

        self.layout.addWidget(buttonBox)

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        # self.promoCheckboxes[0].isChecked()

    def get_inputs(self):
        # print(self.id.text(), [checkbox.isChecked() for checkbox in self.promoCheckboxes])
        return self.id.text(), [i for i, checkbox in enumerate(self.promoCheckboxes) if checkbox.isChecked()]


class SessionSetterInputDialog(QDialog):

    def __init__(self, problem_emploi_du_temp, faculty, promo_index, section_index, day_index, slot_index, parent=None):
        super().__init__(parent)
        self.promo_index = promo_index
        self.section_index = section_index
        self.day_index = day_index
        self.slot_index = slot_index
        self.faculty = faculty
        from src.Solver import PET
        self.p_EDT: PET = problem_emploi_du_temp
        self.manually_added = []
        self.setWindowTitle("Input")
        self.resize(524, 380)
        self.verticalLayout_2 = QVBoxLayout(self)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.session_table = QTableWidget(self)
        self.session_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.session_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        if self.session_table.columnCount() < 5:
            self.session_table.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.session_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.session_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.session_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.session_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.session_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.session_table.setObjectName(u"tableWidget")
        self.session_table.setSelectionMode(QAbstractItemView.SingleSelection)

        self.verticalLayout_2.addWidget(self.session_table)

        self.frame = QFrame(self)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.add_pushButton = QPushButton(self.frame)
        self.add_pushButton.clicked.connect(self.add_session)

        self.add_pushButton.setObjectName(u"pushButton_3")

        self.verticalLayout.addWidget(self.add_pushButton)

        self.edit_pushButton = QPushButton(self.frame)
        self.edit_pushButton.setObjectName(u"pushButton")
        self.edit_pushButton.clicked.connect(self.change_room)
        self.verticalLayout.addWidget(self.edit_pushButton)

        self.remove_pushButton = QPushButton(self.frame)
        self.remove_pushButton.setObjectName(u"pushButton_2")
        self.remove_pushButton.clicked.connect(self.remove_assignment)

        self.verticalLayout.addWidget(self.remove_pushButton)

        self.buttonBox = QDialogButtonBox(self.frame)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

        self.verticalLayout_2.addWidget(self.frame)
        ___qtablewidgetitem = self.session_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText("Module")
        ___qtablewidgetitem1 = self.session_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText("Type")
        ___qtablewidgetitem2 = self.session_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText("Attendance")
        ___qtablewidgetitem3 = self.session_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText("Place")
        ___qtablewidgetitem4 = self.session_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText("Professor")
        self.add_pushButton.setText("Add")
        self.edit_pushButton.setText("Change Room")
        self.remove_pushButton.setText("Remove")
        self.session_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        sect_index = sum(promo.nb_section for promo in self.faculty.list_promo[0:self.promo_index]) + self.section_index
        slot_clicked = self.p_EDT.section_list[sect_index].EDT[self.day_index][self.slot_index]
        self.session_table.setRowCount(len(slot_clicked.sessions))
        if len(slot_clicked.sessions) == 0:
            self.edit_pushButton.setEnabled(False)
            self.remove_pushButton.setEnabled(False)
        self.load_session_data()
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

    def load_session_data(self):
        sect_index = sum(promo.nb_section for promo in self.faculty.list_promo[0:self.promo_index]) + self.section_index
        slot_clicked = self.p_EDT.section_list[sect_index].EDT[self.day_index][self.slot_index]
        self.session_table.setRowCount(len(slot_clicked.sessions))

        for i, session in enumerate(slot_clicked.sessions):
            self.session_table.setItem(i, 0, QTableWidgetItem(str(session.module)))
            self.session_table.setItem(i, 1, QTableWidgetItem(session_type_from_int(session.session_type.value)))
            self.session_table.setItem(i, 2, QTableWidgetItem(str(session.attendance)))
            self.session_table.setItem(i, 3, QTableWidgetItem(str(session.room)))
            self.session_table.setItem(i, 4, QTableWidgetItem(str(session.prof)))

    def add_session(self):

        sect_index = sum(promo.nb_section for promo in self.faculty.list_promo[0:self.promo_index]) + self.section_index
        # print(sect_index)
        diag = SessionAddDialog(self.p_EDT, self.promo_index, self.section_index, self.day_index, self.slot_index,
                                self.p_EDT.sessions_list[sect_index], sect_index)
        sessions = self.p_EDT.sessions_list[sect_index]
        yes_gotry = False
        for session in sessions:
            prof, attendance, module, session_type = session
            session_object = Session(attendance, prof, module, Room("temp", session_type.value, attendance.effective),
                                     session_type)
            if self.p_EDT.valid(session_object, self.day_index, self.slot_index):
                yes_gotry = True
                break

        diag.setModal(True)
        if yes_gotry and diag.exec():
            possible_session, room = diag.get_inputs()
            #print(room)
            prof, attendance, module, session_type = possible_session
            possible_session_object = Session(attendance, prof, module, room, session_type)
            assign(possible_session_object, DataShow([]), self.p_EDT.section_list[sect_index], self.day_index,
                   self.slot_index)
            self.load_session_data()

    def remove_assignment(self):
        index = self.session_table.selectedIndexes()
        sect_index = sum(promo.nb_section for promo in self.faculty.list_promo[0:self.promo_index]) + self.section_index
        if index:
            index = index[0].row()  # cause single selection
            print(self.p_EDT.section_list[sect_index].EDT[self.day_index][self.slot_index].sessions[index])
            session_to_remove = self.p_EDT.section_list[sect_index].EDT[self.day_index][self.slot_index].sessions[index]
            unassign(index, session_to_remove, DataShow([]), session_to_remove.attendance, self.day_index,
                     self.slot_index)
            self.p_EDT.section_list[sect_index].required_sessions.append((session_to_remove.prof,
                                                                          self.p_EDT.section_list[sect_index],
                                                                          session_to_remove.module,
                                                                          session_to_remove.session_type))
            self.session_table.removeRow(index)

    def change_room(self):
        index = self.session_table.selectedIndexes()
        if index:
            index = index[0].row()  # cause single selection
            current_session_index = index
            # print(index)
            diag = RoomPickerInput()
            real_sect_index = sum(
                promo.nb_section for promo in self.faculty.list_promo[0:self.promo_index]) + self.section_index
            current_session = self.p_EDT.section_list[real_sect_index].EDT[self.day_index][self.slot_index].sessions[
                current_session_index]
            temp = []
            for room in self.get_rooms(current_session.session_type, current_session.attendance):
                temp.append(room)
                diag.room_name.addItem(str(room))

            diag.setModal(True)
            if diag.exec():
                room_index = diag.get_inputs()
                current_session.room.set_available_on(self.day_index, self.slot_index)
                current_session.room = temp[room_index]
                current_session.room.set_busy_on(self.day_index, self.slot_index)
                self.session_table.setItem(current_session_index, 3, QTableWidgetItem(str(current_session.room)))

        else:
            QMessageBox.about(self, "Error", "Please select a row")

    def get_rooms(self, session_type, attendance):
        effective = attendance.effective
        appropriate_type = []
        from src.resources import SessionType
        from src.resources import RoomType

        if session_type.value == SessionType.Tp.value:
            appropriate_type.append(RoomType.tp.value)
        else:
            appropriate_type.append(RoomType.td.value)
        if session_type.value == SessionType.Cour.value:
            appropriate_type.append(RoomType.amphi.value)
        appropriate_rooms = [room for room in self.p_EDT.list_of_rooms if room.capacity >= effective and
                             room.type_salle in appropriate_type and room.is_available_on(self.day_index,
                                                                                          self.slot_index)]

        if appropriate_rooms:
            return appropriate_rooms
        else:
            QMessageBox.about(self, "Error", "no available rooms for this session at this time slot")


class SessionAddDialog(QDialog):

    def __init__(self, problem_emploi_du_temp, promo_index, section_index, day_index, slot_index, sessions,
                 real_sect_index,
                 parent=None):
        super().__init__(parent)
        self.real_sect_index = real_sect_index
        self.promo_index = promo_index
        self.section_index = section_index
        self.day_index = day_index
        self.slot_index = slot_index
        from src.Solver import PET
        self.sessions = sessions
        self.p_EDT: PET = problem_emploi_du_temp
        self.setWindowTitle("Add")
        self.layout = QFormLayout(self)
        self.temp = []
        self.temp2 = []
        self.SessionSelectComboBox = ExtendedComboBox(self)
        self.SessionSelectComboBox.blockSignals(True)
        for session in sessions:
            prof, attendance, module, session_type = session
            session_object = Session(attendance, prof, module, Room("temp", session_type, attendance.effective),
                                     session_type)
            if self.p_EDT.valid(session_object, self.day_index, self.slot_index):
                self.SessionSelectComboBox.addItem(str(session))
                self.temp.append(str(session))

        self.rooms_ComboBox = ExtendedComboBox(self)
        self.SessionSelectComboBox.blockSignals(False)
        self.SessionSelectComboBox.currentIndexChanged.connect(self.refresh_rooms)
        self.refresh_rooms()
        # self.

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)

        self.layout.addRow("session ", self.SessionSelectComboBox)
        self.layout.addRow("room", self.rooms_ComboBox)
        self.layout.addWidget(buttonBox)

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

    def refresh_rooms(self):

        current_session_index = self.SessionSelectComboBox.currentIndex()
        if current_session_index != -1:
            self.rooms_ComboBox.clear()
            current_session = self.sessions[current_session_index]
            self.temp2= [room for room in self.get_rooms(current_session[3], current_session[1])]
            self.rooms_ComboBox.addItems([str(room) for room in self.temp2])
        else:
            QMessageBox.about(self, "Error", "no sessions remainning for this slot ")

    def get_inputs(self):
        str_index = self.SessionSelectComboBox.currentIndex()

        for i, session in enumerate(self.p_EDT.sessions_list[self.real_sect_index]):
            # print(self.real_sect_index,str_index)
            # print(str(session), self.temp[str_index])
            if str(session) == self.temp[str_index]:
                return self.p_EDT.sessions_list[self.real_sect_index].pop(i), \
                       self.temp2[self.rooms_ComboBox.currentIndex()]

    def get_rooms(self, session_type, attendance):
        effective = attendance.effective
        appropriate_type = []
        from src.resources import SessionType
        from src.resources import RoomType

        if session_type.value == SessionType.Tp.value:
            appropriate_type.append(RoomType.tp.value)
        else:
            appropriate_type.append(RoomType.td.value)
        if session_type.value == SessionType.Cour.value:
            appropriate_type.append(RoomType.amphi.value)
        appropriate_rooms = [room for room in self.p_EDT.list_of_rooms if room.capacity >= effective and
                             room.type_salle in appropriate_type]

        if appropriate_rooms:
            return [room for room in appropriate_rooms if room.is_available_on(self.day_index, self.slot_index)]
        else:
            QMessageBox.about(self, "Error", "no available rooms for this session at this time slot")


class RoomPickerInput(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("RoomPicker")
        self.layout = QFormLayout(self)
        self.room_name = ExtendedComboBox(self)

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)

        self.layout.addRow("Room name", self.room_name)
        self.layout.addWidget(buttonBox)

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

    def get_inputs(self):
        return self.room_name.currentIndex()


def session_type_from_int(task):
    if task == 1:
        return "Lecture"
    elif task == 2:
        return "TD"
    else:
        return "TP"


def assign(possible_session, equipment, section, day, slot):
    equipment.set_busy_on(day, slot)
    section.EDT[day][slot].add_session(possible_session)
    possible_session.prof.set_busy_on(day, slot)
    possible_session.room.set_busy_on(day, slot)
    possible_session.attendance.set_busy_on(day, slot)
    from src.resources import SessionType
    if possible_session.session_type == SessionType.Cour:
        section.EDT[day][slot].is_full = True
    max_session = section.nb_group // 2 + 1 if section.nb_group > 4 else section.nb_group
    if len(section.EDT[day][slot].sessions) == max_session:
        section.EDT[day][slot].is_full = True
    # pprint(section.EDT)


def unassign(index, possible_session, equipment, section, day, slot):
    equipment.set_available_on(day, slot)
    section.EDT[day][slot].sessions.pop(index)
    possible_session.prof.set_available_on(day, slot)
    possible_session.room.set_available_on(day, slot)
    possible_session.attendance.set_available_on(day, slot)
    section.EDT[day][slot].is_full = False
