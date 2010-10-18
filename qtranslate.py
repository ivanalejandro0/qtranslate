#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

try:
    from PyQt4 import QtCore
    from PyQt4 import QtGui
except ImportError:
    print "PyQt4 (Qt4 bindings for Python) is required for this application."
    print "You can find it here: http://www.riverbankcomputing.co.uk"
    sys.exit()

from googletranslate import GoogleTranslate

class QTranslate(QtGui.QWidget, object):
    def __init__ (self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.initGUI()

        self.googletrans = GoogleTranslate()
        self.langFrom = ""
        self.langTo = "es"

        #self.connect(self.pbTranslate, QtCore.SIGNAL("clicked()"), self.on_pbTranslate_clicked)
        self.pbTranslate.clicked.connect(self.on_pbTranslate_clicked)

        #self.connect(self.cbLangFrom, QtCore.SIGNAL("currentIndexChanged(QString)"), self.on_cbLangFrom_currentIndexChanged)
        self.cbLangFrom.currentIndexChanged.connect(self.on_cbLangFrom_currentIndexChanged)
        
        #self.connect(self.cbLangTo, QtCore.SIGNAL("currentIndexChanged(QString)"), self.on_cbLangTo_currentIndexChanged)
        self.cbLangTo.currentIndexChanged['QString'].connect(self.on_cbLangTo_currentIndexChanged)

    def initGUI(self):
        # Idiomas soportados por google como idioma origen. "???" indica que google debe adivinar el idioma origen.
        # Languages supported by Google as source lang. "???" indicates that google has to guess the source language.
        self.cbLangFrom = QtGui.QComboBox()
        self.cbLangFrom.addItem("???")
        self.cbLangFrom.addItem("es")
        self.cbLangFrom.addItem("en")
        self.cbLangFrom.addItem("fr")

        # Languages supported by Google as destination lang.
        self.cbLangTo = QtGui.QComboBox()
        self.cbLangTo.addItem("es")
        self.cbLangTo.addItem("en")
        self.cbLangTo.addItem("fr")

        self.labelFrom = QtGui.QLabel(self.tr('Texto a traducir'))
        self.textFrom = QtGui.QTextEdit()

        self.labelTo = QtGui.QLabel(self.tr('Texto traducido'))
        self.textTo = QtGui.QTextEdit()

        self.pbTranslate = QtGui.QPushButton(self.tr('Traducir'))

        # Create layout and add widgets
        layout = QtGui.QGridLayout()

        layout.addWidget(self.labelFrom, 1, 1)
        layout.addWidget(self.textFrom, 1, 2)

        layout.addWidget(self.labelTo, 2, 1)
        layout.addWidget(self.textTo, 2, 2)

        layout.addWidget(self.cbLangFrom, 3, 1)
        layout.addWidget(self.cbLangTo, 3, 2)

        layout.addWidget(self.pbTranslate, 4, 1, 1, 2)

        # Set the layout to the top widget
        self.setLayout(layout)
        self.setGeometry(250, 250, 500, 200)
        self.setWindowTitle('QTranslate')

    def on_cbLangFrom_currentIndexChanged(self, txt):
        if txt == '???':
            txt = ""
        self.langFrom = str(txt)

    def on_cbLangTo_currentIndexChanged(self, txt):
        self.langTo = str(txt)

    def on_pbTranslate_clicked(self):
        lsrc = self.langFrom
        ldest = self.langTo
        text = str( self.textFrom.toPlainText() )
        self.textTo.setPlainText( self.googletrans.translate(text, lsrc,  ldest) )


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    prog = QTranslate()
    prog.show()
    app.exec_()
