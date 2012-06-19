# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
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

        self.setupStatusBrowser(self.ui.textBrowserUser)
        self.setupStatusBrowser(self.ui.textBrowserStatusUpdates)
        self.setupStatusBrowser(self.ui.textBrowserFav)

        self.ui.stackedWidgetFollower.currentChanged.connect(self.onStackChangedFollower)
        self.ui.stackedWidgetList.currentChanged.connect(self.onStackChangedList)

        self.ui.tabWidget.currentChanged.connect(self.onTabChanged)
        self.onTabChanged(0)

    def onAnchorClicked(self, uri):
        mainform = self.parentWidget()
        mainform.onAnchorClicked(uri)

    def onLinkActivated(self, href):
        # changePage
        href = unicode(href)
        if href in self.pagetable:
            page, index = self.pagetable[href]
            page.setCurrentIndex(index)

    def onStackChangedFollower(self, index):
        if index == 0:
            self.setupUserTimeLineView()
        elif index == 1:
            self.setupFollowsView()
        elif index == 2:
            self.setupFollowedByView()

    def setupUserTimeLineView(self):
        if self.account.user_timeline:
            return

        self.account.request_user_timeline(self.ui.textBrowserStatusUpdates, False)

    def setupFollowsView(self):
        if self.account.follows:
            return

        listWidget = self.ui.listWidgetFollows
        listWidget.setupGui()
        self.account.request_follows(listWidget, False)

    def setupFollowedByView(self):
        if self.account.followed_by:
            return

        listWidget = self.ui.listWidgetFollowedBy
        listWidget.setupGui()
        self.account.request_followed_by(listWidget, False)

    def setupListsView(self):
        if self.account.lists:
            return

        listWidget = self.ui.listWidgetLists
        listWidget.setupGui()
        self.account.request_lists(listWidget, False)

    def setupListedInView(self):
        if self.account.listed_in:
            return

        listWidget = self.ui.listWidgetListedBy
        listWidget.setupGui()
        self.account.request_listed_in(listWidget, False)

    def onStackChangedList(self, index):
        if index == 0:
            self.setupListsView()
        elif index == 1:
            self.setupListedInView()

    def onTabChanged(self, index):
        acc = self.account
        if index == 0:
            # Follows/Followed-by tab
            if not acc.user_timeline and not acc.follows and not acc.followed_by:
                # いずれもリクエストしたことがない状態。
                # 一番左のラベルに対応するビューを埋める。
                self.onStackChangedFollower(0)

        elif index == 1:
            # List tab
            if not acc.lists and not acc.listed_in:
                # どちらともリクエストしていない。
                # 左側のリストをリクエストすることにする。
                self.onStackChangedList(0)

        elif index == 2 and not acc.favorites:
            # Favorites tab
            acc.request_favorites(self.ui.textBrowserFav, False)

    def setupStatusBrowser(self, tb):
        tb.anchorClicked.connect(self.onAnchorClicked)

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
        format_label(self.ui.labelListedBy, listed_by=users_show['listed_count'])

def format_label(label, **kwargs):
    label.setText(unicode(label.text()).format(**kwargs))
