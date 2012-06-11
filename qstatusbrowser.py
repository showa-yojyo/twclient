# -*- coding: utf-8 -*-

# Borrowed from:
# http://lateral.netmanagers.com.ar/weblog/posts/BB568.html
# http://www.qtcentre.org/archive/index.php/t-5155.html

from PyQt4 import QtCore
from PyQt4 import QtGui
import urllib, os, hashlib

class QStatusBrowser(QtGui.QTextBrowser):

    def __init__(self, parent):
        super(QStatusBrowser, self).__init__(parent)
        self.cache_path = './cache'

    def loadResource(self, type, name):
        url = unicode(name.toString())
        if url.startswith('http://') or url.startswith('https://'):
            dn = self.cache_path
            if not os.path.isdir(dn):
                os.mkdir(dn)

            fn = os.path.join(dn, hashlib.md5(url).hexdigest())
            if not os.path.isfile(fn):
                urllib.urlretrieve(url, fn)

            # Note: super() seems not to work since PyQt 4.9.1.
            #return super(QStatusBrowser, self).loadResource(type, QtCore.QUrl(fn))
            img = QtGui.QImage(fn)
            return QtCore.QVariant(img)
        else:
            return super(QStatusBrowser, self).loadResource(type, name)

