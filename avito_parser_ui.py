# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'avito_parser.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(760, 380)
        Form.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(60, 250, 121, 41))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("background-color: rgb(0, 179, 105);\n"
"color:#fff;\n"
"broder-color: transparent;\n"
"border: none;\n"
"font: 75 9pt \"SF UI  Text G 4\";\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(269, 29, 451, 301))
        self.scrollArea.setMouseTracking(False)
        self.scrollArea.setTabletTracking(False)
        self.scrollArea.setStyleSheet("background-color: rgb(228, 255, 231);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(50, 0, 449, 299))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.Programm_notification = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.Programm_notification.setGeometry(QtCore.QRect(0, 0, 451, 301))
        self.Programm_notification.setStyleSheet("padding: 5px;")
        self.Programm_notification.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.Programm_notification.setObjectName("Programm_notification")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(20, 310, 231, 21))
        self.progressBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setObjectName("progressBar")
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(30, 120, 201, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(30, 150, 201, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(Form)
        self.radioButton_3.setGeometry(QtCore.QRect(30, 180, 201, 17))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(Form)
        self.radioButton_4.setGeometry(QtCore.QRect(30, 210, 201, 17))
        self.radioButton_4.setObjectName("radioButton_4")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 30, 211, 41))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("font: 75 10pt \"SF UI  Text G 4\";")
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.searchInput = QtWidgets.QPlainTextEdit(Form)
        self.searchInput.setGeometry(QtCore.QRect(30, 80, 201, 21))
        self.searchInput.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.searchInput.setAutoFillBackground(False)
        self.searchInput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.searchInput.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.searchInput.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.searchInput.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.searchInput.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.searchInput.setPlainText("")
        self.searchInput.setOverwriteMode(False)
        self.searchInput.setBackgroundVisible(False)
        self.searchInput.setCenterOnScroll(False)
        self.searchInput.setObjectName("plainTextEdit")
        self.pushButton.raise_()
        self.progressBar.raise_()
        self.scrollArea.raise_()
        self.radioButton.raise_()
        self.radioButton_2.raise_()
        self.radioButton_3.raise_()
        self.radioButton_4.raise_()
        self.label.raise_()
        self.searchInput.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Avito Parser"))
        self.pushButton.setText(_translate("Form", "Спарсить"))
        self.radioButton.setText(_translate("Form", "Видеокарты"))
        self.radioButton_2.setText(_translate("Form", "Материнские платы"))
        self.radioButton_3.setText(_translate("Form", "Процессоры"))
        self.radioButton_4.setText(_translate("Form", "Компьютеры"))
        self.label.setText(_translate("Form", "Выберите данные, которые необходимо спарсить"))

