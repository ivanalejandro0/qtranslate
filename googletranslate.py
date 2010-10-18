#!/usr/bin/python
# -*- coding: utf-8 -*-

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
