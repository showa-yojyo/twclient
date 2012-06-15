# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui_userform import Ui_Dialog
from twmodel.account import Account

# TODO: 共通化
CACHE_PATH = r'.\cache'

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

        self.ui.tabWidget.currentChanged.connect(self.onTabChanged)

        self.ui.stackedWidgetFollower.currentChanged.connect(self.onStackChangedFollower)
        self.ui.stackedWidgetList.currentChanged.connect(self.onStackChangedList)

    def onAnchorClicked(self, uri):
        self.parentWidget().onAnchorClicked(uri)

    def onLinkActivated(self, href):
        # changePage
        href = unicode(href)
        if href in self.pagetable:
            page, index = self.pagetable[href]
            page.setCurrentWidget(page.widget(index))

    def onStackChangedFollower(self, index):
        if index == 0:
            listWidget = None
        elif index == 1:
            listWidget = self.ui.listWidgetFollows
        elif index == 2:
            listWidget = self.ui.listWidgetFollowedBy

        if listWidget and listWidget.count() > 0:
            # TODO: あとで実装する？
            return

        if index == 0:
            # TODO: user_timeline
            pass
        elif index == 1:
            self.account.request_follows(False)
            resall = self.account.follows.response_chunks
        elif index == 2:
            self.account.request_followed_by(False)
            resall = self.account.followed_by.response_chunks

        listWidget.setIconSize(QSize(48, 48))
        listWidget.setSortingEnabled(False)
        #listWidget.setWordWrap(True)
        icon = QIcon()
        icon.addPixmap(QPixmap(u":/resource/illvelo-32x32.png"))

        for res in resall:
            for user in res:
                item = QListWidgetItem(listWidget)
                item.setIcon(icon)
                item.setText(u'{screen_name} | {name}\n{status[text]}'.format(**user))
                if listWidget.count() % 2 == 0:
                    color = QColor(u'whitesmoke')
                else:
                    color = QColor(u'white')
                item.setBackgroundColor(color)

    def onStackChangedList(self, index):
        if index == 0:
            listWidget = self.ui.listWidgetLists
        elif index == 1:
            listWidget = self.ui.listWidgetListedBy

        if listWidget.count() > 0:
            # TODO: あとで実装する？
            return

        if index == 0:
            self.account.request_lists(False)
            resall = self.account.lists.response_chunks
        elif index == 1:
            self.account.request_listed_in(False)
            resall = self.account.listed_in.response_chunks

        listWidget.setIconSize(QSize(48, 48))
        listWidget.setSortingEnabled(False)
        #listWidget.setWordWrap(True)
        icon = QIcon()
        icon.addPixmap(QPixmap(u":/resource/illvelo-32x32.png"))

        numlist = 0
        for res in resall:
            numlist += len(res[u'lists'])
            for list in res[u'lists']:
                item = QListWidgetItem(listWidget)
                item.setIcon(icon)
                item.setText(u'{full_name}\n{description}'.format(**list))
                if listWidget.count() % 2 == 0:
                    color = QColor(u'whitesmoke')
                else:
                    color = QColor(u'white')
                item.setBackgroundColor(color)

    def onTabChanged(self, index):
        if index == 0:
            # Follows/Followed-by tab
            pass
        elif index == 1:
            # List tab
            pass
        elif index == 2 and not self.account.favorites:
            # Favorites tab
            self.account.request_favorites(self.ui.textBrowserFav, False)

    def setupStatusBrowser(self, tb):
        tb.anchorClicked.connect(self.onAnchorClicked)
        tb.cache_path = CACHE_PATH

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
