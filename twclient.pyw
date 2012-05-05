# -*- coding: utf-8 -*-

import sys
import codecs

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

class Form(QMainWindow):
    def __init__(self):
        super(Form, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.command_invoker = twcommand.CommandInvoker()
        self.onInitialUpdate()

        tb = self.ui.textBrowser
        slider = tb.verticalScrollBar()

        QtCore.QObject.connect(
            slider, QtCore.SIGNAL(u"valueChanged(int)"), self.onScrollBarValueChanged)
        QtCore.QObject.connect(
            tb, QtCore.SIGNAL(u"anchorClicked(QUrl)"), self.onAnchorClicked)
        QtCore.QMetaObject.connectSlotsByName(self)

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
        self.requestTwitter()

    def requestTwitter(self):
        cb = self.ui.comboBox
        te = self.ui.textBrowser
        sb = self.ui.statusbar

        if cb.currentIndex() == 0:
            te.clear()
            sb.showMessage(u"Done")
            return

        QApplication.setOverrideCursor(QCursor(3))
        sb.showMessage(u"Now loading...")
        cmdline = unicode(cb.currentText())

        te.moveCursor(QTextCursor.End)
        self.command_invoker.invoke_command(cmdline, te)

        #te.moveCursor(QTextCursor.Start)
        sb.showMessage(u"Done")
        QApplication.restoreOverrideCursor()

    def onAnchorClicked(self, hottext):
        path = unicode(hottext.toString())

        if path.startswith(u'chrome:://hashtag/'):
            # hash tag
            QMessageBox.information(self, u"Twitter Search", u"TODO: Display Hash tag '%s'" % path)
        elif path.startswith(u'chrome:://user_mention'):
            # screen_name
            QMessageBox.information(self, u"User Property", u"TODO: Display %s's user_timeline" % path[1:])
        else:
            # general URL
            QDesktopServices.openUrl(hottext)

    def onAppAbout(self):
        QMessageBox.information(
            self, u"About Twitter Client",
            u"とにかくシンプルな Twitter Client")

    def onAppSettings(self):
        QMessageBox.warning(self, u"設定", u"工事中")

    def onScrollBarValueChanged(self, value):
        slider = self.ui.textBrowser.verticalScrollBar()
        #print 'onValueChanged: {0}/{1}'.format(value, slider.maximum())

    def onTimelineRefresh(self):
        self.requestTwitter()

    def onUserShow(self):
        QMessageBox.warning(self, u"ユーザーを表示", u"工事中")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Form()
    window.show()
    sys.exit(app.exec_())
