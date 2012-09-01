# -*- coding: utf-8 -*-
# Copyright (c) 2012 プレハブ小屋 <yojyo@hotmail.com>
# All Rights Reserved.  NO WARRANTY.

from twmodel.timeline import TimeLine
from twitter import Twitter, NoAuth

class List(TimeLine):
    def __init__(self, owner_screen_name, slug, parent=None):
        super(List, self).__init__(parent)
        self.owner_screen_name = owner_screen_name
        self.slug = slug

    def do_request(self, max_id, min_id):
        return request_lists_statuses(self.owner_screen_name, self.slug, max_id, min_id)

def request_lists_statuses(owner_screen_name, slug, max_id, min_id):
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
    if min_id is not None:
        kwargs['since_id'] = min_id

    return api.lists.statuses(**kwargs)
