# -*- coding: utf-8 -*-

from cmd import Command
import twformat

class CmdSearch(Command):
    def __init__(self, query):
        super(CmdSearch, self).__init__()
        self.query = query

    def execute(self):
        data = twformat.request_search(self.query)
        text = u""
        for item in data['results']:
            text += twformat.format_search_result(item)
        return text
