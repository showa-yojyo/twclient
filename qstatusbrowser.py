# -*- coding: utf-8 -*-

# Borrowed from:
# http://lateral.netmanagers.com.ar/weblog/posts/BB568.html
# http://www.qtcentre.org/archive/index.php/t-5155.html

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import urllib, os, hashlib
import twformat

CACHE_PATH = './cache'

class QStatusBrowser(QTextBrowser):

    def __init__(self, parent):
        super(QStatusBrowser, self).__init__(parent)
        self.cache_path = CACHE_PATH # TODO: 設定可能にする
        self.document().setDefaultStyleSheet(twformat.CSS)

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
            img = QImage(fn)
            return QVariant(img)
        else:
            return super(QStatusBrowser, self).loadResource(type, name)

    def on_load_latest_page(self, response):
        self.moveCursor(QTextCursor.Start)
        text = u''
        for status in response:
            text += twformat.format_status(status)
        self.insertHtml(text)
        self.moveCursor(QTextCursor.Start)

    def on_load_next_page(self, response):
        self.moveCursor(QTextCursor.End)
        text = u''
        for status in response:
            text += twformat.format_status(status)
        self.insertHtml(text)
