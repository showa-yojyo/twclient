# -*- coding: utf-8 -*-

# Borrowed from:
# http://lateral.netmanagers.com.ar/weblog/posts/BB568.html
# http://www.qtcentre.org/archive/index.php/t-5155.html

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import urllib, os, hashlib
import time
import traceback
from cStringIO import StringIO
import twformat

CACHE_PATH = './cache'

class StatusMetaData(QTextBlockUserData):
    def __init__(self, metadata):
        super(StatusMetaData, self).__init__()
        self.metadata = metadata

class QStatusBrowser(QTextBrowser):

    imagecache = dict()

    def __init__(self, parent):
        super(QStatusBrowser, self).__init__(parent)
        self.cache_path = CACHE_PATH # TODO: 設定可能にする

    def setupGui(self, request_handler=None, makeMenu=None):
        try:
            with open('statuses.css', 'r') as fin:
                css = fin.read()
                self.document().setDefaultStyleSheet(css)
        except:
            print >>sys.stderr, "WARNING client.css not read"

        self.request_handler = request_handler
        if request_handler:
            slider = self.verticalScrollBar()
            slider.valueChanged.connect(self.onScrollBarValueChanged)
            self.request_handler(self, False)

        self.makeMenu = makeMenu
        if makeMenu:
            self.setContextMenuPolicy(Qt.CustomContextMenu)
            self.customContextMenuRequested.connect(self.onContextMenu)

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

            if fn in self.imagecache:
                return QVariant(self.imagecache[fn])
            else:
                img = QImage(fn)
                self.imagecache[fn] = img
                return QVariant(img)
        else:
            return super(QStatusBrowser, self).loadResource(type, name)

    def on_load_latest_page(self, response):
        self.moveCursor(QTextCursor.Start)
        caret = QTextCursor(self.textCursor())

        for status in response:
            # metadata
            caret.block().setUserData(StatusMetaData(status))

            # <table>...</table><hr/>
            text = twformat.format_status(status)
            self.insertHtml(text)

        self.moveCursor(QTextCursor.Start)

    def on_load_next_page(self, response):
        self.moveCursor(QTextCursor.End)
        caret = QTextCursor(self.textCursor())

        for status in response:
            # metadata
            caret.block().setUserData(StatusMetaData(status))

            # <table>...</table><hr/>
            text = twformat.format_status(status)
            self.insertHtml(text)

    def onContextMenu(self, pt):
        if not self.makeMenu:
            return

        metadata = self.findStatus(pt)
        menu = self.makeMenu(metadata)
        menu.popup(QCursor.pos())
        menu.exec_()
        del menu

    def findStatus(self, pt):
        caret = self.cursorForPosition(pt)
        block = caret.block()
        while block.isValid():
            userdata = block.userData()
            if userdata:
                return userdata.metadata
            else:
                block = block.previous()

        return None

    def onScrollBarValueChanged(self, value):
        slider = self.verticalScrollBar()
        if value > 0 and value == slider.maximum():
            start_time = time.time()
            try:
                # TODO: command invoker, echo status, etc.
                print u"Now loading..."
                QApplication.setOverrideCursor(QCursor(3))
                self.request_handler(self, True)

            except Exception as e:
                traceback.print_exc()

            finally:
                elapsed_time = time.time() - start_time
                print u"Done ({0:.3f} sec)".format(elapsed_time)
                QApplication.restoreOverrideCursor()
