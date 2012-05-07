# -*- coding: utf-8 -*-

class Command(object):
    def __init__(self):
        self.max_id = None
        self.min_id = None

    def update_page_info(self, data):
        max_id = data[0]['id']
        min_id = data[-1]['id']

        if self.max_id is None or max_id > self.max_id:
            self.max_id = max_id

        if self.min_id is None or min_id < self.min_id:
            self.min_id = min_id

    def execute(self):
        pass

    def execute_next_page(self):
        pass
