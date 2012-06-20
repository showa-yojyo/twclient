# -*- coding: utf-8 -*-

from twmodel.accountcollection import AccountCollection

class FollowedBy(AccountCollection):
    def make_request_api(self, api):
        return api.followers.ids
