# -*- coding: utf-8 -*-

import sys
import traceback
import codecs
#import pickle
from cStringIO import StringIO

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QStringList
from PyQt4.QtGui import QApplication
from PyQt4.QtGui import QMainWindow
from PyQt4.QtGui import QMessageBox
from PyQt4.QtGui import QDesktopServices
from PyQt4.QtGui import QTextCursor
from ui_twclient import Ui_MainWindow

import twformat

class Form(QMainWindow):
    def __init__(self):
        super(Form, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.onInitialUpdate()

        QtCore.QObject.connect(
            self.ui.textBrowser, QtCore.SIGNAL(u"anchorClicked(QUrl)"), self.onAnchorClicked)
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
        cb = self.ui.comboBox
        te = self.ui.textBrowser
        sb = self.ui.statusbar

        if cb.currentIndex() == 0:
            te.clear()
            sb.showMessage(u"Done")
            return

        # TODO
        sb.showMessage(u"処理中…")

        try:
            oneline = unicode(cb.currentText())
            words = oneline.split(" ")
            if(words[0] == u"list"):
                owner_slug = words[1].split(u"/")
                data = twformat.request_lists_statuses(owner_slug[0], owner_slug[1])

                text = u""
                for item in data:
                    text += twformat.format_status(item)
                te.setHtml(text)
            elif(words[0] == u"user_timeline"):
                screen_name = words[1]
                data = twformat.request_statuses_user_timeline(screen_name)

                text = u""
                for item in data:
                    text += twformat.format_status(item)
                te.setHtml(text)
            elif(words[0] == u"search"):
                query = oneline[len(u'search'):].strip()
                data = twformat.request_search(query)

                text = u""
                for item in data['results']:
                    text += twformat.format_search_result(item)
                te.setHtml(text)
            else:
                pass
        except Exception as e:
            buf = StringIO()
            traceback.print_exc(file=buf)
            te.setText(u'%s' % buf.getvalue())
            buf.close()

        te.moveCursor(QTextCursor.Start)

        sb.showMessage(u"Done")

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

    def onTimelineRefresh(self):
        QMessageBox.warning(self, u"タイムラインを更新", u"工事中")

    def onUserShow(self):
        QMessageBox.warning(self, u"ユーザーを表示", u"工事中")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Form()
    window.show()
    sys.exit(app.exec_())
