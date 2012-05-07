# -*- coding: utf-8 -*-

from cmd import Command
import twformat

class CmdList(Command):
    def __init__(self, owner_screen_name, slug):
        super(CmdList, self).__init__()
        self.owner_screen_name = owner_screen_name
        self.slug = slug

    def execute(self):
        data = twformat.request_lists_statuses(self.owner_screen_name, self.slug)
        text = u""
        for item in data:
            text += twformat.format_status(item)
        return text
