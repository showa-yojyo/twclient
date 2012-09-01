# -*- coding: utf-8 -*-
# Copyright (c) 2012 プレハブ小屋 <yojyo@hotmail.com>
# All Rights Reserved.  NO WARRANTY.

from twmodel.accountcollection import AccountCollection

class Follows(AccountCollection):
    def make_request_api(self, api):
        return api.friends.ids
