# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qstatusbrowser import QStatusBrowser, StatusMetaData

HTML_CODE = u'''
<table width="100%">
  <tr>
    <td valign="top" width="50">
      <img src="{profile_image_url_https}" width="48" height="48" title="TODO"/>
    </td>
    <td>
      <b>{screen_name}</b> | <b>{name}</b><br/>{text}
    </td>
  </tr>
</table>
<hr width="100%" />
'''

class UserItemBrowser(QStatusBrowser):
    def on_load_latest_page(self, response):
        self.moveCursor(QTextCursor.Start)
        caret = QTextCursor(self.textCursor())
        for useritem in response:
            # metadata
            caret.block().setUserData(StatusMetaData(useritem))

            # HTML table
            if u'status' in useritem:
                text = HTML_CODE.format(text=useritem[u'status'][u'text'], **useritem)
            else:
                text = HTML_CODE.format(text=u'', **useritem)

            self.insertHtml(text)

        self.moveCursor(QTextCursor.Start)

    def on_load_next_page(self, response):
        self.moveCursor(QTextCursor.End)
        caret = QTextCursor(self.textCursor())
        for useritem in response:
            # metadata
            caret.block().setUserData(StatusMetaData(useritem))

            # HTML table
            if u'status' in useritem:
                text = HTML_CODE.format(text=useritem[u'status'][u'text'], **useritem)
            else:
                text = HTML_CODE.format(text=u'', **useritem)

            self.insertHtml(text)
