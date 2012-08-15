# -*- coding: utf-8 -*-
u"""
Copyright (c) 2012 プレハブ小屋管理人 <yojyo@hotmail.com>
All Rights Reserved.  NO WARRANTY.
"""

from twmodel.accountcollection import AccountCollection

class FollowedBy(AccountCollection):
    def make_request_api(self, api):
        return api.followers.ids
