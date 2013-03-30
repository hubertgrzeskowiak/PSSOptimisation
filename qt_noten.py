#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import urllib
import re
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import SIGNAL, SLOT
from qt_noten_ui import Ui_SourceChooser
from qt_noten_ergebnis_ui import Ui_Ergebnis
from qt_noten_fehler_ui import Ui_Fehler
import noten

class Notenrechner(QtGui.QMainWindow, Ui_SourceChooser):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_SourceChooser.__init__(self)
        self.ergebnis_popups = []
        self.fehler_popup = None
        self.initUI()

    def initUI(self):
        self.setupUi(self)
        self.center()
        self.connectStuff()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def connectStuff(self):
        self.connect(self.lineEdit, SIGNAL("returnPressed()"), self.lineEdit_2.setFocus)
        self.connect(self.lineEdit_2, SIGNAL("returnPressed()"), self.pushButton.click)
        self.connect(self.pushButton, SIGNAL("clicked()"), self.onDownloadButtonClick)
        self.connect(self.pushButton_2 ,SIGNAL("clicked()"), self.openFileDialog)

    def onDownloadButtonClick(self):
        old_text = self.pushButton.text()
        self.pushButton.setText("Einen Moment...")
        self.setDisabled(True)
        self.update()
        QtCore.QCoreApplication.processEvents()
        self.update()
        QtCore.QCoreApplication.processEvents()
        self.downloadPSSOPage()
        self.pushButton.setText(old_text)
        self.setEnabled(True)

    def downloadPSSOPage(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        login_url = 'https://psso.fh-koeln.de/qisserver/rds?state=user&type=1&category=auth.login&startpage=portal.vm&breadCrumbSource=portal'
        params = urllib.urlencode({'asdf': username, 'fdsa': password, 'submit':'Login'}) # lol
        html_1 = urllib.urlopen(login_url, params).read()

        if not noten.checkLogin(html_1):
            self.showErrorPopup(u"Sind die Login Daten möglicherweise falsch?")
            return
        try:
            # Von hier an simulieren wir einen Crawler
            html_2 = urllib.urlopen(noten.getLinkByName(html_1, "Prüfungsverwaltung")).read()
            html_3 = urllib.urlopen(noten.getLinkByName(html_2, "Notenspiegel")).read()
            html_4 = urllib.urlopen(noten.getLinkByName(html_3, re.compile("Abschluss"))).read()
            html_5 = urllib.urlopen(noten.getLinkByGraphic(html_4, "/QIS/images//his_info3.gif")).read()
        except TypeError as e:
           self.showErrorPopup(u"Scheinbar haben sich die PSSO Seiten verändert… Sag' bitte Hugo bescheid, damit er das Programm reparieren kann!")
           return
        try:
            anz_noten, anz_credits, schnitt = noten.getInfos(html_5)
            name = noten.getStudentName(html_5)
            self.presentResults(anz_noten, anz_credits, schnitt, name)
        except noten.ParsingError as e:
            self.showErrorPopup(str(e))

    def openFileDialog(self):
        html_file = QtGui.QFileDialog.getOpenFileName(None, u"HTML Datei auswählen", filter="HTML-Datei (*.html *.htm)")
        html_file = unicode(html_file)
        if html_file:
            try:
                anz_noten, anz_credits, schnitt = noten.getInfos(open(html_file).read())
                name = noten.getStudentName(open(html_file).read())
                self.presentResults(anz_noten, anz_credits, schnitt, name)
            except noten.ParsingError as e:
                self.shoeErrorPopup(str(e))

    def presentResults(self, anz_noten, anz_credits, schnitt, name=None):
        ergebnis_popup = QtGui.QDialog(None)
        ergebnis_ui = Ui_Ergebnis()
        ergebnis_ui.setupUi(ergebnis_popup)
        if name:
            ergebnis_popup.setWindowTitle("Ergebnisse von "+name)
        ergebnis_ui.lineEdit.setText(str(anz_noten))
        ergebnis_ui.lineEdit_2.setText(str(anz_credits))
        ergebnis_ui.lineEdit_3.setText(str(schnitt))
        ergebnis_popup.show()
        self.ergebnis_popups.append(ergebnis_popup)

    def showErrorPopup(self, message):
        if self.fehler_popup:
            self.fehler_popup.close()
            self.fehler_popup = None
        self.fehler_popup = QtGui.QDialog(None)
        self.fehler_ui = Ui_Fehler()
        self.fehler_ui.setupUi(self.fehler_popup)
        self.fehler_ui.label.setText("Sorry, es ist ein Fehler aufgetreten:\n"+message)
        self.fehler_popup.show()

    def closeEvent(self, event):
        for popup in self.ergebnis_popups:
            popup.close()

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Notenrechner()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
