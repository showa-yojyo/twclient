# -*- coding: utf-8 -*-
# Copyright (c) 2012 プレハブ小屋 <yojyo@hotmail.com>
# All Rights Reserved.  NO WARRANTY.

from twmodel.collection import Collection
from twitter import Twitter, NoAuth

class Lists(Collection):
    def __init__(self, screen_name, parent=None):
        super(Lists, self).__init__(parent)
        self.screen_name = screen_name

    def do_request(self, next_cursor):
        auth = NoAuth()
        api = Twitter(auth=auth)

        kwargs = dict(screen_name=self.screen_name)
        if next_cursor > 0:
            kwargs[u'next_cursor'] = next_cursor
        else:
            kwargs[u'next_cursor'] = -1

        return api.lists(**kwargs)
