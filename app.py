#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from elgam.elgam_form import ElGamWindow
from des.des_form import DesWindow
from gamn.gamn_form import GamNWindow
from caesar.caesar_form import CezWindow


class MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.gamNWin = None
        self.cezWin = None
        self.desWin = None
        self.elWin = None

        self.setWindowTitle('Шифрование')
        self.resize(250, 75)
        self.mainLayout = QtWidgets.QVBoxLayout()

        self.butCez = QtWidgets.QPushButton('Шифр Цезаря', self)
        self.butGamN = QtWidgets.QPushButton('Гаммирование по модулю N', self)
        self.butDes = QtWidgets.QPushButton('DES', self)
        self.butElGam = QtWidgets.QPushButton('Шифр Эль-Гамаля', self)

        self.butCez.clicked.connect(self.openCez)
        self.butGamN.clicked.connect(self.openGamN)
        self.butDes.clicked.connect(self.openDes)
        self.butElGam.clicked.connect(self.openEl)

        self.mainLayout.addWidget(self.butCez)
        self.mainLayout.addWidget(self.butGamN)
        self.mainLayout.addWidget(self.butDes)
        self.mainLayout.addWidget(self.butElGam)

        self.setLayout(self.mainLayout)

    def openGamN(self):
        if not self.gamNWin:
            self.gamNWin = GamNWindow(self)
        self.gamNWin.exec_()

    def openCez(self):
        if not self.cezWin:
            self.cezWin = CezWindow(self)
        self.cezWin.exec_()

    def openDes(self):
        if not self.desWin:
            self.desWin = DesWindow(self)
        self.desWin.exec_()

    def openEl(self):
        if not self.elWin:
            self.elWin = ElGamWindow(self)
        self.elWin.exec_()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
