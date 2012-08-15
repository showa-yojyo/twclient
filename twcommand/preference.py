# -*- coding: utf-8 -*-
u"""
Copyright (c) 2012 プレハブ小屋管理人 <yojyo@hotmail.com>
All Rights Reserved.  NO WARRANTY.
"""

from twcommand import CommandBase
from PyQt4.QtGui import QFontDialog
from PyQt4.QtGui import QMessageBox

class Preference(CommandBase):
    def __init__(self, parent):
        super(Preference, self).__init__()
        self.parent = parent

    def execute(self):
        target = self.parent.ui.textBrowser
        font, ok = QFontDialog.getFont(target)
        if not ok:
            return

        target.setFont(font)
