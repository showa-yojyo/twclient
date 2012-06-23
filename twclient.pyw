# -*- coding: utf-8 -*-

import sys
import codecs
import shutil
import time
import traceback
from cStringIO import StringIO

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui_twclient import Ui_MainWindow

from twcommand.request import Request
from twcommand.about import About
from twcommand.preference import Preference
from twcommand.showuser import ShowUser
from twmodel.model import TimeLineItemModel

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
        view = self.ui.textBrowser
        start_time = time.time()
        try:
            sb.showMessage(u"Now loading...")
            QApplication.setOverrideCursor(QCursor(3))
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
        self.ui.textBrowser.clear()
        self.requestTwitter()

    def requestTwitter(self):
        item = self.currentTimeLineItem()
        if not item:
            return
        self.invokeRequestCommand(Request(item, False))

    def onAnchorClicked(self, uri):
        path = unicode(uri.toString())

        if path.startswith(u'chrome://hashtag/'):
            # hash tag
            hashtag = path[len(u'chrome://hashtag/'):]
            model = self.model
            item = model.assureSearchHashTag(hashtag)
            self.ui.comboBox.setCurrentIndex(item.index().row())

        elif path.startswith(u'chrome://user_mention/'):
            # screen_name
            screen_name = path[len(u'chrome://user_mention/'):]
            menu = self.makeMenuUser(screen_name)
            menu.popup(QCursor.pos())
            menu.exec_()
            del menu

        else:
            # general URL
            def copyToClipboard():
                QApplication.clipboard().setText(path)

            def invokeBrowser():
                QDesktopServices.openUrl(uri)

            def searchUrl():
                model = self.model
                item = model.assureSearchUrl(path)
                self.ui.comboBox.setCurrentIndex(item.index().row())

            menu = QMenu(self.ui.textBrowser)
            menu.addAction(u"URL をコピー (&C)", copyToClipboard)
            menu.addAction(u"URL をブラウザーで開く (&O)", invokeBrowser)
            menu.addAction(u"URL をサーチ (&S)", searchUrl)
            menu.popup(QCursor.pos())
            menu.exec_()
            del menu

    def makeMenuUser(self, screen_name):
        def invokeShowUser():
            cmd = ShowUser(self, screen_name)
            cmd.execute()

        def invokeUserTimeLine():
            model = self.model
            item = model.assureUserTimeLine(screen_name)
            self.ui.comboBox.setCurrentIndex(item.index().row())

        def invokeSearchScreenName():
            model = self.model
            item = model.assureSearchScreenName(screen_name)
            self.ui.comboBox.setCurrentIndex(item.index().row())

        menu = QMenu()
        menu.addAction(u"ユーザー詳細画面を表示(&P)", invokeShowUser)
        menu.addAction(u"ユーザータイムラインを表示(&U)", invokeUserTimeLine)
        menu.addAction(u"言及ツイートをサーチ(&M)", invokeSearchScreenName)

        return menu

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
