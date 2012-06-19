# -*- coding: utf-8 -*-

import sys
from PyQt4.QtGui import QListWidget

class QStatusStreamListWidget(QListWidget):
    def on_load_latest_page(self, response):
        # TODO
        print 'on_load_latest_page'

    def on_load_next_page(self, response):
        # TODO
        print 'on_load_next_page'
