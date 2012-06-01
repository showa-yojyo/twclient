# -*- coding: utf-8 -*-

from twmodel.factory import ItemFactory
from PyQt4.QtGui import QStandardItem
from PyQt4.QtGui import QStandardItemModel

class TimeLineItemModel(QStandardItemModel):

    def __init__(self):
        super(TimeLineItemModel, self).__init__(0, 0)
        self.item_factory = ItemFactory()

    def setTitles(self, titlelist, dummyline):
        self.clear()

        item = QStandardItem(dummyline)
        item.setData(None)
        self.appendRow(item)

        for title in titlelist:
            item = QStandardItem(title)
            item.setData(None)
            self.appendRow(item)

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
            curitem.setData(curdata)

        return curdata
