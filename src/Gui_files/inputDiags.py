from PySide2.QtWidgets import *


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

    def getInputs(self):
        return self.name.text(), self.numberOfSectionsSpinBox.value(), self.numberOfGroupsSpinBox.value(),\
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

    def getInputs(self):
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

    def getInputs(self):
        return self.name.text(), self.capacitySpinBox.value(), self.typecomboBox.currentIndex()


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

    def getInputs(self):
        return self.name.text(), self.abriv.text(), self.numberOfLecturesSpinBox.value(), \
               self.numberOfTDsSpinBox.value(), self.numberOfTPsSpinBox.value()
