# -*- coding: utf-8 -*-

from twmodel.statusstream import StatusStream

class Collection(StatusStream):
    def __init__(self, parent=None):
        super(Collection, self).__init__(parent)
        self.next_cursor = -1
        self.response_chunks = []

    def update_page_info(self, response):
        if not response:
            self.next_cursor = 0
            return

        self.next_cursor = response[u'next_cursor']

    def request(self, fetch_older=True):
        next_cursor = self.pre_request(fetch_older)
        response = None
        if next_cursor != 0: # -1 or >0
            response = self.do_request(next_cursor)

        self.post_request(response, fetch_older)
        return response

    def do_request(self, next_cursor):
        assert False

    def pre_request(self, fetch_older):
        if fetch_older:
            next_cursor = self.next_cursor
        else:
            next_cursor = -1
        return next_cursor

    def post_request(self, response, fetch_older):
        if fetch_older:
            self.update_page_info(response)
        elif self.next_cursor == -1: # first time
            self.update_page_info(response)

        if response:
            if fetch_older:
                self.response_chunks.append(response)
            else:
                self.response_chunks.insert(0, response)

        self.notify_observers(response, fetch_older)
