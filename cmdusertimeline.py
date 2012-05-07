# -*- coding: utf-8 -*-

from cmd import Command
import twformat

class CmdUserTimeLine(Command):
    def __init__(self, screen_name):
        super(CmdUserTimeLine, self).__init__()
        self.screen_name = screen_name

    def execute(self):
        data = twformat.request_statuses_user_timeline(self.screen_name, None)
        text = u""
        for item in data:
            text += twformat.format_status(item)
        self.update_page_info(data)
        return text

    def execute_next_page(self):
        max_id = self.min_id - 1

        data = twformat.request_statuses_user_timeline(self.screen_name, max_id)
        text = u""
        for item in data:
            text += twformat.format_status(item)
        self.update_page_info(data)
        return text
