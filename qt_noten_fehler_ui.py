# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_noten_fehler_ui.ui'
#
# Created: Mon Mar 25 03:58:53 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Fehler(object):
    def setupUi(self, Fehler):
        Fehler.setObjectName(_fromUtf8("Fehler"))
        Fehler.resize(354, 110)
        Fehler.setMinimumSize(QtCore.QSize(250, 100))
        Fehler.setWindowTitle(_fromUtf8("Fehler"))
        Fehler.setModal(True)
        self.gridLayout = QtGui.QGridLayout(Fehler)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(Fehler)
        self.label.setText(_fromUtf8("Sorry, aber ein Fehler ist aufgetreten :-("))
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.buttonBox = QtGui.QDialogButtonBox(Fehler)
        self.buttonBox.setMinimumSize(QtCore.QSize(0, 0))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Fehler)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Fehler.accept)
        QtCore.QMetaObject.connectSlotsByName(Fehler)

    def retranslateUi(self, Fehler):
        pass

