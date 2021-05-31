from PySide6.QtCore import QSortFilterProxyModel, Qt
from PySide6.QtWidgets import *


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

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Input")
        self.resize(524,380)
        self.verticalLayout_2 = QVBoxLayout(self)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tableWidget = QTableWidget(self)
        if self.tableWidget.columnCount() < 5:
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)

        self.verticalLayout_2.addWidget(self.tableWidget)

        self.frame = QFrame(self)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout.addWidget(self.pushButton_3)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout.addWidget(self.pushButton_2)

        self.buttonBox = QDialogButtonBox(self.frame)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

        self.verticalLayout_2.addWidget(self.frame)
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText("Module")
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText("Type")
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText("Attendance")
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText("Place")
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText("Professor")
        self.pushButton_3.setText("Add")
        self.pushButton.setText("Edit")
        self.pushButton_2.setText("Remove")
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
