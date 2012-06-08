# -*- coding: utf-8 -*-

import sys
import codecs
import shutil
import time
import traceback
from cStringIO import StringIO

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QStringList
from PyQt4.QtGui import QApplication
from PyQt4.QtGui import QCursor
from PyQt4.QtGui import QMainWindow
from PyQt4.QtGui import QMessageBox
from PyQt4.QtGui import QDesktopServices
from PyQt4.QtGui import QTextCursor
from ui_twclient import Ui_MainWindow

import twformat
from twcommand.request import Request
from twcommand.about import About
from twcommand.preference import Preference
from twcommand.showuser import ShowUser
from twmodel.model import TimeLineItemModel

CACHE_PATH = './cache'

class Form(QMainWindow):
    def __init__(self):
        super(Form, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setupModel()
        self.setupComboBox()
        self.setupBrowser()
        self.setupStatusBar()

    def setupModel(self):
        msg = u"選択してください"
        model = TimeLineItemModel(self.ui.textBrowser)
        model.setTitles(self.loadTimelineList(), msg)
        self.model = model

    def setupComboBox(self):
        cb = self.ui.comboBox
        cb.setModel(self.model)

    def setupBrowser(self):
        tb = self.ui.textBrowser
        tb.moveCursor(QTextCursor.End)
        tb.document().setDefaultStyleSheet(twformat.CSS)
        tb.cache_path = CACHE_PATH
        slider = tb.verticalScrollBar()
        slider.valueChanged.connect(self.onScrollBarValueChanged)
        tb.anchorClicked.connect(self.onAnchorClicked)

    def setupStatusBar(self):
        sb = self.ui.statusbar
        sb.showMessage(u'Ready')

    def closeEvent(self, event):
        #shutil.rmtree(CACHE_PATH, True)
        return super(Form, self).closeEvent(event)

    def currentTimeLineItem(self):
        cb = self.ui.comboBox
        i = cb.currentIndex()
        return self.model.assureItemData(i)

    def invokeRequestCommand(self, cmd):
        sb = self.ui.statusbar
        te = self.ui.textBrowser
        view = te
        start_time = time.time()
        try:
            sb.showMessage(u"Now loading...")
            QApplication.setOverrideCursor(QCursor(3))
            te.moveCursor(QTextCursor.End)
            cmd.execute()

        except Exception as e:
            buf = StringIO()
            traceback.print_exc(file=buf)
            view.setText(u'%s' % buf.getvalue())
            buf.close()

        finally:
            elapsed_time = time.time() - start_time
            sb.showMessage(u"Done ({0:.3f} sec)".format(elapsed_time))
            QApplication.restoreOverrideCursor()

    def loadTimelineList(self):
        ls = QStringList()
        try:
            with codecs.open("timelines.ini", 'r', 'utf-8') as fin:
                for line in fin:
                    ls.append(line.strip())
        except IOError:
            pass

        return ls

    def onComboChanged(self):
        self.requestTwitter()

    def requestTwitter(self):
        item = self.currentTimeLineItem()
        if not item:
            return
        self.invokeRequestCommand(Request(item, False))

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
        cmd = About(self)
        cmd.execute()

    def onAppSettings(self):
        cmd = Preference(self)
        cmd.execute()

    def onScrollBarValueChanged(self, value):
        slider = self.ui.textBrowser.verticalScrollBar()
        if value > 0 and value == slider.maximum():
            item = self.currentTimeLineItem()
            if not item:
                return
            self.invokeRequestCommand(Request(item, True))

    def onTimelineRefresh(self):
        self.requestTwitter()

    def onUserShow(self):
        cmd = ShowUser(self)
        cmd.execute()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Form()
    window.show()
    sys.exit(app.exec_())
