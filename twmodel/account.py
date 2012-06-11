# -*- coding: utf-8 -*-

import twitter
from twmodel.favorites import Favorites

# A Twitter user:
# * basic information (users/show)
# * status updates (statuses/user_timeline)
# * follows and friends (friends/ids, followers/ids)
# * lists (lists, lists/membership)
# * favorites (favorites)
class Account(object):
    def __init__(self, users_show):
        self.users_show = users_show # obtained from ShowUser.execute
        self.user_timeline = None # timeline
        self.follows = None
        self.followed_by = None
        self.lists = None
        self.listed_in = None
        self.favorites = None # timeline

    def get_screen_name(self):
        assert self.users_show
        return self.users_show[u'screen_name']

    def request_favorites(self, fetch_older=True):
        if self.favorites:
            fav = self.favorites
        else:
            # first time
            screen_name = self.get_screen_name()
            fav = Favorites(screen_name)

        try:
            fav.request(fetch_older)
        except twitter.TwitterHTTPError as e:
            print >>sys.stderr, u'{0}'.format(e.response_data)
        finally:
            if not self.favorites:
                self.favorites = fav
