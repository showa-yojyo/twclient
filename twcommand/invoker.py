# -*- coding: utf-8 -*-

import sys
import Queue
import threading
import logging

class CommandInvoker(object):
    def __init__(self):
        self.queue = Queue.Queue()
        self.thread = threading.Thread(target=self.worker)
        self.setup_logger()

    def setup_logger(self):
        self.logger = logging.getLogger('CommandInvoker')
        self.logger.setLevel(logging.DEBUG)

        ch = logging.StreamHandler()
        formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

    def start(self):
        self.thread.setDaemon(True)
        self.thread.start()
        self.logger.debug('Start')

    def worker(self):
        queue = self.queue
        while True:
            cmd = queue.get()
            try:
                self.logger.debug('command {0} starts'.format(cmd))
                cmd.execute()

            except Exception as e:
                self.logger.error('{0}'.format(e))
                buf = StringIO()
                traceback.print_exc(file=sys.stderr)
                buf.close()
            finally:
                queue.task_done()
                self.logger.debug('command {0} finished'.format(cmd))

    def store_command(self, cmd):
        if True:
            self.logger.debug('store {0}'.format(cmd))
            self.queue.put(cmd)
        else:
            cmd.execute()
