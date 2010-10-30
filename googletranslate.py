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


import sys
import urllib

try:
    if sys.version_info[0:2]==(2, 5):
        import simplejson
    elif sys.version_info[0:2]==(2, 6):
        import json as simplejson
except ImportError:
    print "simplejson library is required for this application."
    print "You can find it here: http://pypi.python.org/pypi/simplejson"
    sys.exit()


class GoogleTranslate(object):
    def __init__ (self):
        self.url = "http://ajax.googleapis.com/ajax/services/language/translate"
        self.params = {}
        self.params['v'] = '1.0'


    def translate(self,  texto, source,  dest):
        self.params['langpair'] = "%s|%s" % (source, dest)
        self.params['q'] = texto
        data = urllib.urlencode(self.params)
        response = urllib.urlopen(self.url, data)
        json = simplejson.load(response)
        traducido = json['responseData']['translatedText']

        return traducido
