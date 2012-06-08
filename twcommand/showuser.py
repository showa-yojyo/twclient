# -*- coding: utf-8 -*-

from twcommand import CommandBase
from PyQt4.QtGui import QInputDialog
from PyQt4.QtGui import QLineEdit
from PyQt4.QtGui import QMessageBox
from twitter import Twitter, NoAuth
from userform import UserForm

class ShowUser(CommandBase):
    def __init__(self, parent, screen_name = None):
        super(ShowUser, self).__init__()
        self.parent = parent
        self.screen_name = screen_name

    def execute(self):
        if not self.screen_name:
            screen_name, ok = QInputDialog.getText(
                self.parent, 
                u'ユーザーを表示',
                u'ユーザーの名前 (screen_name) を入力',
                QLineEdit.Normal,
                u'showa_yojyo')
            if not ok:
                return
            self.screen_name = unicode(screen_name)

        # QString -> unistr
        screen_name = self.screen_name
        if screen_name.startswith(u'@'):
            screen_name = screen_name[1:]

        # Request GET users/show for Twitter API
        response = request_users_show(screen_name)

        # Display
        form = UserForm(self.parent, response)
        form.show()

def request_users_show(screen_name):
    auth = NoAuth()
    api = Twitter(auth=auth)
    kwargs = dict(
        screen_name=screen_name,
        entities=1)
    return api.users.show(**kwargs)
