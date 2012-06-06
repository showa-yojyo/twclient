# -*- coding: utf-8 -*-

from PyQt4 import QtCore
from PyQt4.QtGui import QDesktopServices
from PyQt4.QtGui import QDialog
from PyQt4.QtGui import QMessageBox
from ui_userform import Ui_Dialog

USER_PROPERTY_HTML = u'''
<table width="100%">
  <tr>
    <td valign="top" width="130">
      <img src="{profile_image_url}" width="{image_size}" height="{image_size}" />
    </td>
    <td>
      <h1>{name}</h1>
      <h2>{location}</h2>
      <h3><a href="{url}">{url}</a></h3>
      <p>{description}</p>
    </td>
  </tr>
</table>
'''

class UserForm(QDialog):
    def __init__(self, parent, screen_name):
        super(UserForm, self).__init__(parent)
        self.screen_name = screen_name
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        title = unicode(self.windowTitle())
        title = title.format(screen_name=self.screen_name)
        self.setWindowTitle(title)

        self.setupUserProperty()

        self.pagetable = {
            u'{follows}':(self.ui.stackedWidgetFollower, 0),
            u'{followed-by}':(self.ui.stackedWidgetFollower, 1),
            u'{lists}':(self.ui.stackedWidgetList, 0),
            u'{listed-by}':(self.ui.stackedWidgetList, 1)
            }

        tb = self.ui.textBrowser
        QtCore.QObject.connect(
            tb, QtCore.SIGNAL(u"anchorClicked(QUrl)"), self.onAnchorClicked)

    def onAnchorClicked(self, hottext):
        path = unicode(hottext.toString())

        if path.startswith(u'chrome://hashtag/'):
            # hash tag
            QMessageBox.information(self, u"Twitter Search", u"TODO: Display Hash tag '%s'" % path)
        elif path.startswith(u'chrome://user_mention'):
            # screen_name
            QMessageBox.information(self, u"User Property", u"TODO: Display %s's user_timeline" % path[1:])
        else:
            # general URL
            QDesktopServices.openUrl(hottext)

    def onLinkActivated(self, hottext):
        # changePage
        if hottext in self.pagetable:
            page, index = pagetable[hottext]
            page.setCurrentIndex(index)

    def setupUserProperty(self):
        tb = self.ui.textBrowser

        kwargs = dict(
            profile_image_url=u'dummy',
            image_size=128,
            name=u'プレハブ小屋',
            location=u'東京都区内',
            url=u'http://www.geocities.jp/showa_yojyo/',
            description=u'実は電子の世界の人で現実には存在しない。')
        
        tb.setHtml(USER_PROPERTY_HTML.format(**kwargs))
