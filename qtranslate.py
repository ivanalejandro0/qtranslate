#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright 2010 Ivan Alejandro <ivanalejandro0@yahoo.com.ar>
#
# This file is part of QTranslate.
#
# QTranslate is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# QTranslate is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with QTranslate.  If not, see <http://www.gnu.org/licenses/>.


import os
import sys

try:
    from PyQt4 import QtCore, QtGui, uic
except ImportError:
    print "PyQt4 (Qt4 bindings for Python) is required for this application."
    print "You can find it here: http://www.riverbankcomputing.co.uk"
    sys.exit()

from googletranslate import GoogleTranslate

class QTranslate(QtGui.QMainWindow):
    about = """
        <center><strong>QTranslator</strong></center>
        Es un programa que permite realizar traducciones de palabras y
        texto gracias a la API de Google Translate.<br />
        """
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        uifile = os.path.join(
            os.path.abspath(os.path.dirname(__file__)), "qtranslate.ui")

        uic.loadUi(uifile, self)

        self.ui = self

        self.googletrans = GoogleTranslate()
        self.langFrom = ""
        self.langTo = "es"


    def translate(self):
        lsrc = self.langFrom
        ldest = self.langTo
        text = str( self.textSource.toPlainText() )
        if text != "":
            self.textDestination.setPlainText( self.googletrans.translate(text, lsrc,  ldest) )


    def on_cbSource_currentIndexChanged(self, txt):
        if txt == '??':
            txt = ""
        self.langFrom = str(txt)


    def on_cbDestination_currentIndexChanged(self, txt):
        self.langTo = str(txt)


    @QtCore.pyqtSlot()
    def on_actionTraducir_triggered(self, b=None):
        self.translate()


    @QtCore.pyqtSlot()
    def on_actionSalir_triggered(self, b=None):
        sys.exit(0)


    def on_pbTranslate_clicked(self):
        self.translate()


    @QtCore.pyqtSlot()
    def on_actionAbout_triggered(self, b=None):
        msgBox = QtGui.QMessageBox()
        msgBox.setText(self.about)
        msgBox.exec_()



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    prog = QTranslate()
    prog.show()
    sys.exit(app.exec_())
