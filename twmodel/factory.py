# -*- coding: utf-8 -*-
# Copyright (c) 2012 プレハブ小屋 <yojyo@hotmail.com>
# All Rights Reserved.  NO WARRANTY.

from twmodel.list import List
from twmodel.usertimeline import UserTimeLine
from twmodel.search import Search
from twmodel.favorites import Favorites
#from twmodel.follows import Follows
#from twmodel.followed_by import FollowedBy
#from twmodel.lists import Lists
#from twmodel.listed_in import ListedIn
from twmodel.dummy import DummyTimeLine

class ItemFactory(object):

    def __init__(self, parent):
        # self.parent should be used for new QObject instances
        self.parent = parent

    def create(self, cmdline):
        item = None
        words = cmdline.split(" ")
        command_name = words[0]
        if(command_name == u"list"):
            owner_slug = words[1].split(u"/")
            item = List(owner_slug[0], owner_slug[1], self.parent)

        elif(command_name == u"user_timeline"):
            screen_name = words[1]
            item = UserTimeLine(screen_name, self.parent)

        elif(command_name == u"search"):
            query = cmdline[len(u'search'):].strip()
            item = Search(query, self.parent)

        elif(command_name == u"favorites"):
            # favorites screen_name
            screen_name = words[1]
            item = Favorites(screen_name, self.parent)

        #elif(command_name == u"lists"):
        #    screen_name = words[1]
        #    item = Lists(screen_name, self.parent)
        #elif(command_name in u"listed-in"):
        #    screen_name = words[1]
        #    item = ListedIn(screen_name, self.parent)
        #elif(command_name in u"follows"):
        #    screen_name = words[1]
        #    item = Follows(screen_name, self.parent)
        #elif(command_name in u"followed-by"):
        #    screen_name = words[1]
        #    item = FollowedBy(screen_name, self.parent)

        elif(command_name == u"dummy_timeline"):
            item = DummyTimeLine(self.parent)

        return item
