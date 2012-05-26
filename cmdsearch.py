# -*- coding: utf-8 -*-

from cmd import Command
from twitter import Twitter, NoAuth
import twformat

class CmdSearch(Command):
    def __init__(self, query):
        super(CmdSearch, self).__init__()
        self.query = query

    def do_execute(self, max_id):
        data = request_search(self.query, max_id)
        text = u""
        for item in data['results']:
            text += twformat.format_status(item)
        return data['results'], text

def request_search(query, max_id):
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

    return api.search(**kwargs)
