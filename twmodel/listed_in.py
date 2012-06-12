# -*- coding: utf-8 -*-

from twmodel.collection import Collection
from twitter import Twitter, NoAuth

class ListedIn(Collection):
    def __init__(self, screen_name):
        super(ListedIn, self).__init__()
        self.screen_name = screen_name

    def do_request(self, next_cursor):
        auth = NoAuth()
        api = Twitter(auth=auth)

        kwargs = dict(screen_name=self.screen_name)
        if next_cursor > 0:
            kwargs[u'next_cursor'] = next_cursor
        else:
            kwargs[u'next_cursor'] = -1

        return api.lists.memberships(**kwargs)
