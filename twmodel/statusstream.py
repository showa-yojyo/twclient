# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from twitter import TwitterResponse

class StatusStream(QObject):

    nextPageLoaded = pyqtSignal(object)
    latestPageLoaded = pyqtSignal(object)

    def __init__(self, parent=None):
        super(StatusStream, self).__init__(parent)

    def add_observer(self, observer):
        assert observer
        self.nextPageLoaded.connect(observer.on_load_next_page)
        self.latestPageLoaded.connect(observer.on_load_latest_page)

    def remove_observer(self, observer):
        self.nextPageLoaded.disconnect(observer.on_load_next_page)
        self.latestPageLoaded.disconnect(observer.on_load_latest_page)

    def notify_observers(self, response, fetch_older):
        if not response:
            return

        if fetch_older:
            self.nextPageLoaded.emit(response)
        else:
            self.latestPageLoaded.emit(response)
