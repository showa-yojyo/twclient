# -*- coding: utf-8 -*-

from cmd import Command
import twformat

class CmdSearch(Command):
    def __init__(self, query):
        super(CmdSearch, self).__init__()
        self.query = query

    def execute(self):
        data = twformat.request_search(self.query, None)
        text = u""
        for item in data['results']:
            text += twformat.format_search_result(item)
        self.update_page_info(data['results'])
        return text

    def execute_next_page(self):
        max_id = self.min_id - 1

        data = twformat.request_search(self.query, max_id)
        text = u""
        for item in data['results']:
            text += twformat.format_search_result(item)
        self.update_page_info(data['results'])
        return text
