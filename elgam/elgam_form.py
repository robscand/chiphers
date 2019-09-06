#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'elgam_form.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from elgam.elgam_chip import elGamEncode, elGamDecode, elGamKeyGen

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(651, 161)
        Form.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Form.setFocusPolicy(QtCore.Qt.NoFocus)
        self.gridLayout_3 = QtWidgets.QGridLayout(Form)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.labelPublicKey = QtWidgets.QLabel(Form)
        self.labelPublicKey.setObjectName("labelPublicKey")
        self.gridLayout.addWidget(self.labelPublicKey, 0, 0, 1, 1)
        self.linePublicKey = QtWidgets.QLineEdit(Form)
        self.linePublicKey.setReadOnly(True)
        self.linePublicKey.setObjectName("linePublicKey")
        self.gridLayout.addWidget(self.linePublicKey, 0, 1, 1, 1)
        self.labelPrivateKey = QtWidgets.QLabel(Form)
        self.labelPrivateKey.setObjectName("labelPrivateKey")
        self.gridLayout.addWidget(self.labelPrivateKey, 1, 0, 1, 1)
        self.linePrivateKey = QtWidgets.QLineEdit(Form)
        self.linePrivateKey.setReadOnly(True)
        self.linePrivateKey.setObjectName("linePrivateKey")
        self.gridLayout.addWidget(self.linePrivateKey, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelMess = QtWidgets.QLabel(Form)
        self.labelMess.setObjectName("labelMess")
        self.horizontalLayout.addWidget(self.labelMess)
        self.lineEditMess = QtWidgets.QLineEdit(Form)
        self.lineEditMess.setMaxLength(99)
        self.lineEditMess.setObjectName("lineEditMess")
        self.horizontalLayout.addWidget(self.lineEditMess)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.btnKeyGen = QtWidgets.QPushButton(Form)
        self.btnKeyGen.setObjectName("btnKeyGen")
        self.gridLayout_2.addWidget(self.btnKeyGen, 1, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnDecode = QtWidgets.QRadioButton(Form)
        self.btnDecode.setObjectName("btnDecode")
        self.verticalLayout.addWidget(self.btnDecode)
        self.btnEncode = QtWidgets.QRadioButton(Form)
        self.btnEncode.setObjectName("btnEncode")
        self.verticalLayout.addWidget(self.btnEncode)
        self.btnCrypt = QtWidgets.QPushButton(Form)
        self.btnCrypt.setObjectName("btnCrypt")
        self.verticalLayout.addWidget(self.btnCrypt)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 2, 1, 1)
        self.labelAnswer_1 = QtWidgets.QLabel(Form)
        self.labelAnswer_1.setObjectName("labelAnswer_1")
        self.gridLayout_3.addWidget(self.labelAnswer_1, 1, 0, 1, 1)
        self.labelAnswer_2 = QtWidgets.QLabel(Form)
        self.labelAnswer_2.setObjectName("labelAnswer_2")
        self.gridLayout_3.addWidget(self.labelAnswer_2, 2, 0, 1, 1)
        self.lineDecodeAnswer = QtWidgets.QLineEdit(Form)
        self.lineDecodeAnswer.setReadOnly(True)
        self.lineDecodeAnswer.setObjectName("lineDecodeAnswer")
        self.gridLayout_3.addWidget(self.lineDecodeAnswer, 2, 1, 1, 1)
        self.lineEncodeAnswer = QtWidgets.QLineEdit(Form)
        self.lineEncodeAnswer.setFrame(True)
        self.lineEncodeAnswer.setReadOnly(True)
        self.lineEncodeAnswer.setObjectName("lineEncodeAnswer")
        self.gridLayout_3.addWidget(self.lineEncodeAnswer, 1, 1, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Шифр Эль-Гамаля"))
        self.labelPublicKey.setText(_translate("Form", "Открытый ключ:"))
        self.linePublicKey.setToolTip(_translate("Form", "Поле для вывода открытого ключа."))
        self.linePublicKey.setPlaceholderText(_translate("Form", "Место для ключа"))
        self.labelPrivateKey.setText(_translate("Form", "Закрытый ключ:"))
        self.linePrivateKey.setToolTip(_translate("Form", "Поле для вывода закрытого ключа."))
        self.linePrivateKey.setPlaceholderText(_translate("Form", "Место для ключа"))
        self.labelMess.setText(_translate("Form", "Сообщение:"))
        self.lineEditMess.setToolTip(_translate("Form", "Введите словосочетание на русском языке.\n"
"В качестве разделителя допустимы только пробелы."))
        self.lineEditMess.setPlaceholderText(_translate("Form", "Введите предложение"))
        self.btnKeyGen.setText(_translate("Form", "Получить\n"
"ключи"))
        self.btnDecode.setText(_translate("Form", "Расшифровать"))
        self.btnEncode.setText(_translate("Form", "Зашифровать"))
        self.btnCrypt.setText(_translate("Form", "Выполнить"))
        self.labelAnswer_1.setText(_translate("Form", "Зашифрованное\n"
"сообщение:"))
        self.labelAnswer_2.setText(_translate("Form", "Расшифрованное\n"
"сообщение:"))
        self.lineDecodeAnswer.setToolTip(_translate("Form", "Поле итогового сообщения"))
        self.lineDecodeAnswer.setPlaceholderText(_translate("Form", "Место для ответа"))
        self.lineEncodeAnswer.setToolTip(_translate("Form", "Поле итогового сообщения"))
        self.lineEncodeAnswer.setPlaceholderText(_translate("Form", "Место для ответа"))

#----------------------------------------
#--- Диалоговое окно шифра Эль-Гамаля ---
#----------------------------------------
class ElGamWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.validatorMess = QtGui.QRegExpValidator(QtCore.QRegExp("[а-я,А-Я,\s]+"), self)
        self.ui.lineEditMess.setValidator(self.validatorMess)

        self.ui.btnCrypt.clicked.connect(self.on_clicked_btnCrypt)
        self.ui.btnKeyGen.clicked.connect(self.on_clicked_btnKeyGen)
        self.ui.btnCrypt.blockSignals(True)

    @QtCore.pyqtSlot()
    def on_clicked_btnCrypt(self):
        if self.ui.lineEditMess.isModified():
            if self.ui.btnEncode.isChecked() == True:
                mess = self.ui.lineEditMess.text()
                text_key = self.ui.linePublicKey.text()
                list_key = text_key[1:-1].split(', ')
                public = [int(x) for x in list_key]
                cdct = elGamEncode(mess, public)
                encode_text = ''
                for val in cdct.values():
                    encode_text += '(' + str(val[0]) + ',' + str(val[1]) + ')'
                self.ui.lineEncodeAnswer.setText(encode_text)

                self.ui.lineEditMess.setReadOnly(True)
                self.ui.btnKeyGen.blockSignals(True)

            if self.ui.btnDecode.isChecked() == True:
                if self.ui.lineEncodeAnswer.text() is not '':
                    text_key = self.ui.linePublicKey.text()
                    list_key = text_key[1:-1].split(', ')
                    public = [int(x) for x in list_key]

                    text_key = self.ui.linePrivateKey.text()
                    private = int(text_key)

                    cmsg = len(self.ui.lineEditMess.text())
                    text_dct = self.ui.lineEncodeAnswer.text()
                    new_text = text_dct[1:-1].replace('(', '')
                    new_text = new_text.replace(')', ',')
                    list_dct = new_text.split(',')
                    num_dct = [int(i) for i in list_dct]
                    crypt_dct = {i:[num_dct[i*2], num_dct[i*2 + 1]] for i in range(cmsg)}

                    mess = elGamDecode(crypt_dct, public, private)
                    self.ui.lineDecodeAnswer.setText(mess)

                    self.ui.lineEditMess.setReadOnly(False)
                    self.ui.btnKeyGen.blockSignals(False)
                    self.ui.btnCrypt.blockSignals(True)

    @QtCore.pyqtSlot()
    def on_clicked_btnKeyGen(self):
        public, private = elGamKeyGen()
        pkey = '(' + str(public[0]) + ', ' + str(public[1]) + ', ' + str(public[2]) + ')'
        self.ui.linePublicKey.setText(pkey)
        self.ui.linePrivateKey.setText(str(private))

        if self.ui.lineEncodeAnswer.text() is not '':
            self.ui.lineEncodeAnswer.clear()
        if self.ui.lineDecodeAnswer.text() is not '':
            self.ui.lineDecodeAnswer.clear()
        self.ui.btnCrypt.blockSignals(False)
