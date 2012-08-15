# -*- coding: utf-8 -*-
u"""
Copyright (c) 2012 プレハブ小屋管理人 <yojyo@hotmail.com>
All Rights Reserved.  NO WARRANTY.
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qstatusbrowser import QStatusBrowser, StatusMetaData
from twformat import get_user_tooltip

HTML_CODE = u'''
<table width="100%">
  <tr>
    <td valign="top" width="50">
      <img src="{user[profile_image_url_https]}" width="48" height="48" title="{tooltip_html_text}"/>
    </td>
    <td>
      <span class="full_name">{full_name}</span>
      <p class="list_description">{description}</p>
    </td>
  </tr>
</table>
<hr width="100%" />
'''

class ListItemBrowser(QStatusBrowser):

    @pyqtSlot(list)
    def on_load_latest_page(self, response):
        self.moveCursor(QTextCursor.Start)
        caret = QTextCursor(self.textCursor())
        lists = response[u'lists']
        for listitem in lists:
            # metadata
            caret.block().setUserData(StatusMetaData(listitem))

            # HTML table
            text = HTML_CODE.format(
                tooltip_html_text=get_user_tooltip(listitem),
                **listitem)
            self.insertHtml(text)

        self.moveCursor(QTextCursor.Start)

    @pyqtSlot(list)
    def on_load_next_page(self, response):
        self.moveCursor(QTextCursor.End)
        caret = QTextCursor(self.textCursor())
        lists = response[u'lists']
        for listitem in lists:
            # metadata
            caret.block().setUserData(StatusMetaData(listitem))

            # HTML table
            text = HTML_CODE.format(
                tooltip_html_text=get_user_tooltip(listitem),
                **listitem)
            self.insertHtml(text)
