# -*- coding: utf-8 -*-

from twmodel.timeline import TimeLine
from twitter import Twitter, NoAuth
import twformat

class UserTimeLine(TimeLine):
    def __init__(self, screen_name):
        super(UserTimeLine, self).__init__()
        self.screen_name = screen_name

    def do_request(self, max_id, min_id):
        data = request_statuses_user_timeline(self.screen_name, max_id, min_id)
        text = u""
        for item in data:
            text += twformat.format_status(item)
        return data, text

def request_statuses_user_timeline(screen_name, max_id, min_id):
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
    if min_id is not None:
        kwargs['min_id'] = min_id

    return api.statuses.user_timeline(**kwargs)
