# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_noten_ergebnis_ui.ui'
#
# Created: Mon Mar 25 03:19:55 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Ergebnis(object):
    def setupUi(self, Ergebnis):
        Ergebnis.setObjectName(_fromUtf8("Ergebnis"))
        Ergebnis.resize(241, 142)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Ergebnis.sizePolicy().hasHeightForWidth())
        Ergebnis.setSizePolicy(sizePolicy)
        Ergebnis.setMinimumSize(QtCore.QSize(220, 142))
        Ergebnis.setWindowTitle(_fromUtf8("Ergebnis"))
        Ergebnis.setModal(False)
        self.gridLayout = QtGui.QGridLayout(Ergebnis)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(Ergebnis)
        self.label.setText(_fromUtf8("Anzahl der Noten"))
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.label_2 = QtGui.QLabel(Ergebnis)
        self.label_2.setText(_fromUtf8("Anzahl der Credits"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtGui.QLabel(Ergebnis)
        self.label_3.setText(_fromUtf8("Notenschnitt"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.lineEdit = QtGui.QLineEdit(Ergebnis)
        self.lineEdit.setAcceptDrops(False)
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit)
        self.lineEdit_2 = QtGui.QLineEdit(Ergebnis)
        self.lineEdit_2.setAcceptDrops(False)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit_2)
        self.lineEdit_3 = QtGui.QLineEdit(Ergebnis)
        self.lineEdit_3.setAcceptDrops(False)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEdit_3)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtGui.QDialogButtonBox(Ergebnis)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.label.setBuddy(self.lineEdit)
        self.label_2.setBuddy(self.lineEdit_2)
        self.label_3.setBuddy(self.lineEdit_3)

        self.retranslateUi(Ergebnis)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Ergebnis.accept)
        QtCore.QMetaObject.connectSlotsByName(Ergebnis)

    def retranslateUi(self, Ergebnis):
        pass

