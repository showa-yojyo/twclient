# -*- coding: utf-8 -*-
# Copyright (c) 2012 プレハブ小屋 <yojyo@hotmail.com>
# All Rights Reserved.  NO WARRANTY.

from twmodel.statusstream import StatusStream

class TimeLine(StatusStream):
    def __init__(self, parent=None):
        super(TimeLine, self).__init__(parent)
        self.max_id = None
        self.min_id = None
        self.response_chunks = []

    def update_page_info(self, response):
        if len(response) == 0:
            return

        max_id = response[0]['id']
        min_id = response[-1]['id']

        if self.max_id is None or max_id > self.max_id:
            self.max_id = max_id

        if self.min_id is None or min_id < self.min_id:
            self.min_id = min_id

    # request の利用状況
    # 
    # 1. 完全にゼロの状態からタイムラインを取得する。
    # 2. 取得済みタイムラインを保持した状態で、より古いタイムラインを取得する。
    # 3. 取得済みタイムラインを保持した状態で、最新のタイムラインを取得する。
    # 
    # 2. のケースでは max_id を、
    # 3. のケースでは min_id を Twitter API に指示する必要がある。
    def request(self, fetch_older=True):
        max_id, min_id = self.pre_request(fetch_older)
        response = self.do_request(max_id, min_id)
        self.post_request(response, fetch_older)
        return response

    def do_request(self, max_id, min_id):
        assert False

    def pre_request(self, fetch_older):
        max_id, min_id = None, None
        if self.max_id:
            if fetch_older:
                max_id = self.min_id - 1
            else:
                min_id = self.max_id

        return max_id, min_id

    def post_request(self, response, fetch_older):
        self.update_page_info(response)
        if fetch_older:
            self.response_chunks.append(response)
        else:
            self.response_chunks.insert(0, response)

        self.notify_observers(response, fetch_older)

