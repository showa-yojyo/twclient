# -*- coding: utf-8 -*-
# Copyright (c) 2012 プレハブ小屋 <yojyo@hotmail.com>
# All Rights Reserved.  NO WARRANTY.

import sys
import twitter
from twmodel.usertimeline import UserTimeLine
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

    def request_user_timeline(self, view, fetch_older=True):
        if not self.user_timeline:
            self.user_timeline = UserTimeLine(self.get_screen_name())
            self.user_timeline.add_observer(view)

        response, collection = self._request_core(view, fetch_older, UserTimeLine, self.user_timeline)
        if collection:
            self.user_timeline = collection
        return response

    def _request_core(self, view, fetch_older, collection_subclass, member):
        if member:
            collection = member
        else:
            # first time
            screen_name = self.get_screen_name()
            collection = collection_subclass(screen_name)
            collection.add_observer(view)

        try:
            response = collection.request(fetch_older)
        except twitter.TwitterHTTPError as e:
            print >>sys.stderr, u'{0}'.format(e.response_data)
        finally:
            if member:
                collection = None

        return response, collection

    def request_follows(self, view, fetch_older=True):
        response, collection = self._request_core(view, fetch_older, Follows, self.follows)
        if collection:
            self.follows = collection
        return response

    def request_followed_by(self, view, fetch_older=True):
        response, collection = self._request_core(view, fetch_older, FollowedBy, self.followed_by)
        if collection:
            self.followed_by = collection
        return response

    def request_lists(self, view, fetch_older=True):
        response, collection = self._request_core(view, fetch_older, Lists, self.lists)
        if collection:
            self.lists = collection
        return response

    def request_listed_in(self, view, fetch_older=True):
        response, collection = self._request_core(view, fetch_older, ListedIn, self.listed_in)
        if collection:
            self.listed_in = collection
        return response

    def request_favorites(self, view, fetch_older=True):
        if not self.favorites:
            self.favorites = Favorites(self.get_screen_name())
            self.favorites.add_observer(view)

        response, collection = self._request_core(view, fetch_older, Favorites, self.favorites)
        if collection:
            self.favorites = collection
        return response
