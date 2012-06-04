# -*- coding: utf-8 -*-

from twcommand import CommandBase
from PyQt4.QtGui import QMessageBox

class Preference(CommandBase):
    def __init__(self, parent):
        super(Preference, self).__init__()
        self.parent = parent

    def execute(self):
        QMessageBox.warning(
            self.parent, 
            u"アプリケーションの設定", 
            u"工事中")
