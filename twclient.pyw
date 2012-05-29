# -*- coding: utf-8 -*-

import sys
import codecs
import shutil
import time

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QStringList
from PyQt4.QtGui import QApplication
from PyQt4.QtGui import QCursor
from PyQt4.QtGui import QMainWindow
from PyQt4.QtGui import QMessageBox
from PyQt4.QtGui import QDesktopServices
from PyQt4.QtGui import QTextCursor
from ui_twclient import Ui_MainWindow

import twcommand
import twformat
import twversion

CACHE_PATH = './cache'

class Form(QMainWindow):
    def __init__(self):
        super(Form, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.onInitialUpdate()

        tb = self.ui.textBrowser
        tb.cache_path = CACHE_PATH
        self.command_invoker = twcommand.CommandInvoker(tb)

        slider = tb.verticalScrollBar()

        QtCore.QObject.connect(
            slider, QtCore.SIGNAL(u"valueChanged(int)"), self.onScrollBarValueChanged)
        QtCore.QObject.connect(
            tb, QtCore.SIGNAL(u"anchorClicked(QUrl)"), self.onAnchorClicked)
        QtCore.QMetaObject.connectSlotsByName(self)

    def closeEvent(self, event):
        #shutil.rmtree(CACHE_PATH, True)
        return super(Form, self).closeEvent(event)

    def onInitialUpdate(self):
        cb = self.ui.comboBox
        msg = u"選択してください"

        ls = QStringList(msg)
        self.loadTimelineList(ls)
        cb.addItems(ls)

        te = self.ui.textBrowser
        te.moveCursor(QTextCursor.End)
        te.document().setDefaultStyleSheet(twformat.CSS)

        sb = self.ui.statusbar
        sb.showMessage(msg)

    def loadTimelineList(self, ls):
        try:
            with codecs.open("timelines.ini", 'r', 'utf-8') as fin:
                for line in fin:
                    ls.append(line.strip())
        except IOError:
            pass

    def onComboChanged(self):
        self.requestTwitter(False)

    def requestTwitter(self, fetch_older):
        cb = self.ui.comboBox
        te = self.ui.textBrowser
        sb = self.ui.statusbar

        te.clear()
        if cb.currentIndex() == 0:
            return

        cmdline = unicode(cb.currentText())

        start_time = time.time()
        try:
            sb.showMessage(u"Now loading...")
            QApplication.setOverrideCursor(QCursor(3))
            te.moveCursor(QTextCursor.End)
            self.command_invoker.request(cmdline, fetch_older)
        finally:
            elapsed_time = time.time() - start_time
            sb.showMessage(u"Done ({0:f} sec)".format(elapsed_time))
            QApplication.restoreOverrideCursor()

    def onAnchorClicked(self, hottext):
        path = unicode(hottext.toString())

        if path.startswith(u'chrome://hashtag/'):
            # hash tag
            QMessageBox.information(self, u"Twitter Search", u"TODO: Display Hash tag '%s'" % path)
        elif path.startswith(u'chrome://user_mention'):
            # screen_name
            QMessageBox.information(self, u"User Property", u"TODO: Display %s's user_timeline" % path[1:])
        else:
            # general URL
            QDesktopServices.openUrl(hottext)

    def onAppAbout(self):
        QMessageBox.information(
            self, u"バージョン情報",
            u"とにかくシンプルな Twitter クライアント\nバージョン {0}".format(twversion.VERSION))

    def onAppSettings(self):
        QMessageBox.warning(self, u"設定", u"工事中")

    def onScrollBarValueChanged(self, value):
        slider = self.ui.textBrowser.verticalScrollBar()
        #print 'onValueChanged: {0}/{1}'.format(value, slider.maximum())
        if value > 0 and value == slider.maximum():
            sb = self.ui.statusbar
            te = self.ui.textBrowser
            start_time = time.time()
            try:
                sb.showMessage(u"Now loading...")
                QApplication.setOverrideCursor(QCursor(3))
                te.moveCursor(QTextCursor.End)
                self.command_invoker.request_next_page()
            finally:
                elapsed_time = time.time() - start_time
                sb.showMessage(u"Done ({0:f} sec)".format(elapsed_time))
                QApplication.restoreOverrideCursor()

    def onTimelineRefresh(self):
        self.requestTwitter(False)

    def onUserShow(self):
        QMessageBox.warning(self, u"ユーザーを表示", u"工事中")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Form()
    window.show()
    sys.exit(app.exec_())
