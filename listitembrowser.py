# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qstatusbrowser import QStatusBrowser, StatusMetaData

HTML_CODE = u'''
<table width="100%">
  <tr>
    <td valign="top" width="50">
      <img src="{user[profile_image_url_https]}" width="48" height="48" title="TODO"/>
    </td>
    <td>
      <b>{full_name}</b><br/>{description}
    </td>
  </tr>
</table>
<hr width="100%" />
'''

class ListItemBrowser(QStatusBrowser):
    def on_load_latest_page(self, response):
        self.moveCursor(QTextCursor.Start)
        caret = QTextCursor(self.textCursor())
        lists = response[u'lists']
        for listitem in lists:
            # metadata
            caret.block().setUserData(StatusMetaData(listitem))

            # HTML table
            text = HTML_CODE.format(**listitem)
            self.insertHtml(text)

        self.moveCursor(QTextCursor.Start)

    def on_load_next_page(self, response):
        self.moveCursor(QTextCursor.End)
        caret = QTextCursor(self.textCursor())
        lists = response[u'lists']
        for listitem in lists:
            # metadata
            caret.block().setUserData(StatusMetaData(listitem))

            # HTML table
            text = HTML_CODE.format(**listitem)
            self.insertHtml(text)
