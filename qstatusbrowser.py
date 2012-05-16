# -*- coding: utf-8 -*-

# Borrowed from:
# http://lateral.netmanagers.com.ar/weblog/posts/BB568.html

from PyQt4 import QtCore
from PyQt4 import QtGui
import urllib, os, hashlib

class QStatusBrowser(QtGui.QTextBrowser):

    def loadResource(self, type, name):
        url = unicode(name.toString())
        if url.startswith('http://'):
            #dn = os.path.expanduser('./cache/')
            dn = './cache'
            if not os.path.isdir(dn):
                os.mkdir(dn)

            fn = os.path.join(dn, hashlib.md5(url).hexdigest())
            if not os.path.isfile(fn):
                urllib.urlretrieve(url, fn)
                return super(QStatusBrowser, self).loadResource(type, QtCore.QUrl(fn))
        else:
            return super(QStatusBrowser, self).loadResource(type, name)

