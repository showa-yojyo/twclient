# -*- coding: utf-8 -*-

from cmd import Command
import twformat

class CmdList(Command):
    def __init__(self, owner_screen_name, slug):
        super(CmdList, self).__init__()
        self.owner_screen_name = owner_screen_name
        self.slug = slug

    def execute(self):
        data = twformat.request_lists_statuses(self.owner_screen_name, self.slug, None)
        text = u""
        for item in data:
            text += twformat.format_status(item)
        self.update_page_info(data)
        return text

    def execute_next_page(self):
        max_id = self.min_id - 1

        data = twformat.request_lists_statuses(self.owner_screen_name, self.slug, max_id)
        text = u""
        for item in data:
            text += twformat.format_status(item)
        self.update_page_info(data)
        return text
