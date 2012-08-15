# -*- coding: utf-8 -*-
u"""
Copyright (c) 2012 プレハブ小屋管理人 <yojyo@hotmail.com>
All Rights Reserved.  NO WARRANTY.
"""

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
