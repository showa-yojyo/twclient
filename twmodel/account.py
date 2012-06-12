# -*- coding: utf-8 -*-

import twitter
from twmodel.follows import Follows
from twmodel.followed_by import FollowedBy
from twmodel.lists import Lists
from twmodel.listed_in import ListedIn
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
        self.follows = None # collection
        self.followed_by = None # collection
        self.lists = None # collection
        self.listed_in = None # collection
        self.favorites = None # timeline

    def get_screen_name(self):
        assert self.users_show
        return self.users_show[u'screen_name']

    def _request_core(self, fetch_older, collection_subclass, member):
        if member:
            collection = member
        else:
            # first time
            screen_name = self.get_screen_name()
            collection = collection_subclass(screen_name)

        try:
            collection.request(fetch_older)
        except twitter.TwitterHTTPError as e:
            print >>sys.stderr, u'{0}'.format(e.response_data)
        finally:
            if not member:
                member = collection

    def request_follows(self, fetch_older=True):
        return self._request_core(fetch_older, Follows, self.follows)

    def request_followed_by(self, fetch_older=True):
        return self._request_core(fetch_older, FollowedBy, self.followed_by)

    def request_lists(self, fetch_older=True):
        return self._request_core(fetch_older, Lists, self.lists)

    def request_listed_in(self, fetch_older=True):
        return self._request_core(fetch_older, ListedIn, self.listed_in)

    def request_favorites(self, fetch_older=True):
        return self._request_core(fetch_older, Favorites, self.favorites)
