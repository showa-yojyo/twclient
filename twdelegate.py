# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class ComboBoxItemDelegate(QStyledItemDelegate):

    def __init__(self, parent=None, heightFactor=1.5):
        super(ComboBoxItemDelegate, self).__init__(parent)
        self.heightFactor = heightFactor

    def sizeHint(self, option, index):
        size = super(ComboBoxItemDelegate, self).sizeHint(option, index)
        size.setHeight(size.height() * self.heightFactor)
        return size
