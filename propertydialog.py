# -*- coding: utf-8 -*-
# Copyright (c) 2012 プレハブ小屋 <yojyo@hotmail.com>
# All Rights Reserved.  NO WARRANTY.

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui_propertydialog import Ui_Dialog

DEMODATA = {u'created_at': u'Tue Apr 17 15:55:49 +0000 2012',
            u'description': u'Accounts that follow me except bots and news',
            u'following': False,
            u'full_name': u'@showa_yojyo/followed-by',
            u'id': 69069899,
            u'id_str': u'69069899',
            u'member_count': 5,
            u'mode': u'public',
            u'name': u'followed-by',
            u'slug': u'followed-by',
            u'subscriber_count': 0,
            u'uri': u'/showa_yojyo/followed-by',}

class PropertyDialog(QDialog):
    def __init__(self):
        super(PropertyDialog, self).__init__()
        self.twitter_entity = None
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

    def setup(self, twitter_entity):
        self.twitter_entity = twitter_entity
        self.setupTableContents(self.ui.tableWidget)
        if u'full_name' in twitter_entity:
            # List
            title = u"{full_name} プロパティー".format(**twitter_entity)
        elif u'source' in twitter_entity:
            # Status (a.k.a. tweet)
            title = u"ツイート {id_str} プロパティー".format(**twitter_entity)

        self.setWindowTitle(title)

    def setupTableContents(self, tableWidget):
        tableWidget.clearContents()
        tableWidget.setShowGrid(False)
        tableWidget.horizontalHeader().hide()
        tableWidget.verticalHeader().hide()

        twitter_entity = self.twitter_entity
        numrow = len(twitter_entity)

        tableWidget.setRowCount(numrow)
        tableWidget.setColumnCount(2)

        labels = QStringList([u'プロパティー', u'値'])
        tableWidget.setHorizontalHeaderLabels(labels)

        row = 0
        height = -1
        for k, v in sorted(twitter_entity.iteritems()):
            tooltiptext = u"<b>{key}</b> {value}".format(key=k, value=v)

            item = QTableWidgetItem(k)
            item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            fnt = item.font()
            fnt.setBold(True)
            if height == -1:
                height = QFontMetrics(fnt).height()
            item.setFont(fnt)
            item.setToolTip(tooltiptext)
            tableWidget.setItem(row, 0, item)

            item = QTableWidgetItem(u'{0}'.format(v))
            item.setToolTip(tooltiptext)
            tableWidget.setItem(row, 1, item)
            row += 1

        if True:
            tableWidget.verticalHeader().setDefaultSectionSize(height + 4)
        else:
            tableWidget.resizeRowsToContents()

        if True:
            tableWidget.resizeColumnsToContents()
        else:
            #width = tableWidget.width() / 2
            width = self.width() / 3
            tableWidget.setColumnWidth(0, width)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    try:
        with open('client.css', 'r') as fin:
            css = fin.read()
            app.setStyleSheet(css)
    except:
        print >>sys.stderr, "WARNING client.css not read"

    window = PropertyDialog()
    window.setup(DEMODATA)
    window.show()
    sys.exit(app.exec_())
