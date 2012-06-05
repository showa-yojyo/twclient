# -*- coding: utf-8 -*-

from twcommand import CommandBase
from PyQt4.QtGui import QInputDialog
from PyQt4.QtGui import QLineEdit
from PyQt4.QtGui import QMessageBox

from userform import UserForm

class ShowUser(CommandBase):
    def __init__(self, parent):
        super(ShowUser, self).__init__()
        self.parent = parent

    def execute(self):
        screen_name, ok = QInputDialog.getText(
            self.parent, 
            u'ユーザーを表示',
            u'ユーザーの名前 (screen_name) を入力',
            QLineEdit.Normal,
            u'@')
        if not ok:
            return

        # QString -> unistr
        screen_name = unicode(screen_name)
        if not screen_name.startswith(u'@'):
            screen_name = '@' + screen_name

        form = UserForm(self.parent, screen_name)
        form.show()
