# -*- coding: utf-8 -*-

from twcommand import CommandBase
from PyQt4.QtGui import QMessageBox

class ShowUser(CommandBase):
    def __init__(self, parent):
        super(ShowUser, self).__init__()
        self.parent = parent

    def execute(self):
        QMessageBox.warning(
            self.parent, 
            u"ユーザー詳細を表示", 
            u"工事中")
