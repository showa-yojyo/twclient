# -*- coding: utf-8 -*-

from PyQt4 import QtCore
from PyQt4.QtGui import QDesktopServices
from PyQt4.QtGui import QDialog
from PyQt4.QtGui import QMessageBox
from ui_userform import Ui_Dialog

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
    def __init__(self, parent, response):
        super(UserForm, self).__init__(parent)
        self.response = response
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        title = unicode(self.windowTitle())
        title = title.format(screen_name=self.response['screen_name'])
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
        res = self.response

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
        format_label(self.ui.labelFollows, follows=self.response['friends_count'])
        format_label(self.ui.labelFollowedBy, followed_by=self.response['followers_count'])

def format_label(label, **kwargs):
    label.setText(unicode(label.text()).format(**kwargs))
