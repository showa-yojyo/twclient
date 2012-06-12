# -*- coding: utf-8 -*-

class Collection(object):
    def __init__(self):
        self.next_cursor = 0
        self.response_chunks = []
        #self.view = None

    def update_page_info(self, response):
        if not response:
            return

        next_cursor = response[u'next_cursor']
        if next_cursor == 0 or next_cursor > self.next_cursor:
            self.next_cursor = next_cursor

    def request(self, fetch_older=True):
        next_cursor = self.pre_request(fetch_older)
        response = self.do_request(next_cursor)
        self.post_request(response, fetch_older)
        return response

    def do_request(self, next_cursor):
        assert False

    def pre_request(self, fetch_older):
        next_cursor = 0
        if self.next_cursor and fetch_older:
            next_cursor = self.next_cursor
        return next_cursor

    def post_request(self, response, fetch_older):
        self.update_page_info(response)
        # TODO: process the entire or only delta of the response.
        if fetch_older:
            self.response_chunks.append(response)
            # ...
        else:
            self.response.chunks.insert(0, response)
            # ...
