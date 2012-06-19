# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class QStatusStreamListWidget(QListWidget):

    def setupGui(self):
        self.setIconSize(QSize(48, 48))
        self.setSortingEnabled(False)
        #listWidget.setWordWrap(True)

        # dummy icon
        self.icon = QIcon()
        self.icon.addPixmap(QPixmap(u":/resource/illvelo-32x32.png"))

    def on_load_latest_page(self, response):
        is_list = False
        if len(response) > 0 and u'lists' in response:
            is_list = True

        if is_list:
            stream = response[u'lists']
        else:
            stream = response

        for element in stream:
            item = QListWidgetItem(self)
            item.setIcon(self.icon) # TODO: obtain icon from each element

            if is_list:
                item.setText(u'{full_name}\n{description}'.format(**element))
            else:
                if u'status' in element:
                    item.setText(u'{screen_name} | {name}\n{status[text]}'.format(**element))
                else:
                    item.setText(u'{screen_name} | {name}'.format(**element))

            if self.count() % 2 == 0:
                color = QColor(u'whitesmoke')
            else:
                color = QColor(u'white')
            item.setBackgroundColor(color)


    def on_load_next_page(self, response):
        # TODO
        print 'on_load_next_page'
