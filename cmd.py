# -*- coding: utf-8 -*-

class Command(object):
    def __init__(self):
        self.max_id = None
        self.min_id = None

    def update_page_info(self, data):
        if len(data) == 0:
            return

        max_id = data[0]['id']
        min_id = data[-1]['id']

        if self.max_id is None or max_id > self.max_id:
            self.max_id = max_id

        if self.min_id is None or min_id < self.min_id:
            self.min_id = min_id

    def execute(self):
        max_id = self.pre_execute()
        data, text = self.do_execute(max_id)
        self.post_execute(data)
        return text

    def pre_execute(self):
        max_id = None
        if self.max_id:
            max_id = self.min_id - 1
        return max_id

    def post_execute(self, data):
        self.update_page_info(data)

