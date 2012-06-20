# -*- coding: utf-8 -*-

from twmodel.accountcollection import AccountCollection

class Follows(AccountCollection):
    def make_request_api(self, api):
        return api.friends.ids
