# -*- coding: utf-8 -*-
# Copyright (c) 2012 プレハブ小屋 <yojyo@hotmail.com>
# All Rights Reserved.  NO WARRANTY.

from twmodel.timeline import TimeLine
from twitter import Twitter, NoAuth

class Search(TimeLine):
    def __init__(self, query, parent=None):
        super(Search, self).__init__(parent)
        self.query = query

    def do_request(self, max_id, min_id):
        response = request_search(self.query, max_id, min_id)
        return response['results']

def request_search(query, max_id, min_id):
    auth = NoAuth()
    api = Twitter(auth=auth, domain="search.twitter.com")

    kwargs = dict(
        q=query.encode('utf-8'),
        rpp=20,
        page=1,
        include_entities=1,
        #result_type='recent',
        result_type='mixed',
        show_user=1,)

    if max_id is not None:
        kwargs['max_id'] = max_id
    if min_id is not None:
        kwargs['since_id'] = min_id

    return api.search(**kwargs)
