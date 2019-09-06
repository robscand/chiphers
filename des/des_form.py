#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'des_form.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from des.des_chip import encodeDES, decodeDES

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(516, 602)
        Form.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(9, 9, 501, 86))
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.labelKey = QtWidgets.QLabel(self.widget)
        self.labelKey.setObjectName("labelKey")
        self.gridLayout.addWidget(self.labelKey, 1, 0, 1, 1)
        self.labelMess = QtWidgets.QLabel(self.widget)
        self.labelMess.setObjectName("labelMess")
        self.gridLayout.addWidget(self.labelMess, 0, 0, 1, 1)
        self.lineEditMess = QtWidgets.QLineEdit(self.widget)
        self.lineEditMess.setMaxLength(4)
        self.lineEditMess.setObjectName("lineEditMess")
        self.gridLayout.addWidget(self.lineEditMess, 0, 1, 1, 1)
        self.lineEditKey = QtWidgets.QLineEdit(self.widget)
        self.lineEditKey.setMaxLength(4)
        self.lineEditKey.setObjectName("lineEditKey")
        self.gridLayout.addWidget(self.lineEditKey, 1, 1, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioBtnEncode = QtWidgets.QRadioButton(self.widget)
        self.radioBtnEncode.setObjectName("radioBtnEncode")
        self.verticalLayout.addWidget(self.radioBtnEncode)
        self.radioBtnDecode = QtWidgets.QRadioButton(self.widget)
        self.radioBtnDecode.setObjectName("radioBtnDecode")
        self.verticalLayout.addWidget(self.radioBtnDecode)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.btnCrypt = QtWidgets.QPushButton(self.widget)
        self.btnCrypt.setObjectName("btnCrypt")
        self.horizontalLayout_2.addWidget(self.btnCrypt)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelFirstRep = QtWidgets.QLabel(self.widget)
        self.labelFirstRep.setObjectName("labelFirstRep")
        self.horizontalLayout.addWidget(self.labelFirstRep)
        self.lineEditFirst = QtWidgets.QLineEdit(self.widget)
        self.lineEditFirst.setReadOnly(True)
        self.lineEditFirst.setObjectName("lineEditFirst")
        self.horizontalLayout.addWidget(self.lineEditFirst)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.widget1 = QtWidgets.QWidget(Form)
        self.widget1.setGeometry(QtCore.QRect(9, 101, 401, 431))
        self.widget1.setObjectName("widget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.labelRound = QtWidgets.QLabel(self.widget1)
        self.labelRound.setObjectName("labelRound")
        self.gridLayout_2.addWidget(self.labelRound, 0, 0, 1, 1)
        self.labelRoundKey = QtWidgets.QLabel(self.widget1)
        self.labelRoundKey.setObjectName("labelRoundKey")
        self.gridLayout_2.addWidget(self.labelRoundKey, 0, 1, 1, 1)
        self.labelRound_1 = QtWidgets.QLabel(self.widget1)
        self.labelRound_1.setObjectName("labelRound_1")
        self.gridLayout_2.addWidget(self.labelRound_1, 1, 0, 1, 1)
        self.lineKey_1 = QtWidgets.QLineEdit(self.widget1)
        self.lineKey_1.setReadOnly(True)
        self.lineKey_1.setObjectName("lineKey_1")
        self.gridLayout_2.addWidget(self.lineKey_1, 1, 1, 1, 1)
        self.labelRound_2 = QtWidgets.QLabel(self.widget1)
        self.labelRound_2.setObjectName("labelRound_2")
        self.gridLayout_2.addWidget(self.labelRound_2, 2, 0, 1, 1)
        self.lineKey_2 = QtWidgets.QLineEdit(self.widget1)
        self.lineKey_2.setReadOnly(True)
        self.lineKey_2.setObjectName("lineKey_2")
        self.gridLayout_2.addWidget(self.lineKey_2, 2, 1, 1, 1)
        self.labelRound_3 = QtWidgets.QLabel(self.widget1)
        self.labelRound_3.setObjectName("labelRound_3")
        self.gridLayout_2.addWidget(self.labelRound_3, 3, 0, 1, 1)
        self.lineKey_3 = QtWidgets.QLineEdit(self.widget1)
        self.lineKey_3.setReadOnly(True)
        self.lineKey_3.setObjectName("lineKey_3")
        self.gridLayout_2.addWidget(self.lineKey_3, 3, 1, 1, 1)
        self.labelRound_4 = QtWidgets.QLabel(self.widget1)
        self.labelRound_4.setObjectName("labelRound_4")
        self.gridLayout_2.addWidget(self.labelRound_4, 4, 0, 1, 1)
        self.lineKey_4 = QtWidgets.QLineEdit(self.widget1)
        self.lineKey_4.setReadOnly(True)
        self.lineKey_4.setObjectName("lineKey_4")
        self.gridLayout_2.addWidget(self.lineKey_4, 4, 1, 1, 1)
        self.labelRound_5 = QtWidgets.QLabel(self.widget1)
        self.labelRound_5.setObjectName("labelRound_5")
        self.gridLayout_2.addWidget(self.labelRound_5, 5, 0, 1, 1)
        self.lineKey_5 = QtWidgets.QLineEdit(self.widget1)
        self.lineKey_5.setReadOnly(True)
        self.lineKey_5.setObjectName("lineKey_5")
        self.gridLayout_2.addWidget(self.lineKey_5, 5, 1, 1, 1)
        self.labelRound_6 = QtWidgets.QLabel(self.widget1)
        self.labelRound_6.setObjectName("labelRound_6")
        self.gridLayout_2.addWidget(self.labelRound_6, 6, 0, 1, 1)
        self.lineKey_6 = QtWidgets.QLineEdit(self.widget1)
        self.lineKey_6.setReadOnly(True)
        self.lineKey_6.setObjectName("lineKey_6")
        self.gridLayout_2.addWidget(self.lineKey_6, 6, 1, 1, 1)
        self.labelRound_7 = QtWidgets.QLabel(self.widget1)
        self.labelRound_7.setObjectName("labelRound_7")
        self.gridLayout_2.addWidget(self.labelRound_7, 7, 0, 1, 1)
        self.lineKey_7 = QtWidgets.QLineEdit(self.widget1)
        self.lineKey_7.setReadOnly(True)
        self.lineKey_7.setObjectName("lineKey_7")
        self.gridLayout_2.addWidget(self.lineKey_7, 7, 1, 1, 1)
        self.labelRound_8 = QtWidgets.QLabel(self.widget1)
        self.labelRound_8.setObjectName("labelRound_8")
        self.gridLayout_2.addWidget(self.labelRound_8, 8, 0, 1, 1)
        self.lineKey_8 = QtWidgets.QLineEdit(self.widget1)
        self.lineKey_8.setReadOnly(True)
        self.lineKey_8.setObjectName("lineKey_8")
        self.gridLayout_2.addWidget(self.lineKey_8, 8, 1, 1, 1)
        self.labelRound_9 = QtWidgets.QLabel(self.widget1)
        self.labelRound_9.setObjectName("labelRound_9")
        self.gridLayout_2.addWidget(self.labelRound_9, 9, 0, 1, 1)
        self.lineKey_9 = QtWidgets.QLineEdit(self.widget1)
        self.lineKey_9.setReadOnly(True)
        self.lineKey_9.setObjectName("lineKey_9")
        self.gridLayout_2.addWidget(self.lineKey_9, 9, 1, 1, 1)
        self.labelRound_10 = QtWidgets.QLabel(self.widget1)
        self.labelRound_10.setObjectName("labelRound_10")
        self.gridLayout_2.addWidget(self.labelRound_10, 10, 0, 1, 1)
        self.lineKey_10 = QtWidgets.QLineEdit(self.widget1)
        self.lineKey_10.setReadOnly(True)
        self.lineKey_10.setObjectName("lineKey_10")
        self.gridLayout_2.addWidget(self.lineKey_10, 10, 1, 1, 1)
        self.labelRound_11 = QtWidgets.QLabel(self.widget1)
        self.labelRound_11.setObjectName("labelRound_11")
        self.gridLayout_2.addWidget(self.labelRound_11, 11, 0, 1, 1)
        self.lineKey_11 = QtWidgets.QLineEdit(self.widget1)
        self.lineKey_11.setReadOnly(True)
        self.lineKey_11.setObjectName("lineKey_11")
        self.gridLayout_2.addWidget(self.lineKey_11, 11, 1, 1, 1)
        self.labelRound_12 = QtWidgets.QLabel(self.widget1)
        self.labelRound_12.setObjectName("labelRound_12")
        self.gridLayout_2.addWidget(self.labelRound_12, 12, 0, 1, 1)
        self.lineKey_12 = QtWidgets.QLineEdit(self.widget1)
        self.lineKey_12.setReadOnly(True)
        self.lineKey_12.setObjectName("lineKey_12")
        self.gridLayout_2.addWidget(self.lineKey_12, 12, 1, 1, 1)
        self.labelRound_13 = QtWidgets.QLabel(self.widget1)
        self.labelRound_13.setObjectName("labelRound_13")
        self.gridLayout_2.addWidget(self.labelRound_13, 13, 0, 1, 1)
        self.lineKey_13 = QtWidgets.QLineEdit(self.widget1)
        self.lineKey_13.setReadOnly(True)
        self.lineKey_13.setObjectName("lineKey_13")
        self.gridLayout_2.addWidget(self.lineKey_13, 13, 1, 1, 1)
        self.labelRound_14 = QtWidgets.QLabel(self.widget1)
        self.labelRound_14.setObjectName("labelRound_14")
        self.gridLayout_2.addWidget(self.labelRound_14, 14, 0, 1, 1)
        self.lineKey_14 = QtWidgets.QLineEdit(self.widget1)
        self.lineKey_14.setReadOnly(True)
        self.lineKey_14.setObjectName("lineKey_14")
        self.gridLayout_2.addWidget(self.lineKey_14, 14, 1, 1, 1)
        self.labelRound_15 = QtWidgets.QLabel(self.widget1)
        self.labelRound_15.setObjectName("labelRound_15")
        self.gridLayout_2.addWidget(self.labelRound_15, 15, 0, 1, 1)
        self.lineKey_15 = QtWidgets.QLineEdit(self.widget1)
        self.lineKey_15.setReadOnly(True)
        self.lineKey_15.setObjectName("lineKey_15")
        self.gridLayout_2.addWidget(self.lineKey_15, 15, 1, 1, 1)
        self.labelRound_16 = QtWidgets.QLabel(self.widget1)
        self.labelRound_16.setObjectName("labelRound_16")
        self.gridLayout_2.addWidget(self.labelRound_16, 16, 0, 1, 1)
        self.lineKey_16 = QtWidgets.QLineEdit(self.widget1)
        self.lineKey_16.setReadOnly(True)
        self.lineKey_16.setObjectName("lineKey_16")
        self.gridLayout_2.addWidget(self.lineKey_16, 16, 1, 1, 1)
        self.widget2 = QtWidgets.QWidget(Form)
        self.widget2.setGeometry(QtCore.QRect(9, 538, 501, 54))
        self.widget2.setObjectName("widget2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.labelLastRep = QtWidgets.QLabel(self.widget2)
        self.labelLastRep.setObjectName("labelLastRep")
        self.gridLayout_3.addWidget(self.labelLastRep, 0, 0, 1, 1)
        self.labelAnswer = QtWidgets.QLabel(self.widget2)
        self.labelAnswer.setObjectName("labelAnswer")
        self.gridLayout_3.addWidget(self.labelAnswer, 1, 0, 1, 1)
        self.lineAnswer = QtWidgets.QLineEdit(self.widget2)
        self.lineAnswer.setReadOnly(True)
        self.lineAnswer.setObjectName("lineAnswer")
        self.gridLayout_3.addWidget(self.lineAnswer, 1, 1, 1, 1)
        self.lineEditLast = QtWidgets.QLineEdit(self.widget2)
        self.lineEditLast.setReadOnly(True)
        self.lineEditLast.setObjectName("lineEditLast")
        self.gridLayout_3.addWidget(self.lineEditLast, 0, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "DES"))
        self.labelKey.setText(_translate("Form", "Ключ:"))
        self.labelMess.setText(_translate("Form", "Сообщение:"))
        self.lineEditMess.setToolTip(_translate("Form", "Введите слово из русских букв.\n"
"Длина слова - 4 символа!"))
        self.lineEditMess.setPlaceholderText(_translate("Form", "Введите слово"))
        self.lineEditKey.setToolTip(_translate("Form", "Введите слово из русских букв.\n"
"Длина слова - 4 символа!"))
        self.lineEditKey.setPlaceholderText(_translate("Form", "Введите слово"))
        self.radioBtnEncode.setText(_translate("Form", "Зашифровать"))
        self.radioBtnDecode.setText(_translate("Form", "Расшифровать"))
        self.btnCrypt.setText(_translate("Form", "DES"))
        self.labelFirstRep.setText(_translate("Form", "Первая\n"
"перестановка:"))
        self.lineEditFirst.setPlaceholderText(_translate("Form", "Перестановка"))
        self.labelRound.setText(_translate("Form", "Раунд:"))
        self.labelRoundKey.setText(_translate("Form", "Подключ раунда:"))
        self.labelRound_1.setText(_translate("Form", "Раунд 1"))
        self.lineKey_1.setPlaceholderText(_translate("Form", "Подключ"))
        self.labelRound_2.setText(_translate("Form", "Раунд 2"))
        self.lineKey_2.setPlaceholderText(_translate("Form", "Подключ"))
        self.labelRound_3.setText(_translate("Form", "Раунд 3"))
        self.lineKey_3.setPlaceholderText(_translate("Form", "Подключ"))
        self.labelRound_4.setText(_translate("Form", "Раунд 4"))
        self.lineKey_4.setPlaceholderText(_translate("Form", "Подключ"))
        self.labelRound_5.setText(_translate("Form", "Раунд 5"))
        self.lineKey_5.setPlaceholderText(_translate("Form", "Подключ"))
        self.labelRound_6.setText(_translate("Form", "Раунд 6"))
        self.lineKey_6.setPlaceholderText(_translate("Form", "Подключ"))
        self.labelRound_7.setText(_translate("Form", "Раунд 7"))
        self.lineKey_7.setPlaceholderText(_translate("Form", "Подключ"))
        self.labelRound_8.setText(_translate("Form", "Раунд 8"))
        self.lineKey_8.setPlaceholderText(_translate("Form", "Подключ"))
        self.labelRound_9.setText(_translate("Form", "Раунд 9"))
        self.lineKey_9.setPlaceholderText(_translate("Form", "Подключ"))
        self.labelRound_10.setText(_translate("Form", "Раунд 10"))
        self.lineKey_10.setPlaceholderText(_translate("Form", "Подключ"))
        self.labelRound_11.setText(_translate("Form", "Раунд 11"))
        self.lineKey_11.setPlaceholderText(_translate("Form", "Подключ"))
        self.labelRound_12.setText(_translate("Form", "Раунд 12"))
        self.lineKey_12.setPlaceholderText(_translate("Form", "Подключ"))
        self.labelRound_13.setText(_translate("Form", "Раунд 13"))
        self.lineKey_13.setPlaceholderText(_translate("Form", "Подключ"))
        self.labelRound_14.setText(_translate("Form", "Раунд 14"))
        self.lineKey_14.setPlaceholderText(_translate("Form", "Подключ"))
        self.labelRound_15.setText(_translate("Form", "Раунд 15"))
        self.lineKey_15.setPlaceholderText(_translate("Form", "Подключ"))
        self.labelRound_16.setText(_translate("Form", "Раунд 16"))
        self.lineKey_16.setPlaceholderText(_translate("Form", "Подключ"))
        self.labelLastRep.setText(_translate("Form", "Конечная\n"
"перестановка:"))
        self.labelAnswer.setText(_translate("Form", "Ответ:"))
        self.lineAnswer.setToolTip(_translate("Form", "Поле итогового сообщения"))
        self.lineAnswer.setPlaceholderText(_translate("Form", "Место для ответа"))
        self.lineEditLast.setPlaceholderText(_translate("Form", "Перестановка"))

# ---------------------------------
# --- Диалоговое окно шифрв DES ---
# ---------------------------------
class DesWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.validatorKey = QtGui.QRegExpValidator(QtCore.QRegExp("[а-я,,А-Я]{4}"), self)
        self.ui.lineEditKey.setValidator(self.validatorKey)

        self.validatorMess = QtGui.QRegExpValidator(QtCore.QRegExp("[а-я,А-Я]{4}"), self)
        self.ui.lineEditMess.setValidator(self.validatorMess)

        self.ui.btnCrypt.clicked.connect(self.on_clicked_btnCrypt)

    @QtCore.pyqtSlot()
    def on_clicked_btnCrypt(self):
        lines = [self.ui.lineKey_1, self.ui.lineKey_2, self.ui.lineKey_3, self.ui.lineKey_4,
                self.ui.lineKey_5, self.ui.lineKey_6, self.ui.lineKey_7, self.ui.lineKey_8,
                self.ui.lineKey_9, self.ui.lineKey_10, self.ui.lineKey_11, self.ui.lineKey_12,
                self.ui.lineKey_13, self.ui.lineKey_14, self.ui.lineKey_15, self.ui.lineKey_16]
        if self.ui.lineEditKey.isModified() == True and self.ui.lineEditMess.isModified() == True:
            if self.ui.radioBtnEncode.isChecked() == True \
                    and len(self.ui.lineEditKey.text()) == 4 \
                    and len(self.ui.lineEditMess.text()) == 4:
                key = self.ui.lineEditKey.text()
                mess = self.ui.lineEditMess.text()

                start_replace, answer, dkeys = encodeDES(mess, key)
                last_replace = answer

                self.ui.lineEditFirst.setText(start_replace)
                self.ui.lineEditLast.setText(last_replace)
                self.ui.lineAnswer.setText(answer)
                for ind, line in enumerate(lines):
                    line.setText(dkeys[ind])

                self.ui.lineEditKey.setModified(False)
                self.ui.lineEditMess.setModified(False)

        if self.ui.lineEditKey.isModified() == False and self.ui.lineEditMess.isModified() == False:
            if self.ui.radioBtnDecode.isChecked() == True \
                    and self.ui.lineAnswer.text() is not ''\
                    and self.ui.lineAnswer.text() != self.ui.lineEditMess.text():
                mess = self.ui.lineAnswer.text()
                dkeys = {}
                for ind, line in enumerate(lines):
                    key = line.text()
                    dkeys[ind] = key

                start_replace, last_replace, answer, dkeys = decodeDES(mess, dkeys)

                self.ui.lineEditFirst.clear()
                self.ui.lineEditFirst.setText(start_replace)
                self.ui.lineEditLast.clear()
                self.ui.lineEditLast.setText(last_replace)
                self.ui.lineAnswer.clear()
                self.ui.lineAnswer.setText(answer)
                for ind, line in enumerate(lines):
                    line.clear()
                    line.setText(dkeys[ind])