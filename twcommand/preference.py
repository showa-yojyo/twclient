# -*- coding: utf-8 -*-

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
