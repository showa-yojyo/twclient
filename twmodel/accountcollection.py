# -*- coding: utf-8 -*-
u"""
Copyright (c) 2012 プレハブ小屋管理人 <yojyo@hotmail.com>
All Rights Reserved.  NO WARRANTY.
"""

from twmodel.collection import Collection
from twitter import Twitter, NoAuth

class AccountCollection(Collection):
    """
    This is the superclass of class Follows and FollowedBy.
    """

    def __init__(self, screen_name, parent=None):
        super(AccountCollection, self).__init__(parent)
        self.screen_name = screen_name
        self.user_ids_rest = None

    def update_page_info(self, response):
        pass

    def do_request(self, next_cursor):
        auth = NoAuth()
        api = Twitter(auth=auth)
        if self.user_ids_rest:
            # api.users.lookup のみで事足りる。
            return self._request_users_lookup(api, self.user_ids_rest)
        else:
            kwargs = dict(screen_name=self.screen_name)
            if next_cursor > 0:
                kwargs[u'next_cursor'] = next_cursor
            else:
                kwargs[u'next_cursor'] = -1

            request = self.make_request_api(api)
            res1 = request(**kwargs)
            self.next_cursor = res1[u'next_cursor']
            return self._request_users_lookup(api, res1['ids'])

    def _request_users_lookup(self, api, user_ids):
        num_users = len(user_ids)
        if not num_users:
            self.user_ids_rest = None
            self.next_cursor = 0
            return list()

        if num_users < 100:
            # 一回のリクエストですべてのユーザー情報が取得できる。
            ids = ','.join([str(id) for id in user_ids])
            res2 = api.users.lookup(user_id=ids, include_entities=0)
            sorted_res = self._sort_users_lookup(user_ids, res2)

            # 残りをクリア
            self.user_ids_rest = None
        else:
            # 1. 最初の 100 ユーザーだけをスライスして利用する。
            user_ids_first = user_ids[:100]
            ids = ','.join([str(id) for id in user_ids_first])
            res2 = api.users.lookup(user_id=ids, include_entities=0)
            sorted_res = self._sort_users_lookup(user_ids_first, res2)

            # 残りは次回のスクロールで利用するので、キープしておく。
            self.user_ids_rest = user_ids[100:]

        return sorted_res

    def _sort_users_lookup(self, user_ids, response):
        """
        Sorts the response from api.users.lookup with api.followers.ids
        or api.friends.ids
        """
        sorted_response = [None] * len(user_ids)
        for user in response:
            user_id = user[u'id']
            i = user_ids.index(user_id)
            sorted_response[i] = user

        return sorted_response
