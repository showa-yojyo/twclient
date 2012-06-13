# -*- coding: utf-8 -*-

from twmodel.collection import Collection
from twitter import Twitter, NoAuth

class Follows(Collection):
    def __init__(self, screen_name):
        super(Follows, self).__init__()
        self.screen_name = screen_name

    def update_page_info(self, response):
        pass

    def do_request(self, next_cursor):
        auth = NoAuth()
        api = Twitter(auth=auth)

        kwargs = dict(screen_name=self.screen_name)
        if next_cursor > 0:
            kwargs[u'next_cursor'] = next_cursor
        else:
            kwargs[u'next_cursor'] = -1

        res1 = api.friends.ids(**kwargs)
        if len(res1['ids']):
            ids = ','.join([str(id) for id in res1['ids']])
            res2 = api.users.lookup(user_id=ids, include_entities=0)
            self.next_cursor = res1[u'next_cursor']
            return res2
        else:
            self.next_cursor = 0
            return list()
