# -*- coding: utf-8 -*-

from twcommand import CommandBase

class Request(CommandBase):
    def __init__(self, item, fetch_older):
        super(Request, self).__init__()
        self.item = item
        self.fetch_older = fetch_older

    def execute(self):
        self.item.request(self.fetch_older)
