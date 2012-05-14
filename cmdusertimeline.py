# -*- coding: utf-8 -*-

from cmd import Command
from twitter import Twitter, NoAuth
import twformat

class CmdUserTimeLine(Command):
    def __init__(self, screen_name):
        super(CmdUserTimeLine, self).__init__()
        self.screen_name = screen_name

    def execute(self):
        data = request_statuses_user_timeline(self.screen_name, None)
        text = u""
        for item in data:
            text += twformat.format_status(item)
        self.update_page_info(data)
        return text

    def execute_next_page(self):
        max_id = self.min_id - 1

        data = request_statuses_user_timeline(self.screen_name, max_id)
        text = u""
        for item in data:
            text += twformat.format_status(item)
        self.update_page_info(data)
        return text

def request_statuses_user_timeline(screen_name, max_id):
    auth = NoAuth()
    api = Twitter(auth=auth)

    kwargs = dict(
        screen_name=screen_name,
        count=20,
        page=1,
        include_entities=1,
        include_rts=1,
        exclude_replies=0)

    if max_id is not None:
        kwargs['max_id'] = max_id

    return api.statuses.user_timeline(**kwargs)
