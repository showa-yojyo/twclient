# -*- coding: utf-8 -*-

from twmodel.timeline import TimeLine
from twitter import Twitter, NoAuth
import twformat

class Mentions(TimeLine):
    def __init__(self, screen_name):
        super(Mentions, self).__init__()
        self.screen_name = screen_name

    def do_request(self, max_id, min_id):
        auth = NoAuth()
        api = Twitter(auth=auth)
        kwargs = dict(
            screen_name=self.screen_name,
            count=20,
            include_entities=1)

        if max_id is not None:
            kwargs['max_id'] = max_id
        if min_id is not None:
            kwargs['since_id'] = min_id

        response = api.statuses.mentions(**kwargs)

        text = u""
        for item in response:
            text += twformat.format_status(item)
        return response, text
