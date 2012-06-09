# -*- coding: utf-8 -*-

from twmodel.timeline import TimeLine
from twitter import Twitter, NoAuth
import twformat

class Favorites(TimeLine):
    def __init__(self, screen_name):
        super(Favorites, self).__init__()
        self.screen_name = screen_name

    def do_request(self, max_id, min_id):
        response = request_favorites(self.screen_name, max_id, min_id)
        text = u""
        for item in response:
            text += twformat.format_status(item)
        return response, text

def request_favorites(screen_name, max_id, min_id):
    auth = NoAuth()
    api = Twitter(auth=auth)

    kwargs = dict(
        screen_name=screen_name,
        count=20,
        page=1,
        include_entities=1)

    if max_id is not None:
        kwargs['max_id'] = max_id
    if min_id is not None:
        kwargs['since_id'] = min_id

    return api.favorites(**kwargs)
