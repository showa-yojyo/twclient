# -*- coding: utf-8 -*-

from twmodel.list import List
from twmodel.usertimeline import UserTimeLine
from twmodel.search import Search

class ItemFactory(object):
    def create(self, cmdline):
        item = None
        words = cmdline.split(" ")
        if(words[0] == u"list"):
            owner_slug = words[1].split(u"/")
            item = List(owner_slug[0], owner_slug[1])

        elif(words[0] == u"user_timeline"):
            screen_name = words[1]
            item = UserTimeLine(screen_name)

        elif(words[0] == u"search"):
            query = title[len(u'search'):].strip()
            item = Search(query)

        return item
