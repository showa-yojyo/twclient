# -*- coding: utf-8 -*-

from cmd import Command
from twitter import Twitter, NoAuth
import twformat

class CmdList(Command):
    def __init__(self, owner_screen_name, slug):
        super(CmdList, self).__init__()
        self.owner_screen_name = owner_screen_name
        self.slug = slug

    def execute(self):
        data = request_lists_statuses(self.owner_screen_name, self.slug, None)
        text = u""
        for item in data:
            text += twformat.format_status(item)
        self.update_page_info(data)
        return text

    def execute_next_page(self):
        max_id = self.min_id - 1

        data = request_lists_statuses(self.owner_screen_name, self.slug, max_id)
        text = u""
        for item in data:
            text += twformat.format_status(item)
        self.update_page_info(data)
        return text

def request_lists_statuses(owner_screen_name, slug, max_id):
    auth = NoAuth()
    api = Twitter(auth=auth)

    kwargs = dict(
        owner_screen_name=owner_screen_name,
        slug=slug,
        per_page=20,
        page=1,
        include_entities=1,
        include_rts=1)

    if max_id is not None:
        kwargs['max_id'] = max_id

    return api.lists.statuses(**kwargs)
