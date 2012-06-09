# -*- coding: utf-8 -*-

from twcommand import CommandBase
import twversion

from PyQt4.QtGui import QMessageBox

class About(CommandBase):
    def __init__(self, parent):
        super(About, self).__init__()
        self.parent = parent

    def execute(self):
        QMessageBox.information(
            self.parent, 
            u"バージョン情報",
            u"とにかくシンプルな Twitter クライアント\nバージョン {0}".format(twversion.VERSION))
