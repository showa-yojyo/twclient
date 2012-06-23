# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import time
import traceback

class QStatusStreamListWidget(QListWidget):

    def setupGui(self, request_handler, makeMenu=None):
        self.request_handler = request_handler
        self.setIconSize(QSize(48, 48))
        self.setSortingEnabled(False)
        #listWidget.setWordWrap(True)

        # dummy icon
        self.icon = QIcon()
        self.icon.addPixmap(QPixmap(u":/resource/illvelo-32x32.png"))

        # signal-slot
        slider = self.verticalScrollBar()
        slider.valueChanged.connect(self.onScrollBarValueChanged)
        self.request_handler(self, False)

        self.makeMenu = makeMenu
        if makeMenu:
            self.setContextMenuPolicy(Qt.CustomContextMenu)
            self.customContextMenuRequested.connect(self.onContextMenu)

    def on_load_latest_page(self, response):
        self._on_load_page(response, False)

    def on_load_next_page(self, response):
        self._on_load_page(response, True)

    def _on_load_page(self, response, push_back):
        is_list = False
        if len(response) > 0 and u'lists' in response:
            is_list = True

        if is_list:
            stream = response[u'lists']
        else:
            stream = response

        for i, element in enumerate(stream):
            if is_list:
                label = u'{full_name}\n{description}'.format(**element)
            else:
                if u'status' in element:
                    label = u'{screen_name} | {name}\n{status[text]}'.format(**element)
                else:
                    label = u'{screen_name} | {name}'.format(**element)

            if push_back:
                self.insertItem(i, label)
                item = self.item(i)
            else:
                item = QListWidgetItem(self)
                item.setText(label)

            # store JSON data
            item.setData(Qt.UserRole, QVariant(element))
            # TODO: obtain icon from each element
            item.setIcon(self.icon)

        # alternate row colors
        numitem = self.count()
        for i in xrange(numitem):
            item = self.item(i)
            if not i & 1:
                color = QColor(u'whitesmoke')
            else:
                color = QColor(u'white')
            item.setBackgroundColor(color)

    def onContextMenu(self, pt):
        index = self.indexAt(pt)
        if index < 0:
            return

        row = index.row()
        item = self.item(row)
        item.setSelected(True)
        data = item.data(Qt.UserRole).toPyObject()

        menu = self.makeMenu(data)
        menu.popup(QCursor.pos())
        menu.exec_()
        del menu

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
