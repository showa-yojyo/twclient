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
from propertydialog import PropertyDialog

from twcommand.request import Request
from twcommand.about import About
from twcommand.preference import Preference
from twcommand.showuser import ShowUser
from twdelegate import ComboBoxItemDelegate
from twmodel.model import TimeLineItemModel
from twsettings import *

class Form(QMainWindow):
    def __init__(self):
        super(Form, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.readSettings()
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
        cb.view().setAlternatingRowColors(True)
        cb.view().setTextElideMode(Qt.ElideRight)
        cb.setModel(self.model)
        cb.setItemDelegate(ComboBoxItemDelegate())
        cb.setMinimumWidth(80) # TODO

    def setupBrowser(self):
        tb = self.ui.textBrowser
        tb.moveCursor(QTextCursor.End)
        tb.setupGui(self.makeMenuStatus)
        slider = tb.verticalScrollBar()
        slider.valueChanged.connect(self.onScrollBarValueChanged)
        tb.anchorClicked.connect(self.onAnchorClicked)

    def setupStatusBar(self):
        sb = self.ui.statusbar
        sb.showMessage(u'準備完了')

    def closeEvent(self, event):
        #shutil.rmtree(CACHE_PATH, True)
        self.writeSettings()
        return super(Form, self).closeEvent(event)

    def readSettings(self):
        #restorePlacement(self, "mainwindow", size=QSize(450, 600))
        # MainWindow の場合はツールバー等も考慮するので別ロジック。
        settings = createSettings()
        self.restoreGeometry(settings.value("mainwindow/geometry").toByteArray())
        self.restoreState(settings.value("mainwindow/state").toByteArray())

    def writeSettings(self):
        #savePlacement(self, "mainwindow")
        # MainWindow の場合はツールバー等も考慮するので別ロジック。
        settings = createSettings()
        settings.setValue("mainwindow/geometry", self.saveGeometry())
        settings.setValue("mainwindow/state", self.saveState())

    def currentTimeLineItem(self):
        cb = self.ui.comboBox
        i = cb.currentIndex()
        return self.model.assureItemData(i)

    def invokeRequestCommand(self, cmd):
        sb = self.ui.statusbar
        view = self.ui.textBrowser
        start_time = time.time()
        try:
            sb.showMessage(u"ロード中...")
            QApplication.setOverrideCursor(QCursor(3))
            cmd.execute()

        except Exception as e:
            buf = StringIO()
            traceback.print_exc(file=buf)
            view.setText(u'%s' % buf.getvalue())
            buf.close()

        finally:
            elapsed_time = time.time() - start_time
            sb.showMessage(u"完了 ({0:.3f} sec)".format(elapsed_time))
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
            menu = self.makeMenuUrl(uri, path)
            menu.popup(QCursor.pos())
            menu.exec_()
            del menu

    def makeMenuList(self, list_entity):
        assert list_entity
        def invokeViewListStatusStream():
            assert list_entity
            if u'slug' in list_entity:
                owner_screen_name = list_entity['user'][u'screen_name']
                slug = list_entity[u'slug']
            elif QString(u'slug') in list_entity:
                owner_screen_name = list_entity[QString('user')][QString(u'screen_name')]
                slug = list_entity[QString(u'slug')]
            else:
                return

            model = self.model
            item = model.assureList(owner_screen_name, slug)
            self.ui.comboBox.setCurrentIndex(item.index().row())

        def invokeViewListProperty():
            assert list_entity
            target = None
            if u'slug' in list_entity:
                target = list_entity
            elif QString(u'slug') in list_entity:
                # QString => unicode
                target = dict()
                for k, v in list_entity.iteritems():
                    target[unicode(k)] = v
            else:
                return

            dlg = PropertyDialog()
            dlg.setup(target)
            dlg.exec_()

        menu = QMenu()
        menu.addAction(u"リストのタイムラインを見る(&V)", invokeViewListStatusStream)
        menu.addAction(u"リストのプロパティ(&R)", invokeViewListProperty) # tooltip?
        return menu

    def makeMenuStatus(self, metadata):
        def invokeCopyToClipboard():
            txt = metadata['text']
            QApplication.clipboard().setText(txt)

        def invokeViewStatusProperty():
            dlg = PropertyDialog()
            dlg.setup(metadata)
            dlg.exec_()

        menu = QMenu()

        action = QAction(u"ツイートをコピー(&C)", self)
        action.triggered.connect(invokeCopyToClipboard)
        if not metadata:
            action.setEnabled(False)
        menu.addAction(action)

        action = QAction(u"ツイートのプロパティー(&R)", self)
        action.triggered.connect(invokeViewStatusProperty)
        if not metadata:
            action.setEnabled(False)
        menu.addAction(action)
        return menu

    def makeMenuUser(self, screen_name):

        if isinstance(screen_name, QString):
            screen_name = unicode(screen_name)

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

    def makeMenuUrl(self, uri, path):
        def copyToClipboard():
            QApplication.clipboard().setText(path)

        def invokeBrowser():
            QDesktopServices.openUrl(uri)

        def searchUrl():
            model = self.model
            item = model.assureSearchUrl(path)
            self.ui.comboBox.setCurrentIndex(item.index().row())

        menu = QMenu()
        menu.addAction(u"URL をコピー(&C)", copyToClipboard)
        menu.addAction(u"URL をブラウザーで開く(&O)", invokeBrowser)
        menu.addAction(u"URL をサーチ(&S)", searchUrl)

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
    try:
        with open('client.css', 'r') as fin:
            css = fin.read()
            app.setStyleSheet(css)
    except:
        print >>sys.stderr, "WARNING client.css not read"

    window = Form()
    window.show()
    sys.exit(app.exec_())
