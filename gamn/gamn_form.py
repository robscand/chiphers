#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gamn_form.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from gamn.gamn_chip import gamNCrypt

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 155)
        Form.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.labelKey = QtWidgets.QLabel(Form)
        self.labelKey.setObjectName("labelKey")
        self.gridLayout.addWidget(self.labelKey, 0, 0, 1, 1)
        self.lineEditKey = QtWidgets.QLineEdit(Form)
        self.lineEditKey.setMaxLength(35)
        self.lineEditKey.setObjectName("lineEditKey")
        self.gridLayout.addWidget(self.lineEditKey, 0, 1, 1, 1)
        self.labelMess = QtWidgets.QLabel(Form)
        self.labelMess.setObjectName("labelMess")
        self.gridLayout.addWidget(self.labelMess, 1, 0, 1, 1)
        self.lineEditMess = QtWidgets.QLineEdit(Form)
        self.lineEditMess.setMaxLength(99)
        self.lineEditMess.setObjectName("lineEditMess")
        self.gridLayout.addWidget(self.lineEditMess, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.lineAnswer = QtWidgets.QLineEdit(Form)
        self.lineAnswer.setReadOnly(True)
        self.lineAnswer.setObjectName("lineAnswer")
        self.verticalLayout.addWidget(self.lineAnswer)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnCrypt = QtWidgets.QPushButton(Form)
        self.btnCrypt.setObjectName("btnCrypt")
        self.horizontalLayout.addWidget(self.btnCrypt)
        self.btnDecrypt = QtWidgets.QPushButton(Form)
        self.btnDecrypt.setObjectName("btnDecrypt")
        self.horizontalLayout.addWidget(self.btnDecrypt)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.btnNewCrypt = QtWidgets.QPushButton(Form)
        self.btnNewCrypt.setObjectName("btnNewCrypt")
        self.verticalLayout.addWidget(self.btnNewCrypt)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Гаммирование по модулю N"))
        self.labelKey.setText(_translate("Form", "Ключ:"))
        self.lineEditKey.setToolTip(_translate("Form", "Введите ключ. Это должно быть одно слово,\n"
"состоящее из букв русского алфавита без Ё."))
        self.lineEditKey.setPlaceholderText(_translate("Form", "Введите слово"))
        self.labelMess.setText(_translate("Form", "Сообщение:"))
        self.lineEditMess.setToolTip(_translate("Form", "Введите несколько русских слов без буквы Ё.\n"
"В качестве разделителя допустимы только пробелы."))
        self.lineEditMess.setPlaceholderText(_translate("Form", "Введите предложение"))
        self.lineAnswer.setToolTip(_translate("Form", "Поле итогового сообщения"))
        self.lineAnswer.setPlaceholderText(_translate("Form", "Место для ответа"))
        self.btnCrypt.setText(_translate("Form", "Зашифровать"))
        self.btnDecrypt.setText(_translate("Form", "Расшифровать"))
        self.btnNewCrypt.setText(_translate("Form", "Новый шифр"))

# ------------------------------------------------------
# --- Диалоговое окно шифра Гаммирование по модулю N ---
# ------------------------------------------------------
class GamNWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        # Передаём ссылку на родительский элемент и чтобы виджет
        # отображался как самостоятельное окно указываем тип окна
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.validatorKey = QtGui.QRegExpValidator(QtCore.QRegExp("[а-я,А-Я]+"), self)
        self.ui.lineEditKey.setValidator(self.validatorKey)

        self.validatorMess = QtGui.QRegExpValidator(QtCore.QRegExp("[а-я,А-Я,\s]+"), self)
        self.ui.lineEditMess.setValidator(self.validatorMess)

        self.ui.btnCrypt.clicked.connect(self.on_clicked_btnCrypt)
        self.ui.btnDecrypt.clicked.connect(self.on_clicked_btnDecrypt)
        self.ui.btnNewCrypt.clicked.connect(self.on_clicked_btnNewCrypt)
        self.ui.btnNewCrypt.setEnabled(False)

    @QtCore.pyqtSlot()
    def on_clicked_btnCrypt(self):
        if self.ui.lineEditKey.isModified() and self.ui.lineEditMess.isModified():
            key = self.ui.lineEditKey.text()
            mess = self.ui.lineEditMess.text()
            self.ui.lineAnswer.setText(gamNCrypt(1, key, mess))

            self.ui.lineEditKey.setReadOnly(True)
            self.ui.lineEditMess.setReadOnly(True)
            self.ui.btnCrypt.blockSignals(True)
            self.ui.btnNewCrypt.setEnabled(True)
            self.ui.btnDecrypt.setEnabled(False)

    @QtCore.pyqtSlot()
    def on_clicked_btnDecrypt(self):
        if self.ui.lineEditKey.isModified() and self.ui.lineEditMess.isModified():
            key = self.ui.lineEditKey.text()
            mess = self.ui.lineEditMess.text()
            self.ui.lineAnswer.setText(gamNCrypt(2, key, mess))

            self.ui.lineEditKey.setReadOnly(True)
            self.ui.lineEditMess.setReadOnly(True)
            self.ui.btnDecrypt.blockSignals(True)
            self.ui.btnNewCrypt.setEnabled(True)
            self.ui.btnCrypt.setEnabled(False)

    @QtCore.pyqtSlot()
    def on_clicked_btnNewCrypt(self):
        self.ui.lineEditKey.clear()
        self.ui.lineEditMess.clear()
        self.ui.lineAnswer.clear()
        self.ui.lineEditKey.setReadOnly(False)
        self.ui.lineEditMess.setReadOnly(False)
        self.ui.lineEditKey.setModified(False)
        self.ui.lineEditMess.setModified(False)

        if self.ui.btnCrypt.signalsBlocked() == True:
            self.ui.btnCrypt.blockSignals(False)
            self.ui.btnDecrypt.setEnabled(True)
        if self.ui.btnDecrypt.signalsBlocked() == True:
            self.ui.btnDecrypt.blockSignals(False)
            self.ui.btnCrypt.setEnabled(True)
        self.ui.btnNewCrypt.setEnabled(False)

