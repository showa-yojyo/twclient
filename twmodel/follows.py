# -*- coding: utf-8 -*-

from twmodel.collection import Collection
from twitter import Twitter, NoAuth

# TODO: フォロー系は users.loopkup を併用する。
class Follows(Collection):
    def __init__(self, screen_name):
        super(Follows, self).__init__()
        self.screen_name = screen_name

    def do_request(self, next_cursor):
        auth = NoAuth()
        api = Twitter(auth=auth)

        kwargs = dict(screen_name=self.screen_name)
        if next_cursor > 0:
            kwargs[u'next_cursor'] = next_cursor
        else:
            kwargs[u'next_cursor'] = -1

        return api.friends.ids(**kwargs)
