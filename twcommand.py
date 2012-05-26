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
        self.command_cache = dict()

    def request(self, cmdline, fetch_older):
        view = self.view
        cmd = None
        if cmdline in self.command_cache:
            cmd = self.command_cache[cmdline]

        try:
            if not cmd:
                #assert fetch_older
                words = cmdline.split(" ")
                if(words[0] == u"list"):
                    owner_slug = words[1].split(u"/")
                    cmd = CmdList(owner_slug[0], owner_slug[1])

                elif(words[0] == u"user_timeline"):
                    screen_name = words[1]
                    cmd = CmdUserTimeLine(screen_name)

                elif(words[0] == u"search"):
                    query = cmdline[len(u'search'):].strip()
                    cmd = CmdSearch(query)

                if cmd:
                    text = cmd.execute(fetch_older)
                    self.command_cache[cmdline] = cmd
            else:
                # Reuse cmd.textall
                assert not fetch_older
                cmd.execute(False)
                text = cmd.textall

            if text:
                view.setHtml(text)
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
            text = cmd.execute(True)
            view.insertHtml(text)

        except Exception as e:
            buf = StringIO()
            traceback.print_exc(file=buf)
            view.setText(u'%s' % buf.getvalue())
            buf.close()
        finally:
            pass
