# -*- coding: utf-8 -*-

import traceback
from cStringIO import StringIO
import twformat

class CommandInvoker(object):
    def __init__(self):
        pass

    def invoke_command(self, cmdline, view):
        words = cmdline.split(" ")
        text = u""

        try:
            if(words[0] == u"list"):
                owner_slug = words[1].split(u"/")
                data = twformat.request_lists_statuses(owner_slug[0], owner_slug[1])

                for item in data:
                    text += twformat.format_status(item)

            elif(words[0] == u"user_timeline"):
                screen_name = words[1]
                data = twformat.request_statuses_user_timeline(screen_name)

                text = u""
                for item in data:
                    text += twformat.format_status(item)

            elif(words[0] == u"search"):
                query = cmdline[len(u'search'):].strip()
                data = twformat.request_search(query)

                text = u""
                for item in data['results']:
                    text += twformat.format_search_result(item)

            if text:
                view.insertHtml(text)
            else:
                view.clear()

        except Exception as e:
            buf = StringIO()
            traceback.print_exc(file=buf)
            view.setText(u'%s' % buf.getvalue())
            buf.close()

