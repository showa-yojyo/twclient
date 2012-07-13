# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qstatusbrowser import QStatusBrowser, StatusMetaData
from twformat import get_user_tooltip

HTML_CODE = u'''
<table width="100%">
  <tr>
    <td valign="top" width="50">
      <img src="{profile_image_url_https}" width="48" height="48" title="{tooltip_html_text}"/>
    </td>
    <td>
      <span class="screen_name">{screen_name}</span> | <span class="name">{name}</span>
      <p class="useritem_text">{text}</p>
    </td>
  </tr>
</table>
<hr width="100%" />
'''

class UserItemBrowser(QStatusBrowser):

    @pyqtSlot(list)
    def on_load_latest_page(self, response):
        self.moveCursor(QTextCursor.Start)
        caret = QTextCursor(self.textCursor())
        for useritem in response:
            # metadata
            caret.block().setUserData(StatusMetaData(useritem))

            # HTML table
            if u'status' in useritem:
                text = HTML_CODE.format(
                    text=useritem[u'status'][u'text'],
                    tooltip_html_text=get_user_tooltip(useritem),
                    **useritem)
            else:
                text = HTML_CODE.format(
                    text=u'',
                    
                    **useritem)

            self.insertHtml(text)

        self.moveCursor(QTextCursor.Start)

    @pyqtSlot(list)
    def on_load_next_page(self, response):
        self.moveCursor(QTextCursor.End)
        caret = QTextCursor(self.textCursor())
        for useritem in response:
            # metadata
            caret.block().setUserData(StatusMetaData(useritem))

            # HTML table
            if u'status' in useritem:
                text = HTML_CODE.format(
                    text=useritem[u'status'][u'text'], 
                    tooltip_html_text=get_user_tooltip(useritem),
                    **useritem)
            else:
                text = HTML_CODE.format(
                    text=u'',
                    tooltip_html_text=get_user_tooltip(useritem),
                    **useritem)

            self.insertHtml(text)
