# -*- coding: utf-8 -*-

import traceback
from cStringIO import StringIO

from cmdlist import CmdList
from cmdusertimeline import CmdUserTimeLine
from cmdsearch import CmdSearch

class CommandInvoker(object):
    def __init__(self, view):
        self.view = view
        self.current_command = None

    def request(self, cmdline):
        view = self.view

        words = cmdline.split(" ")
        cmd = None
        try:
            if(words[0] == u"list"):
                owner_slug = words[1].split(u"/")
                cmd = CmdList(owner_slug[0], owner_slug[1])

            elif(words[0] == u"user_timeline"):
                screen_name = words[1]
                cmd = CmdUserTimeLine(screen_name)

            elif(words[0] == u"search"):
                query = cmdline[len(u'search'):].strip()
                cmd = CmdSearch(query)

            else:
                pass

            if cmd:
                text = cmd.execute()
                view.insertHtml(text)
            else:
                view.clear()

        except Exception as e:
            buf = StringIO()
            traceback.print_exc(file=buf)
            view.setText(u'%s' % buf.getvalue())
            buf.close()

        finally:
            self.current_command = cmd

    def request_next_page(self):
        cmd = self.current_command
        if cmd is None:
            return

        view = self.view
        try:
            text = cmd.execute_next_page()
            view.insertHtml(text)

        except Exception as e:
            buf = StringIO()
            traceback.print_exc(file=buf)
            view.setText(u'%s' % buf.getvalue())
            buf.close()
        finally:
            pass
