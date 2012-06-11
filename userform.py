# -*- coding: utf-8 -*-

from PyQt4 import QtCore
from PyQt4.QtGui import QDesktopServices
from PyQt4.QtGui import QDialog
from PyQt4.QtGui import QMessageBox
from ui_userform import Ui_Dialog
from twmodel.account import Account

USER_PROPERTY_HTML = u'''
<table width="100%">
  <tr>
    <td valign="top" width="{image_size}">
      <img src="{profile_image_url}" width="{image_size}" height="{image_size}" />
    </td>
    <td>
      <h1>{name}</h1>
      <h2>{location}</h2>
      {url}
      <p>{description}</p>
    </td>
  </tr>
</table>
'''

class UserForm(QDialog):
    def __init__(self, parent, users_show):
        super(UserForm, self).__init__(parent)
        self.account = Account(users_show)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        users_show = self.account.users_show
        title = unicode(self.windowTitle())
        title = title.format(screen_name=users_show['screen_name'])
        self.setWindowTitle(title)

        self.setupUserProperty()

        self.pagetable = {
            u'updates':(self.ui.stackedWidgetFollower, 0),
            u'follows':(self.ui.stackedWidgetFollower, 1),
            u'followed_by':(self.ui.stackedWidgetFollower, 2),
            u'lists':(self.ui.stackedWidgetList, 0),
            u'listed_by':(self.ui.stackedWidgetList, 1)
            }

        self.ui.textBrowserUser.anchorClicked.connect(self.onAnchorClicked)
        self.ui.textBrowserStatusUpdates.anchorClicked.connect(self.onAnchorClicked)
        self.ui.textBrowserFav.anchorClicked.connect(self.onAnchorClicked)

        self.ui.stackedWidgetFollower.currentChanged.connect(self.onStackChanged)
        self.ui.stackedWidgetList.currentChanged.connect(self.onStackChanged)

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

    def onLinkActivated(self, href):
        # changePage
        href = unicode(href)
        if href in self.pagetable:
            page, index = self.pagetable[href]
            page.setCurrentIndex(index)
            print 'setCurrentIndex', page, index

    def onStackChanged(self, index):
        print index

    def setupUserProperty(self):
        tb = self.ui.textBrowserUser
        res = self.account.users_show

        # TODO: GET users/profile_image 
        kwargs = dict(
            profile_image_url=res[u'profile_image_url_https'],
            image_size=48,
            location=res[u'location'],
            name=res[u'name'],
            description=res[u'description'])

        if res[u'url']:
            kwargs['url'] = '''<h3><a href="{url}">{url}</a></h3>'''.format(url=res['url'])
        else:
            kwargs['url'] = ''

        tb.setHtml(USER_PROPERTY_HTML.format(**kwargs))

        # Follow tab
        users_show = self.account.users_show
        format_label(self.ui.labelUpdates, updates=users_show['statuses_count'])
        format_label(self.ui.labelFollows, follows=users_show['friends_count'])
        format_label(self.ui.labelFollowedBy, followed_by=users_show['followers_count'])

def format_label(label, **kwargs):
    label.setText(unicode(label.text()).format(**kwargs))
