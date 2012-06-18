# -*- coding: utf-8 -*-

class StatusStream(object):
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        if not observer in self.observers:
            self.observers.append(observer)

    def remove_observer(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def notify_observers(self, response, fetch_older):
        if fetch_older:
            for observer in self.observers:
                observer.on_load_next_page(response)
        else:
            for observer in self.observers:
                observer.on_load_latest_page(response)
