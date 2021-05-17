# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'windowwlxiHB.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        os.chdir('./Gui_files')
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(944, 600)
        icon = QIcon()
        icon.addFile(u"icons/logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"/*\n"
"Aqua Style Sheet for QT Applications\n"
"Author: Jaime A. Quiroga P.\n"
"Company: GTRONICK\n"
"Last updated: 22/01/2019, 07:55.\n"
"Available at: https://github.com/GTRONICK/QSS/blob/master/Aqua.qss\n"
"*/\n"
"QMainWindow {\n"
"	background-color:#ececec;\n"
"}\n"
"QTextEdit {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QPlainTextEdit {\n"
"	border-width: 1px;\n"
"	border-style: solid;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QToolButton {\n"
"	border-style: solid;\n"
"	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"	border-left"
                        "-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"	color: rgb(0,0,0);\n"
"	padding: 2px;\n"
"	background-color: rgb(255,255,255);\n"
"}\n"
"QToolButton:hover{\n"
"	border-style: solid;\n"
"	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(195, 195, 195), stop:1 rgb(222, 222, 222));\n"
"	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(197, 197, 197), stop:1 rgb(227, 227, 227));\n"
"	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(197, 197, 197));\n"
"	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(195, 195, 195), stop:1 rgb(222, 222, 222));\n"
"	border-width: 1px;\n"
"	border-rad"
                        "ius: 5px;\n"
"	color: rgb(0,0,0);\n"
"	padding: 2px;\n"
"	background-color: rgb(255,255,255);\n"
"}\n"
"QToolButton:pressed{\n"
"	border-style: solid;\n"
"	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"	color: rgb(0,0,0);\n"
"	padding: 2px;\n"
"	background-color: rgb(142,142,142);\n"
"}\n"
"QPushButton{\n"
"	border-style: solid;\n"
"	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-righ"
                        "t-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"	color: rgb(0,0,0);\n"
"	padding: 2px;\n"
"	background-color: rgb(255,255,255);\n"
"	text-align:bottom;\n"
"}\n"
"QPushButton::default{\n"
"	border-style: solid;\n"
"	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"	border-b"
                        "ottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"	color: rgb(0,0,0);\n"
"	padding: 2px;\n"
"	background-color: rgb(255,255,255);\n"
"}\n"
"QPushButton:hover{\n"
"	border-style: solid;\n"
"	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(195, 195, 195), stop:1 rgb(222, 222, 222));\n"
"	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(197, 197, 197), stop:1 rgb(227, 227, 227));\n"
"	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(197, 197, 197));\n"
"	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(195, 195, 195), stop:1 rgb(222, 222, 222));\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"	color: rgb(0,0,0);\n"
"	padding: 2px;\n"
"	background-color: rgb(255,255,255);\n"
"}\n"
"QPushButton:pressed{\n"
"	bo"
                        "rder-style: solid;\n"
"	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
"	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"	color: rgb(0,0,0);\n"
"	padding: 2px;\n"
"	background-color: rgb(142,142,142);\n"
"}\n"
"QPushButton:disabled{\n"
"	border-style: solid;\n"
"	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
""
                        "	border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
"	border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
"	border-width: 1px;\n"
"	border-radius: 5px;\n"
"	color: #808086;\n"
"	padding: 2px;\n"
"	background-color: rgb(142,142,142);\n"
"}\n"
"QLineEdit {\n"
"	border-width: 1px; border-radius: 4px;\n"
"	border-style: solid;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QLabel {\n"
"	color: #000000;\n"
"}\n"
"QLCDNumber {\n"
"	color: rgb(0, 113, 255, 255);\n"
"}\n"
"QProgressBar {\n"
"	text-align: center;\n"
"	color: rgb(240, 240, 240);\n"
"	border-width: 1px; \n"
"	border-radius: 10px;\n"
"	border-color: rgb(230, 230, 230);\n"
"	border-style: solid;\n"
"	background-color:rgb(207,207,207);\n"
"}\n"
"QProgressBar::chunk {\n"
"	background-color: qline"
                        "argradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));\n"
"	border-radius: 10px;\n"
"}\n"
"QMenuBar {\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(207, 209, 207, 255), stop:1 rgba(230, 229, 230, 255));\n"
"}\n"
"QMenuBar::item {\n"
"	color: #000000;\n"
"  	spacing: 3px;\n"
"  	padding: 1px 4px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(207, 209, 207, 255), stop:1 rgba(230, 229, 230, 255));\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"  	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"	color: #FFFFFF;\n"
"}\n"
"QMenu::item:selected {\n"
"	border-style: solid;\n"
"	border-top-color: transparent;\n"
"	border-right-color: transparent;\n"
"	border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252,"
                        " 255));\n"
"	border-bottom-color: transparent;\n"
"	border-left-width: 2px;\n"
"	color: #000000;\n"
"	padding-left:15px;\n"
"	padding-top:4px;\n"
"	padding-bottom:4px;\n"
"	padding-right:7px;\n"
"}\n"
"QMenu::item {\n"
"	border-style: solid;\n"
"	border-top-color: transparent;\n"
"	border-right-color: transparent;\n"
"	border-left-color: transparent;\n"
"	border-bottom-color: transparent;\n"
"	border-bottom-width: 1px;\n"
"	color: #000000;\n"
"	padding-left:17px;\n"
"	padding-top:4px;\n"
"	padding-bottom:4px;\n"
"	padding-right:7px;\n"
"}\n"
"QTabWidget {\n"
"	color:rgb(0,0,0);\n"
"	background-color:#000000;\n"
"}\n"
"QTabWidget::pane {\n"
"		border-color: rgb(223,223,223);\n"
"		background-color:rgb(226,226,226);\n"
"		border-style: solid;\n"
"		border-width: 2px;\n"
"    	border-radius: 6px;\n"
"}\n"
"QTabBar::tab:first {\n"
"	border-style: solid;\n"
"	border-left-width:1px;\n"
"	border-right-width:0px;\n"
"	border-top-width:1px;\n"
"	border-bottom-width:1px;\n"
"	border-top-color: rgb(209,209,209);\n"
"	bor"
                        "der-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"	border-bottom-color: rgb(229,229,229);\n"
"	border-top-left-radius: 4px;\n"
"	border-bottom-left-radius: 4px;\n"
"	color: #000000;\n"
"	padding: 3px;\n"
"	margin-left:0px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(247, 247, 247, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QTabBar::tab:last {\n"
"	border-style: solid;\n"
"	border-width:1px;\n"
"	border-top-color: rgb(209,209,209);\n"
"	border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"	border-right-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"	border-bottom-color: rgb(229,229,229);\n"
"	border-top-right-radius: 4px;\n"
"	border-bottom-right-radius: 4px;\n"
"	color: #000000;\n"
"	paddi"
                        "ng: 3px;\n"
"	margin-left:0px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(247, 247, 247, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QTabBar::tab {\n"
"	border-style: solid;\n"
"	border-top-width:1px;\n"
"	border-bottom-width:1px;\n"
"	border-left-width:1px;\n"
"	border-top-color: rgb(209,209,209);\n"
"	border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"	border-bottom-color: rgb(229,229,229);\n"
"	color: #000000;\n"
"	padding: 3px;\n"
"	margin-left:0px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(247, 247, 247, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:last:selected, QTabBar::tab:hover {\n"
"  	border-style: solid;\n"
"  	border-left-width:1px;\n"
"	border-right-color: transparent;\n"
"	border-top-color: rgb(209,209,209);\n"
"	border-left-color: qlineargradient(spread:pad, x"
                        "1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"	border-bottom-color: rgb(229,229,229);\n"
"	color: #FFFFFF;\n"
"	padding: 3px;\n"
"	margin-left:0px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:first:selected, QTabBar::tab:hover {\n"
"  	border-style: solid;\n"
"  	border-left-width:1px;\n"
"  	border-bottom-width:1px;\n"
"  	border-top-width:1px;\n"
"	border-right-color: transparent;\n"
"	border-top-color: rgb(209,209,209);\n"
"	border-left-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(209, 209, 209, 209), stop:1 rgba(229, 229, 229, 229));\n"
"	border-bottom-color: rgb(229,229,229);\n"
"	color: #FFFFFF;\n"
"	padding: 3px;\n"
"	margin-left:0px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
""
                        "}\n"
"\n"
"QCheckBox {\n"
"	color: #000000;\n"
"	padding: 2px;\n"
"}\n"
"QCheckBox:disabled {\n"
"	color: #808086;\n"
"	padding: 2px;\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"	border-radius:4px;\n"
"	border-style:solid;\n"
"	padding-left: 1px;\n"
"	padding-right: 1px;\n"
"	padding-bottom: 1px;\n"
"	padding-top: 1px;\n"
"	border-width:1px;\n"
"	border-color: transparent;\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"\n"
"	height: 10px;\n"
"	width: 10px;\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"	color: #000000;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"\n"
"	height: 10px;\n"
"	width: 10px;\n"
"	border-style:solid;\n"
"	border-width: 1px;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba("
                        "0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"	color: #000000;\n"
"}\n"
"QRadioButton {\n"
"	color: 000000;\n"
"	padding: 1px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"	height: 10px;\n"
"	width: 10px;\n"
"	border-style:solid;\n"
"	border-radius:5px;\n"
"	border-width: 1px;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"	color: #a9b7c6;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QRadioButton::indicator:!checked {\n"
"	height: 10px;\n"
"	width: 10px;\n"
"	border-style:solid;\n"
"	border-radius:5px;\n"
"	border-width: 1px;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"	color: #a9b7c6;\n"
"	background-color: transparent;\n"
"}\n"
"QStatusBar {\n"
"	color:#027f7f;\n"
"}\n"
"QSpinBox {\n"
"	border-styl"
                        "e: solid;\n"
"	border-width: 1px;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QDoubleSpinBox {\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QTimeEdit {\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QDateTimeEdit {\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));\n"
"}\n"
"QDateEdit {\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(0, 113, 255, 255), stop:1 rgba(91, 171, 252, 255));"
                        "\n"
"}\n"
"\n"
"QToolBox {\n"
"	color: #a9b7c6;\n"
"	background-color:#000000;\n"
"}\n"
"QToolBox::tab {\n"
"	color: #a9b7c6;\n"
"	background-color:#000000;\n"
"}\n"
"QToolBox::tab:selected {\n"
"	color: #FFFFFF;\n"
"	background-color:#000000;\n"
"}\n"
"QScrollArea {\n"
"	color: #FFFFFF;\n"
"	background-color:#000000;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"	height: 5px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));\n"
"}\n"
"QSlider::groove:vertical {\n"
"	width: 5px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));\n"
"}\n"
"QSlider::handle:horizontal {\n"
"	background: rgb(253,253,253);\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(207,207,207);\n"
"	width: 12px;\n"
"	margin: -5px 0;\n"
"	border-radius: 7px;\n"
"}\n"
"QSlider::handle:vertical {\n"
"	background: rgb(253,253,253);\n"
"	bord"
                        "er-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(207,207,207);\n"
"	height: 12px;\n"
"	margin: 0 -5px;\n"
"	border-radius: 7px;\n"
"}\n"
"QSlider::add-page:horizontal {\n"
"    background: rgb(181,181,181);\n"
"}\n"
"QSlider::add-page:vertical {\n"
"    background: rgb(181,181,181);\n"
"}\n"
"QSlider::sub-page:horizontal {\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));\n"
"}\n"
"QSlider::sub-page:vertical {\n"
"    background-color: qlineargradient(spread:pad, y1:0.5, x1:1, y2:0.5, x2:0, stop:0 rgba(49, 147, 250, 255), stop:1 rgba(34, 142, 255, 255));\n"
"}\n"
"QScrollBar:horizontal {\n"
"	max-height: 20px;\n"
"	border: 1px transparent grey;\n"
"	margin: 0px 20px 0px 20px;\n"
"}\n"
"QScrollBar:vertical {\n"
"	max-width: 20px;\n"
"	border: 1px transparent grey;\n"
"	margin: 20px 0px 20px 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"	background: rgb(253,253,253);\n"
"	border-style: solid;\n"
""
                        "	border-width: 1px;\n"
"	border-color: rgb(207,207,207);\n"
"	border-radius: 7px;\n"
"	min-width: 25px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"	background: rgb(253,253,253);\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(147, 200, 200);\n"
"	border-radius: 7px;\n"
"	min-width: 25px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"	background: rgb(253,253,253);\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(207,207,207);\n"
"	border-radius: 7px;\n"
"	min-height: 25px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"	background: rgb(253,253,253);\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(147, 200, 200);\n"
"	border-radius: 7px;\n"
"	min-height: 25px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"   border: 2px transparent grey;\n"
"   border-top-right-radius: 7px;\n"
"   border-bottom-right-radius: 7px;\n"
"   background: rgba(34, 142, 255, 255);\n"
"   width: 20px;\n"
"   subcontrol-position: right;\n"
"   subcontrol"
                        "-origin: margin;\n"
"}\n"
"QScrollBar::add-line:horizontal:pressed {\n"
"   border: 2px transparent grey;\n"
"   border-top-right-radius: 7px;\n"
"   border-bottom-right-radius: 7px;\n"
"   background: rgb(181,181,181);\n"
"   width: 20px;\n"
"   subcontrol-position: right;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical {\n"
"   border: 2px transparent grey;\n"
"   border-bottom-left-radius: 7px;\n"
"   border-bottom-right-radius: 7px;\n"
"   background: rgba(34, 142, 255, 255);\n"
"   height: 20px;\n"
"   subcontrol-position: bottom;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {\n"
"   border: 2px transparent grey;\n"
"   border-bottom-left-radius: 7px;\n"
"   border-bottom-right-radius: 7px;\n"
"   background: rgb(181,181,181);\n"
"   height: 20px;\n"
"   subcontrol-position: bottom;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 7px;\n"
"   borde"
                        "r-bottom-left-radius: 7px;\n"
"   background: rgba(34, 142, 255, 255);\n"
"   width: 20px;\n"
"   subcontrol-position: left;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal:pressed {\n"
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 7px;\n"
"   border-bottom-left-radius: 7px;\n"
"   background: rgb(181,181,181);\n"
"   width: 20px;\n"
"   subcontrol-position: left;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 7px;\n"
"   border-top-right-radius: 7px;\n"
"   background: rgba(34, 142, 255, 255);\n"
"   height: 20px;\n"
"   subcontrol-position: top;\n"
"   subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {\n"
"   border: 2px transparent grey;\n"
"   border-top-left-radius: 7px;\n"
"   border-top-right-radius: 7px;\n"
"   background: rgb(181,181,181);\n"
"   height: 20px;\n"
"   subcontrol-position: top;\n"
"   subcontrol-origin: margin;\n"
"}\n"
""
                        "QScrollBar::left-arrow:horizontal {\n"
"   border: 1px transparent grey;\n"
"   border-top-left-radius: 3px;\n"
"   border-bottom-left-radius: 3px;\n"
"   width: 6px;\n"
"   height: 6px;\n"
"   background: white;\n"
"}\n"
"QScrollBar::right-arrow:horizontal {\n"
"   border: 1px transparent grey;\n"
"   border-top-right-radius: 3px;\n"
"   border-bottom-right-radius: 3px;\n"
"   width: 6px;\n"
"   height: 6px;\n"
"   background: white;\n"
"}\n"
"QScrollBar::up-arrow:vertical {\n"
"   border: 1px transparent grey;\n"
"   border-top-left-radius: 3px;\n"
"   border-top-right-radius: 3px;\n"
"   width: 6px;\n"
"   height: 6px;\n"
"   background: white;\n"
"}\n"
"QScrollBar::down-arrow:vertical {\n"
"   border: 1px transparent grey;\n"
"   border-bottom-left-radius: 3px;\n"
"   border-bottom-right-radius: 3px;\n"
"   width: 6px;\n"
"   height: 6px;\n"
"   background: white;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"   background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, Q"
                        "ScrollBar::sub-page:vertical {\n"
"   background: none;\n"
"}")
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.ribbon = QTabWidget(self.frame)
        self.ribbon.setObjectName(u"ribbon")
        self.ribbon.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ribbon.sizePolicy().hasHeightForWidth())
        self.ribbon.setSizePolicy(sizePolicy)
        self.ribbon.setMinimumSize(QSize(0, 0))
        self.ribbon.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamily(u"Times New Roman")
        font.setPointSize(14)
        self.ribbon.setFont(font)
        self.ribbon.setTabletTracking(False)
        self.ribbon.setStyleSheet(u"")
        self.ribbon.setTabPosition(QTabWidget.North)
        self.ribbon.setTabShape(QTabWidget.Rounded)
        self.ribbon.setIconSize(QSize(32, 32))
        self.ribbon.setTabBarAutoHide(False)
        self.file_tab = QWidget()
        self.file_tab.setObjectName(u"file_tab")
        self.horizontalLayout_12 = QHBoxLayout(self.file_tab)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.new_project_frame = QFrame(self.file_tab)
        self.new_project_frame.setObjectName(u"new_project_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.new_project_frame.sizePolicy().hasHeightForWidth())
        self.new_project_frame.setSizePolicy(sizePolicy1)
        self.new_project_frame.setFrameShape(QFrame.StyledPanel)
        self.new_project_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.new_project_frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.new_project_pushButton = QPushButton(self.new_project_frame)
        self.new_project_pushButton.setObjectName(u"new_project_pushButton")
        self.new_project_pushButton.setContextMenuPolicy(Qt.NoContextMenu)
        self.new_project_pushButton.setLayoutDirection(Qt.LeftToRight)
        self.new_project_pushButton.setText(u"")
        icon1 = QIcon()
        icon1.addFile(u"icons/new file.png", QSize(), QIcon.Normal, QIcon.Off)
        self.new_project_pushButton.setIcon(icon1)
        self.new_project_pushButton.setIconSize(QSize(64, 64))

        self.verticalLayout.addWidget(self.new_project_pushButton)

        self.new_project_label = QLabel(self.new_project_frame)
        self.new_project_label.setObjectName(u"new_project_label")
        self.new_project_label.setLineWidth(0)
        self.new_project_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.new_project_label)


        self.horizontalLayout_12.addWidget(self.new_project_frame)

        self.open_project_frame = QFrame(self.file_tab)
        self.open_project_frame.setObjectName(u"open_project_frame")
        sizePolicy1.setHeightForWidth(self.open_project_frame.sizePolicy().hasHeightForWidth())
        self.open_project_frame.setSizePolicy(sizePolicy1)
        self.open_project_frame.setFrameShape(QFrame.StyledPanel)
        self.open_project_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.open_project_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.open_project_pushButton = QPushButton(self.open_project_frame)
        self.open_project_pushButton.setObjectName(u"open_project_pushButton")
        self.open_project_pushButton.setContextMenuPolicy(Qt.NoContextMenu)
        self.open_project_pushButton.setLayoutDirection(Qt.LeftToRight)
        self.open_project_pushButton.setText(u"")
        icon2 = QIcon()
        icon2.addFile(u"icons/open_file.png", QSize(), QIcon.Normal, QIcon.Off)
        self.open_project_pushButton.setIcon(icon2)
        self.open_project_pushButton.setIconSize(QSize(64, 64))

        self.verticalLayout_2.addWidget(self.open_project_pushButton)

        self.open_project_label = QLabel(self.open_project_frame)
        self.open_project_label.setObjectName(u"open_project_label")
        self.open_project_label.setLineWidth(0)
        self.open_project_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.open_project_label)


        self.horizontalLayout_12.addWidget(self.open_project_frame)

        self.save_project_frame = QFrame(self.file_tab)
        self.save_project_frame.setObjectName(u"save_project_frame")
        sizePolicy1.setHeightForWidth(self.save_project_frame.sizePolicy().hasHeightForWidth())
        self.save_project_frame.setSizePolicy(sizePolicy1)
        self.save_project_frame.setFrameShape(QFrame.StyledPanel)
        self.save_project_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.save_project_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.new_project_pushButton_2 = QPushButton(self.save_project_frame)
        self.new_project_pushButton_2.setObjectName(u"new_project_pushButton_2")
        self.new_project_pushButton_2.setContextMenuPolicy(Qt.NoContextMenu)
        self.new_project_pushButton_2.setLayoutDirection(Qt.LeftToRight)
        self.new_project_pushButton_2.setText(u"")
        icon3 = QIcon()
        icon3.addFile(u"icons/save_file.png", QSize(), QIcon.Normal, QIcon.Off)
        self.new_project_pushButton_2.setIcon(icon3)
        self.new_project_pushButton_2.setIconSize(QSize(64, 64))

        self.verticalLayout_3.addWidget(self.new_project_pushButton_2)

        self.new_project_label_2 = QLabel(self.save_project_frame)
        self.new_project_label_2.setObjectName(u"new_project_label_2")
        self.new_project_label_2.setLineWidth(0)
        self.new_project_label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.new_project_label_2)


        self.horizontalLayout_12.addWidget(self.save_project_frame)

        icon4 = QIcon()
        icon4.addFile(u"icons/homepage-icon-png-17.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.ribbon.addTab(self.file_tab, icon4, "")
        self.data_tab = QWidget()
        self.data_tab.setObjectName(u"data_tab")
        self.verticalLayout_4 = QVBoxLayout(self.data_tab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.spec_ribbon = QTabWidget(self.data_tab)
        self.spec_ribbon.setObjectName(u"spec_ribbon")
        sizePolicy.setHeightForWidth(self.spec_ribbon.sizePolicy().hasHeightForWidth())
        self.spec_ribbon.setSizePolicy(sizePolicy)
        self.spec_ribbon.setMinimumSize(QSize(0, 100))
        font1 = QFont()
        font1.setPointSize(12)
        self.spec_ribbon.setFont(font1)
        self.spec_ribbon.setIconSize(QSize(32, 32))
        self.promotions_tab = QWidget()
        self.promotions_tab.setObjectName(u"promotions_tab")
        self.verticalLayout_5 = QVBoxLayout(self.promotions_tab)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.promo_control_frame = QFrame(self.promotions_tab)
        self.promo_control_frame.setObjectName(u"promo_control_frame")
        self.promo_control_frame.setFrameShape(QFrame.StyledPanel)
        self.promo_control_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.promo_control_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.promo_add_pushbutton = QPushButton(self.promo_control_frame)
        self.promo_add_pushbutton.setObjectName(u"promo_add_pushbutton")

        self.horizontalLayout_5.addWidget(self.promo_add_pushbutton)

        self.promo_edit__pushbutton = QPushButton(self.promo_control_frame)
        self.promo_edit__pushbutton.setObjectName(u"promo_edit__pushbutton")

        self.horizontalLayout_5.addWidget(self.promo_edit__pushbutton)

        self.promo_remove_pushbutton = QPushButton(self.promo_control_frame)
        self.promo_remove_pushbutton.setObjectName(u"promo_remove_pushbutton")

        self.horizontalLayout_5.addWidget(self.promo_remove_pushbutton)


        self.verticalLayout_5.addWidget(self.promo_control_frame)

        self.promo_table = QTableWidget(self.promotions_tab)
        if (self.promo_table.columnCount() < 5):
            self.promo_table.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.promo_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.promo_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.promo_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.promo_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.promo_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.promo_table.setObjectName(u"promo_table")

        self.verticalLayout_5.addWidget(self.promo_table)

        self.spec_ribbon.addTab(self.promotions_tab, "")
        self.professors_tab = QWidget()
        self.professors_tab.setObjectName(u"professors_tab")
        self.horizontalLayout_4 = QHBoxLayout(self.professors_tab)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.professor_tablewidget = QTableWidget(self.professors_tab)
        if (self.professor_tablewidget.columnCount() < 2):
            self.professor_tablewidget.setColumnCount(2)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.professor_tablewidget.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.professor_tablewidget.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        self.professor_tablewidget.setObjectName(u"professor_tablewidget")
        self.professor_tablewidget.setColumnCount(2)

        self.horizontalLayout_4.addWidget(self.professor_tablewidget)

        self.Prof_control_frame = QFrame(self.professors_tab)
        self.Prof_control_frame.setObjectName(u"Prof_control_frame")
        self.Prof_control_frame.setFrameShape(QFrame.StyledPanel)
        self.Prof_control_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.Prof_control_frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.prof_add_pushbutton = QPushButton(self.Prof_control_frame)
        self.prof_add_pushbutton.setObjectName(u"prof_add_pushbutton")

        self.verticalLayout_6.addWidget(self.prof_add_pushbutton)

        self.prof_edit_pushbutton = QPushButton(self.Prof_control_frame)
        self.prof_edit_pushbutton.setObjectName(u"prof_edit_pushbutton")

        self.verticalLayout_6.addWidget(self.prof_edit_pushbutton)

        self.prof_remove_pushbutton = QPushButton(self.Prof_control_frame)
        self.prof_remove_pushbutton.setObjectName(u"prof_remove_pushbutton")

        self.verticalLayout_6.addWidget(self.prof_remove_pushbutton)


        self.horizontalLayout_4.addWidget(self.Prof_control_frame)

        self.spec_ribbon.addTab(self.professors_tab, "")
        self.facilities_tab = QWidget()
        self.facilities_tab.setObjectName(u"facilities_tab")
        self.horizontalLayout_3 = QHBoxLayout(self.facilities_tab)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.room_tablewidget = QTableWidget(self.facilities_tab)
        if (self.room_tablewidget.columnCount() < 4):
            self.room_tablewidget.setColumnCount(4)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.room_tablewidget.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.room_tablewidget.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.room_tablewidget.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.room_tablewidget.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        self.room_tablewidget.setObjectName(u"room_tablewidget")
        self.room_tablewidget.setColumnCount(4)

        self.horizontalLayout_3.addWidget(self.room_tablewidget)

        self.room_control_frame = QFrame(self.facilities_tab)
        self.room_control_frame.setObjectName(u"room_control_frame")
        self.room_control_frame.setFrameShape(QFrame.StyledPanel)
        self.room_control_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.room_control_frame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.room_add_pushbutton = QPushButton(self.room_control_frame)
        self.room_add_pushbutton.setObjectName(u"room_add_pushbutton")

        self.verticalLayout_7.addWidget(self.room_add_pushbutton)

        self.room_edit_pushbutton = QPushButton(self.room_control_frame)
        self.room_edit_pushbutton.setObjectName(u"room_edit_pushbutton")

        self.verticalLayout_7.addWidget(self.room_edit_pushbutton)

        self.room_remove_pushbutton = QPushButton(self.room_control_frame)
        self.room_remove_pushbutton.setObjectName(u"room_remove_pushbutton")

        self.verticalLayout_7.addWidget(self.room_remove_pushbutton)


        self.horizontalLayout_3.addWidget(self.room_control_frame)

        self.spec_ribbon.addTab(self.facilities_tab, "")
        self.modules_tab = QWidget()
        self.modules_tab.setObjectName(u"modules_tab")
        self.gridLayout = QGridLayout(self.modules_tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.module_control_frame = QFrame(self.modules_tab)
        self.module_control_frame.setObjectName(u"module_control_frame")
        self.module_control_frame.setFrameShape(QFrame.StyledPanel)
        self.module_control_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.module_control_frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.module_add_pushbutton = QPushButton(self.module_control_frame)
        self.module_add_pushbutton.setObjectName(u"module_add_pushbutton")

        self.horizontalLayout_6.addWidget(self.module_add_pushbutton)

        self.module_edit_pushbutton = QPushButton(self.module_control_frame)
        self.module_edit_pushbutton.setObjectName(u"module_edit_pushbutton")

        self.horizontalLayout_6.addWidget(self.module_edit_pushbutton)

        self.module_remove_pushbutton = QPushButton(self.module_control_frame)
        self.module_remove_pushbutton.setObjectName(u"module_remove_pushbutton")

        self.horizontalLayout_6.addWidget(self.module_remove_pushbutton)


        self.gridLayout.addWidget(self.module_control_frame, 1, 0, 1, 1)

        self.pick_promo_frame = QFrame(self.modules_tab)
        self.pick_promo_frame.setObjectName(u"pick_promo_frame")
        self.pick_promo_frame.setFrameShape(QFrame.StyledPanel)
        self.pick_promo_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.pick_promo_frame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pick_promo_label = QLabel(self.pick_promo_frame)
        self.pick_promo_label.setObjectName(u"pick_promo_label")

        self.horizontalLayout_7.addWidget(self.pick_promo_label)

        self.pick_promo_comboBox = QComboBox(self.pick_promo_frame)
        self.pick_promo_comboBox.setObjectName(u"pick_promo_comboBox")

        self.horizontalLayout_7.addWidget(self.pick_promo_comboBox)


        self.gridLayout.addWidget(self.pick_promo_frame, 0, 0, 1, 1)

        self.modules_tableWidget = QTableWidget(self.modules_tab)
        if (self.modules_tableWidget.columnCount() < 6):
            self.modules_tableWidget.setColumnCount(6)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.modules_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.modules_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.modules_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.modules_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.modules_tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.modules_tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem16)
        self.modules_tableWidget.setObjectName(u"modules_tableWidget")

        self.gridLayout.addWidget(self.modules_tableWidget, 2, 0, 1, 1)

        self.spec_ribbon.addTab(self.modules_tab, "")
        self.assignements_tab = QWidget()
        self.assignements_tab.setObjectName(u"assignements_tab")
        self.verticalLayout_8 = QVBoxLayout(self.assignements_tab)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.pick_promo_frame_2 = QFrame(self.assignements_tab)
        self.pick_promo_frame_2.setObjectName(u"pick_promo_frame_2")
        self.pick_promo_frame_2.setFrameShape(QFrame.StyledPanel)
        self.pick_promo_frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.pick_promo_frame_2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.pick_promo_label_2 = QLabel(self.pick_promo_frame_2)
        self.pick_promo_label_2.setObjectName(u"pick_promo_label_2")

        self.horizontalLayout_8.addWidget(self.pick_promo_label_2)

        self.pick_promo_comboBox_2 = QComboBox(self.pick_promo_frame_2)
        self.pick_promo_comboBox_2.setObjectName(u"pick_promo_comboBox_2")

        self.horizontalLayout_8.addWidget(self.pick_promo_comboBox_2)


        self.verticalLayout_8.addWidget(self.pick_promo_frame_2)

        self.modules_tableWidget_2 = QTableWidget(self.assignements_tab)
        if (self.modules_tableWidget_2.columnCount() < 4):
            self.modules_tableWidget_2.setColumnCount(4)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.modules_tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.modules_tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.modules_tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.modules_tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem20)
        self.modules_tableWidget_2.setObjectName(u"modules_tableWidget_2")

        self.verticalLayout_8.addWidget(self.modules_tableWidget_2)

        self.spec_ribbon.addTab(self.assignements_tab, "")
        self.datashows_tab = QWidget()
        self.datashows_tab.setObjectName(u"datashows_tab")
        self.verticalLayout_9 = QVBoxLayout(self.datashows_tab)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.datashows_control_frame_2 = QFrame(self.datashows_tab)
        self.datashows_control_frame_2.setObjectName(u"datashows_control_frame_2")
        self.datashows_control_frame_2.setFrameShape(QFrame.StyledPanel)
        self.datashows_control_frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.datashows_control_frame_2)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.datashow_add_pushbutton_2 = QPushButton(self.datashows_control_frame_2)
        self.datashow_add_pushbutton_2.setObjectName(u"datashow_add_pushbutton_2")

        self.horizontalLayout_9.addWidget(self.datashow_add_pushbutton_2)

        self.datashow_edit_pushbutton_2 = QPushButton(self.datashows_control_frame_2)
        self.datashow_edit_pushbutton_2.setObjectName(u"datashow_edit_pushbutton_2")

        self.horizontalLayout_9.addWidget(self.datashow_edit_pushbutton_2)

        self.datashow_remove_pushbutton_2 = QPushButton(self.datashows_control_frame_2)
        self.datashow_remove_pushbutton_2.setObjectName(u"datashow_remove_pushbutton_2")

        self.horizontalLayout_9.addWidget(self.datashow_remove_pushbutton_2)


        self.verticalLayout_9.addWidget(self.datashows_control_frame_2)

        self.tableWidget = QTableWidget(self.datashows_tab)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem23)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_9.addWidget(self.tableWidget)

        self.spec_ribbon.addTab(self.datashows_tab, "")

        self.verticalLayout_4.addWidget(self.spec_ribbon)

        icon5 = QIcon()
        icon5.addFile(u"icons/spec.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ribbon.addTab(self.data_tab, icon5, "")
        self.options_tab = QWidget()
        self.options_tab.setObjectName(u"options_tab")
        self.horizontalLayout_10 = QHBoxLayout(self.options_tab)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.timetable_options_frame = QFrame(self.options_tab)
        self.timetable_options_frame.setObjectName(u"timetable_options_frame")
        self.timetable_options_frame.setFrameShape(QFrame.StyledPanel)
        self.timetable_options_frame.setFrameShadow(QFrame.Raised)
        self.timetable_label = QLabel(self.timetable_options_frame)
        self.timetable_label.setObjectName(u"timetable_label")
        self.timetable_label.setGeometry(QRect(20, 25, 81, 21))
        font2 = QFont()
        font2.setFamily(u"Times New Roman")
        font2.setPointSize(12)
        self.timetable_label.setFont(font2)
        self.days_per_week_label = QLabel(self.timetable_options_frame)
        self.days_per_week_label.setObjectName(u"days_per_week_label")
        self.days_per_week_label.setGeometry(QRect(20, 60, 91, 16))
        self.slots_perday_label = QLabel(self.timetable_options_frame)
        self.slots_perday_label.setObjectName(u"slots_perday_label")
        self.slots_perday_label.setGeometry(QRect(20, 140, 101, 16))
        self.days_per_week_spinBox = QSpinBox(self.timetable_options_frame)
        self.days_per_week_spinBox.setObjectName(u"days_per_week_spinBox")
        self.days_per_week_spinBox.setGeometry(QRect(130, 60, 91, 22))
        self.days_per_week_spinBox.setAlignment(Qt.AlignCenter)
        self.slots_perday_spinBox = QSpinBox(self.timetable_options_frame)
        self.slots_perday_spinBox.setObjectName(u"slots_perday_spinBox")
        self.slots_perday_spinBox.setGeometry(QRect(130, 140, 91, 22))
        self.slots_perday_spinBox.setAlignment(Qt.AlignCenter)
        self.starting_day_label = QLabel(self.timetable_options_frame)
        self.starting_day_label.setObjectName(u"starting_day_label")
        self.starting_day_label.setGeometry(QRect(20, 100, 61, 16))
        self.starting_day_comboBox = QComboBox(self.timetable_options_frame)
        self.starting_day_comboBox.addItem("")
        self.starting_day_comboBox.addItem("")
        self.starting_day_comboBox.addItem("")
        self.starting_day_comboBox.addItem("")
        self.starting_day_comboBox.addItem("")
        self.starting_day_comboBox.addItem("")
        self.starting_day_comboBox.setObjectName(u"starting_day_comboBox")
        self.starting_day_comboBox.setGeometry(QRect(130, 100, 91, 22))
        self.starting_day_comboBox.setLayoutDirection(Qt.LeftToRight)
        self.slot_duration_label = QLabel(self.timetable_options_frame)
        self.slot_duration_label.setObjectName(u"slot_duration_label")
        self.slot_duration_label.setGeometry(QRect(20, 180, 81, 16))
        self.slot_duration_lineEdit = QLineEdit(self.timetable_options_frame)
        self.slot_duration_lineEdit.setObjectName(u"slot_duration_lineEdit")
        self.slot_duration_lineEdit.setGeometry(QRect(130, 180, 91, 20))
        self.slot_duration_lineEdit.setAlignment(Qt.AlignCenter)
        self.mins_label = QLabel(self.timetable_options_frame)
        self.mins_label.setObjectName(u"mins_label")
        self.mins_label.setGeometry(QRect(230, 180, 21, 16))

        self.horizontalLayout_10.addWidget(self.timetable_options_frame)

        self.Constraints = QFrame(self.options_tab)
        self.Constraints.setObjectName(u"Constraints")
        self.Constraints.setFrameShape(QFrame.StyledPanel)
        self.Constraints.setFrameShadow(QFrame.Raised)
        self.constraints_label = QLabel(self.Constraints)
        self.constraints_label.setObjectName(u"constraints_label")
        self.constraints_label.setGeometry(QRect(10, 10, 55, 16))
        sizePolicy1.setHeightForWidth(self.constraints_label.sizePolicy().hasHeightForWidth())
        self.constraints_label.setSizePolicy(sizePolicy1)
        self.studentavailability_checkBox = QCheckBox(self.Constraints)
        self.studentavailability_checkBox.setObjectName(u"studentavailability_checkBox")
        self.studentavailability_checkBox.setGeometry(QRect(10, 58, 111, 17))
        self.studentavailability_checkBox.setChecked(True)
        self.professoravailability_checkBox = QCheckBox(self.Constraints)
        self.professoravailability_checkBox.setObjectName(u"professoravailability_checkBox")
        self.professoravailability_checkBox.setGeometry(QRect(10, 35, 119, 17))
        self.professoravailability_checkBox.setChecked(True)
        self.professoravailability_checkBox.setTristate(False)
        self.roomavailability_checkBox = QCheckBox(self.Constraints)
        self.roomavailability_checkBox.setObjectName(u"roomavailability_checkBox")
        self.roomavailability_checkBox.setGeometry(QRect(10, 81, 100, 17))
        self.roomavailability_checkBox.setChecked(True)
        self.threeconsecutivemaxsessions_checkBox = QCheckBox(self.Constraints)
        self.threeconsecutivemaxsessions_checkBox.setObjectName(u"threeconsecutivemaxsessions_checkBox")
        self.threeconsecutivemaxsessions_checkBox.setGeometry(QRect(10, 104, 170, 17))
        self.twocourderdaymax_checkBox = QCheckBox(self.Constraints)
        self.twocourderdaymax_checkBox.setObjectName(u"twocourderdaymax_checkBox")
        self.twocourderdaymax_checkBox.setGeometry(QRect(10, 127, 120, 17))
        self.uniquesessiondaily_checkBox = QCheckBox(self.Constraints)
        self.uniquesessiondaily_checkBox.setObjectName(u"uniquesessiondaily_checkBox")
        self.uniquesessiondaily_checkBox.setGeometry(QRect(10, 150, 114, 17))

        self.horizontalLayout_10.addWidget(self.Constraints)

        icon6 = QIcon()
        icon6.addFile(u"icons/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ribbon.addTab(self.options_tab, icon6, "")
        self.timetable_tab = QWidget()
        self.timetable_tab.setObjectName(u"timetable_tab")
        self.timetable_tab.setEnabled(False)
        self.verticalLayout_15 = QVBoxLayout(self.timetable_tab)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.pick_promo_section = QFrame(self.timetable_tab)
        self.pick_promo_section.setObjectName(u"pick_promo_section")
        self.pick_promo_section.setFrameShape(QFrame.StyledPanel)
        self.pick_promo_section.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.pick_promo_section)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.pick_promo_label_3 = QLabel(self.pick_promo_section)
        self.pick_promo_label_3.setObjectName(u"pick_promo_label_3")

        self.horizontalLayout_11.addWidget(self.pick_promo_label_3)

        self.comboBox = QComboBox(self.pick_promo_section)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_11.addWidget(self.comboBox)

        self.label = QLabel(self.pick_promo_section)
        self.label.setObjectName(u"label")

        self.horizontalLayout_11.addWidget(self.label)

        self.pick_promo_comboBox_3 = QComboBox(self.pick_promo_section)
        self.pick_promo_comboBox_3.setObjectName(u"pick_promo_comboBox_3")

        self.horizontalLayout_11.addWidget(self.pick_promo_comboBox_3)


        self.verticalLayout_15.addWidget(self.pick_promo_section)

        self.timetable_tableview = QTableWidget(self.timetable_tab)
        if (self.timetable_tableview.columnCount() < 7):
            self.timetable_tableview.setColumnCount(7)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.timetable_tableview.setHorizontalHeaderItem(0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.timetable_tableview.setHorizontalHeaderItem(1, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.timetable_tableview.setHorizontalHeaderItem(2, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.timetable_tableview.setHorizontalHeaderItem(3, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.timetable_tableview.setHorizontalHeaderItem(4, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.timetable_tableview.setHorizontalHeaderItem(5, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.timetable_tableview.setHorizontalHeaderItem(6, __qtablewidgetitem30)
        if (self.timetable_tableview.rowCount() < 5):
            self.timetable_tableview.setRowCount(5)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.timetable_tableview.setVerticalHeaderItem(0, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.timetable_tableview.setVerticalHeaderItem(1, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.timetable_tableview.setVerticalHeaderItem(2, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.timetable_tableview.setVerticalHeaderItem(3, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.timetable_tableview.setVerticalHeaderItem(4, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        __qtablewidgetitem36.setTextAlignment(Qt.AlignCenter);
        self.timetable_tableview.setItem(0, 1, __qtablewidgetitem36)
        self.timetable_tableview.setObjectName(u"timetable_tableview")
        self.timetable_tableview.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.timetable_tableview.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.timetable_tableview.setGridStyle(Qt.DashLine)
        self.timetable_tableview.setSortingEnabled(False)
        self.timetable_tableview.setCornerButtonEnabled(False)
        self.timetable_tableview.horizontalHeader().setCascadingSectionResizes(True)
        self.timetable_tableview.horizontalHeader().setMinimumSectionSize(44)
        self.timetable_tableview.horizontalHeader().setDefaultSectionSize(104)
        self.timetable_tableview.horizontalHeader().setStretchLastSection(True)
        self.timetable_tableview.verticalHeader().setCascadingSectionResizes(True)
        self.timetable_tableview.verticalHeader().setDefaultSectionSize(77)
        self.timetable_tableview.verticalHeader().setStretchLastSection(True)

        self.verticalLayout_15.addWidget(self.timetable_tableview)

        icon7 = QIcon()
        icon7.addFile(u"icons/timetable.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ribbon.addTab(self.timetable_tab, icon7, "")
        self.help_tab = QWidget()
        self.help_tab.setObjectName(u"help_tab")
        self.horizontalLayout_13 = QHBoxLayout(self.help_tab)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.about_us_frame = QFrame(self.help_tab)
        self.about_us_frame.setObjectName(u"about_us_frame")
        self.about_us_frame.setFrameShape(QFrame.StyledPanel)
        self.about_us_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.about_us_frame)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.about_us_pushButton = QPushButton(self.about_us_frame)
        self.about_us_pushButton.setObjectName(u"about_us_pushButton")
        self.about_us_pushButton.setContextMenuPolicy(Qt.NoContextMenu)
        self.about_us_pushButton.setLayoutDirection(Qt.LeftToRight)
        self.about_us_pushButton.setText(u"")
        icon8 = QIcon()
        icon8.addFile(u"icons/about_us.png", QSize(), QIcon.Normal, QIcon.Off)
        self.about_us_pushButton.setIcon(icon8)
        self.about_us_pushButton.setIconSize(QSize(64, 64))

        self.verticalLayout_10.addWidget(self.about_us_pushButton)

        self.about_us_label = QLabel(self.about_us_frame)
        self.about_us_label.setObjectName(u"about_us_label")
        self.about_us_label.setLineWidth(0)
        self.about_us_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.about_us_label)


        self.horizontalLayout_13.addWidget(self.about_us_frame)

        self.technical_support_frame = QFrame(self.help_tab)
        self.technical_support_frame.setObjectName(u"technical_support_frame")
        self.technical_support_frame.setFrameShape(QFrame.StyledPanel)
        self.technical_support_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.technical_support_frame)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.technical_support_pushButton = QPushButton(self.technical_support_frame)
        self.technical_support_pushButton.setObjectName(u"technical_support_pushButton")
        self.technical_support_pushButton.setContextMenuPolicy(Qt.NoContextMenu)
        self.technical_support_pushButton.setLayoutDirection(Qt.LeftToRight)
        self.technical_support_pushButton.setText(u"")
        icon9 = QIcon()
        icon9.addFile(u"icons/tech_support.png", QSize(), QIcon.Normal, QIcon.Off)
        self.technical_support_pushButton.setIcon(icon9)
        self.technical_support_pushButton.setIconSize(QSize(64, 64))

        self.verticalLayout_11.addWidget(self.technical_support_pushButton)

        self.technical_support_label = QLabel(self.technical_support_frame)
        self.technical_support_label.setObjectName(u"technical_support_label")
        self.technical_support_label.setLineWidth(0)
        self.technical_support_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.technical_support_label)


        self.horizontalLayout_13.addWidget(self.technical_support_frame)

        self.check_for_updates_frame = QFrame(self.help_tab)
        self.check_for_updates_frame.setObjectName(u"check_for_updates_frame")
        self.check_for_updates_frame.setFrameShape(QFrame.StyledPanel)
        self.check_for_updates_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.check_for_updates_frame)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.new_project_pushButton_5 = QPushButton(self.check_for_updates_frame)
        self.new_project_pushButton_5.setObjectName(u"new_project_pushButton_5")
        self.new_project_pushButton_5.setContextMenuPolicy(Qt.NoContextMenu)
        self.new_project_pushButton_5.setLayoutDirection(Qt.LeftToRight)
        self.new_project_pushButton_5.setText(u"")
        icon10 = QIcon()
        icon10.addFile(u"icons/update.png", QSize(), QIcon.Normal, QIcon.Off)
        self.new_project_pushButton_5.setIcon(icon10)
        self.new_project_pushButton_5.setIconSize(QSize(64, 64))

        self.verticalLayout_12.addWidget(self.new_project_pushButton_5)

        self.new_project_label_5 = QLabel(self.check_for_updates_frame)
        self.new_project_label_5.setObjectName(u"new_project_label_5")
        self.new_project_label_5.setLineWidth(0)
        self.new_project_label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.new_project_label_5)


        self.horizontalLayout_13.addWidget(self.check_for_updates_frame)

        self.new_project_frame_5 = QFrame(self.help_tab)
        self.new_project_frame_5.setObjectName(u"new_project_frame_5")
        self.new_project_frame_5.setFrameShape(QFrame.StyledPanel)
        self.new_project_frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.new_project_frame_5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.new_project_pushButton_6 = QPushButton(self.new_project_frame_5)
        self.new_project_pushButton_6.setObjectName(u"new_project_pushButton_6")
        self.new_project_pushButton_6.setContextMenuPolicy(Qt.NoContextMenu)
        self.new_project_pushButton_6.setLayoutDirection(Qt.LeftToRight)
        self.new_project_pushButton_6.setText(u"")
        icon11 = QIcon()
        icon11.addFile(u"icons/purchase.png", QSize(), QIcon.Normal, QIcon.Off)
        self.new_project_pushButton_6.setIcon(icon11)
        self.new_project_pushButton_6.setIconSize(QSize(64, 64))

        self.verticalLayout_13.addWidget(self.new_project_pushButton_6)

        self.new_project_label_6 = QLabel(self.new_project_frame_5)
        self.new_project_label_6.setObjectName(u"new_project_label_6")
        self.new_project_label_6.setLineWidth(0)
        self.new_project_label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.new_project_label_6)


        self.horizontalLayout_13.addWidget(self.new_project_frame_5)

        self.new_project_frame_6 = QFrame(self.help_tab)
        self.new_project_frame_6.setObjectName(u"new_project_frame_6")
        self.new_project_frame_6.setFrameShape(QFrame.StyledPanel)
        self.new_project_frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.new_project_frame_6)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.new_project_pushButton_7 = QPushButton(self.new_project_frame_6)
        self.new_project_pushButton_7.setObjectName(u"new_project_pushButton_7")
        self.new_project_pushButton_7.setContextMenuPolicy(Qt.NoContextMenu)
        self.new_project_pushButton_7.setLayoutDirection(Qt.LeftToRight)
        self.new_project_pushButton_7.setText(u"")
        icon12 = QIcon()
        icon12.addFile(u"icons/online_help.png", QSize(), QIcon.Normal, QIcon.Off)
        self.new_project_pushButton_7.setIcon(icon12)
        self.new_project_pushButton_7.setIconSize(QSize(64, 64))

        self.verticalLayout_14.addWidget(self.new_project_pushButton_7)

        self.new_project_label_7 = QLabel(self.new_project_frame_6)
        self.new_project_label_7.setObjectName(u"new_project_label_7")
        self.new_project_label_7.setLineWidth(0)
        self.new_project_label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.new_project_label_7)


        self.horizontalLayout_13.addWidget(self.new_project_frame_6)

        icon13 = QIcon()
        icon13.addFile(u"icons/help.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ribbon.addTab(self.help_tab, icon13, "")

        self.horizontalLayout_2.addWidget(self.ribbon)


        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.ribbon.setCurrentIndex(3)
        self.spec_ribbon.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"FSEI Mosta TimeTabler", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.new_project_label.setText(QCoreApplication.translate("MainWindow", u"New Project", None))
        self.open_project_label.setText(QCoreApplication.translate("MainWindow", u"Open Project", None))
        self.new_project_label_2.setText(QCoreApplication.translate("MainWindow", u"Save Project", None))
        self.ribbon.setTabText(self.ribbon.indexOf(self.file_tab), QCoreApplication.translate("MainWindow", u"Home", None))
        self.promo_add_pushbutton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.promo_edit__pushbutton.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.promo_remove_pushbutton.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        ___qtablewidgetitem = self.promo_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Number", None));
        ___qtablewidgetitem1 = self.promo_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem2 = self.promo_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Number of Sections", None));
        ___qtablewidgetitem3 = self.promo_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Number of Groups", None));
        ___qtablewidgetitem4 = self.promo_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Effective per Group", None));
        self.spec_ribbon.setTabText(self.spec_ribbon.indexOf(self.promotions_tab), QCoreApplication.translate("MainWindow", u"Promotions", None))
        ___qtablewidgetitem5 = self.professor_tablewidget.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Number", None));
        ___qtablewidgetitem6 = self.professor_tablewidget.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        self.prof_add_pushbutton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.prof_edit_pushbutton.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.prof_remove_pushbutton.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.spec_ribbon.setTabText(self.spec_ribbon.indexOf(self.professors_tab), QCoreApplication.translate("MainWindow", u"Professors", None))
        ___qtablewidgetitem7 = self.room_tablewidget.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Number", None));
        ___qtablewidgetitem8 = self.room_tablewidget.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem9 = self.room_tablewidget.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"capacity", None));
        ___qtablewidgetitem10 = self.room_tablewidget.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"type", None));
        self.room_add_pushbutton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.room_edit_pushbutton.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.room_remove_pushbutton.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.spec_ribbon.setTabText(self.spec_ribbon.indexOf(self.facilities_tab), QCoreApplication.translate("MainWindow", u"Facilities", None))
        self.module_add_pushbutton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.module_edit_pushbutton.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.module_remove_pushbutton.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.pick_promo_label.setText(QCoreApplication.translate("MainWindow", u"Pick a Promotion", None))
        ___qtablewidgetitem11 = self.modules_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Number", None));
        ___qtablewidgetitem12 = self.modules_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem13 = self.modules_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Acronyme", None));
        ___qtablewidgetitem14 = self.modules_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Number of Lectures", None));
        ___qtablewidgetitem15 = self.modules_tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Number of TDs", None));
        ___qtablewidgetitem16 = self.modules_tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Number of TPs", None));
        self.spec_ribbon.setTabText(self.spec_ribbon.indexOf(self.modules_tab), QCoreApplication.translate("MainWindow", u"Modules", None))
        self.pick_promo_label_2.setText(QCoreApplication.translate("MainWindow", u"Pick a Promotion", None))
        ___qtablewidgetitem17 = self.modules_tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Module", None));
        ___qtablewidgetitem18 = self.modules_tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Lectures Allocation", None));
        ___qtablewidgetitem19 = self.modules_tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"TD Allocation", None));
        ___qtablewidgetitem20 = self.modules_tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"TP  Allocation", None));
        self.spec_ribbon.setTabText(self.spec_ribbon.indexOf(self.assignements_tab), QCoreApplication.translate("MainWindow", u"Assignements", None))
        self.datashow_add_pushbutton_2.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.datashow_edit_pushbutton_2.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.datashow_remove_pushbutton_2.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        ___qtablewidgetitem21 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Number", None));
        ___qtablewidgetitem22 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem23 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Allocation", None));
        self.spec_ribbon.setTabText(self.spec_ribbon.indexOf(self.datashows_tab), QCoreApplication.translate("MainWindow", u"Datashows", None))
        self.ribbon.setTabText(self.ribbon.indexOf(self.data_tab), QCoreApplication.translate("MainWindow", u"Specification", None))
        self.timetable_label.setText(QCoreApplication.translate("MainWindow", u"TimeTable", None))
        self.days_per_week_label.setText(QCoreApplication.translate("MainWindow", u"Days per week", None))
        self.slots_perday_label.setText(QCoreApplication.translate("MainWindow", u"Time slots per day", None))
        self.starting_day_label.setText(QCoreApplication.translate("MainWindow", u"Starting day", None))
        self.starting_day_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Sunday", None))
        self.starting_day_comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Monday", None))
        self.starting_day_comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Tuesday", None))
        self.starting_day_comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Wednesday", None))
        self.starting_day_comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Thursday", None))
        self.starting_day_comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Saturday", None))

        self.slot_duration_label.setText(QCoreApplication.translate("MainWindow", u"Slot duration", None))
        self.slot_duration_lineEdit.setText(QCoreApplication.translate("MainWindow", u"30", None))
        self.mins_label.setText(QCoreApplication.translate("MainWindow", u"Mins", None))
        self.constraints_label.setText(QCoreApplication.translate("MainWindow", u"Constraints", None))
#if QT_CONFIG(tooltip)
        self.studentavailability_checkBox.setToolTip(QCoreApplication.translate("MainWindow", u"Student can only attend one session at a time ", None))
#endif // QT_CONFIG(tooltip)
        self.studentavailability_checkBox.setText(QCoreApplication.translate("MainWindow", u"StudentAvailability", None))
#if QT_CONFIG(tooltip)
        self.professoravailability_checkBox.setToolTip(QCoreApplication.translate("MainWindow", u"Professor can only teach one session at a time", None))
#endif // QT_CONFIG(tooltip)
        self.professoravailability_checkBox.setText(QCoreApplication.translate("MainWindow", u"ProfessorAvailability", None))
#if QT_CONFIG(tooltip)
        self.roomavailability_checkBox.setToolTip(QCoreApplication.translate("MainWindow", u"Room can host only one session at a time", None))
#endif // QT_CONFIG(tooltip)
        self.roomavailability_checkBox.setText(QCoreApplication.translate("MainWindow", u"RoomAvailability", None))
#if QT_CONFIG(tooltip)
        self.threeconsecutivemaxsessions_checkBox.setToolTip(QCoreApplication.translate("MainWindow", u"Professors and students can at most have 3 consecutive sessions", None))
#endif // QT_CONFIG(tooltip)
        self.threeconsecutivemaxsessions_checkBox.setText(QCoreApplication.translate("MainWindow", u"ThreeConsecutiveMaxSessions", None))
#if QT_CONFIG(tooltip)
        self.twocourderdaymax_checkBox.setToolTip(QCoreApplication.translate("MainWindow", u"For each section there will be at most 2 lectures daily", None))
#endif // QT_CONFIG(tooltip)
        self.twocourderdaymax_checkBox.setText(QCoreApplication.translate("MainWindow", u"TwoCourPerDayMax", None))
#if QT_CONFIG(tooltip)
        self.uniquesessiondaily_checkBox.setToolTip(QCoreApplication.translate("MainWindow", u"if a session repeats multiple times a week make sure it's not on the same day", None))
#endif // QT_CONFIG(tooltip)
        self.uniquesessiondaily_checkBox.setText(QCoreApplication.translate("MainWindow", u"UniqueSessionDaily", None))
        self.ribbon.setTabText(self.ribbon.indexOf(self.options_tab), QCoreApplication.translate("MainWindow", u"Options", None))
        self.pick_promo_label_3.setText(QCoreApplication.translate("MainWindow", u"Pick a Promotion", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Pick a Section", None))
        ___qtablewidgetitem24 = self.timetable_tableview.horizontalHeaderItem(0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"08:30 -9:30", None));
        ___qtablewidgetitem25 = self.timetable_tableview.horizontalHeaderItem(1)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"09:30-10:30", None));
        ___qtablewidgetitem26 = self.timetable_tableview.horizontalHeaderItem(2)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"10:30-11:30", None));
        ___qtablewidgetitem27 = self.timetable_tableview.horizontalHeaderItem(3)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"11:30-12:30", None));
        ___qtablewidgetitem28 = self.timetable_tableview.horizontalHeaderItem(4)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"12:30-13:30", None));
        ___qtablewidgetitem29 = self.timetable_tableview.horizontalHeaderItem(5)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"13:30-14:30", None));
        ___qtablewidgetitem30 = self.timetable_tableview.horizontalHeaderItem(6)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"14:30-15:30", None));
        ___qtablewidgetitem31 = self.timetable_tableview.verticalHeaderItem(0)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Sunday ", None));
        ___qtablewidgetitem32 = self.timetable_tableview.verticalHeaderItem(1)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Monday", None));
        ___qtablewidgetitem33 = self.timetable_tableview.verticalHeaderItem(2)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"Tuesday", None));
        ___qtablewidgetitem34 = self.timetable_tableview.verticalHeaderItem(3)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Wednesday ", None));
        ___qtablewidgetitem35 = self.timetable_tableview.verticalHeaderItem(4)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Thursday", None));

        __sortingEnabled = self.timetable_tableview.isSortingEnabled()
        self.timetable_tableview.setSortingEnabled(False)
        self.timetable_tableview.setSortingEnabled(__sortingEnabled)

        self.ribbon.setTabText(self.ribbon.indexOf(self.timetable_tab), QCoreApplication.translate("MainWindow", u"Timetable", None))
        self.about_us_label.setText(QCoreApplication.translate("MainWindow", u"About us", None))
        self.technical_support_label.setText(QCoreApplication.translate("MainWindow", u"Technical support", None))
        self.new_project_label_5.setText(QCoreApplication.translate("MainWindow", u"Check for updates", None))
        self.new_project_label_6.setText(QCoreApplication.translate("MainWindow", u"Register and Purchase", None))
        self.new_project_label_7.setText(QCoreApplication.translate("MainWindow", u"Online Help", None))
        self.ribbon.setTabText(self.ribbon.indexOf(self.help_tab), QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())