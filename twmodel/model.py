# -*- coding: utf-8 -*-

from twmodel.factory import ItemFactory
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QStandardItem
from PyQt4.QtGui import QStandardItemModel

class TimeLineItemModel(QStandardItemModel):

    def __init__(self, view):
        super(TimeLineItemModel, self).__init__(0, 0)
        self.item_factory = ItemFactory(self)
        self.view = view

    def setTitles(self, titlelist, dummyline):
        self.clear()

        item = QStandardItem(dummyline)
        item.setData(None)
        self.appendRow(item)

        for title in titlelist:
            item = QStandardItem(title)
            item.setToolTip(title)
            item.setData(None)
            self.appendRow(item)

    def _assureItem(self, cmdline):
        result = self.findItems(cmdline, Qt.MatchFixedString)
        if result:
            return result[0]
        else:
            item = QStandardItem(cmdline)
            item.setToolTip(cmdline)
            item.setData(None)
            self.appendRow(item)
            return item

    def assureList(self, owner_screen_name, slug):
        cmdline = u'list {0}/{1}'.format(owner_screen_name, slug)
        return self._assureItem(cmdline)

    def assureSearchScreenName(self, screen_name):
        cmdline = u'search @{0}'.format(screen_name)
        return self._assureItem(cmdline)

    def assureSearchHashTag(self, hashtag):
        cmdline = u'search #{0}'.format(hashtag)
        return self._assureItem(cmdline)

    def assureSearchUrl(self, uri):
        cmdline = u'search {0}'.format(uri)
        return self._assureItem(cmdline)

    def assureUserTimeLine(self, screen_name):
        cmdline = u'user_timeline {0}'.format(screen_name)
        return self._assureItem(cmdline)

    def assureItemData(self, index):
        if index == 0:
            # dummy item
            return None

        curitem = self.item(index)
        curdata = curitem.data().toPyObject()
        if curdata is None:
            # lazy-initialize
            title = unicode(curitem.text())
            curdata = self.item_factory.create(title)
            curdata.add_observer(self.view)
            curitem.setData(curdata)

        assert curdata and curdata.parent()
        return curdata
