# -*- coding: utf-8 -*-
# Copyright (c) 2012 プレハブ小屋 <yojyo@hotmail.com>
# All Rights Reserved.  NO WARRANTY.

from twmodel.timeline import TimeLine
from twitter import Twitter, NoAuth

class Favorites(TimeLine):
    def __init__(self, screen_name, parent=None):
        super(Favorites, self).__init__(parent)
        self.screen_name = screen_name

    def do_request(self, max_id, min_id):
        return request_favorites(self.screen_name, max_id, min_id)

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
