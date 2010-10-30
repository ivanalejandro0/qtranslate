#!/usr/bin/python
# -*- coding: utf-8 -*-

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

    def on_actionTraducir_triggered(self, b=None):
        if b == None: return

        self.translate()

    def on_actionSalir_triggered(self, b=None):
        if b == None: return
        sys.exit(0)

    def on_pbTranslate_clicked(self):
        self.translate()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    prog = QTranslate()
    prog.show()
    sys.exit(app.exec_())
