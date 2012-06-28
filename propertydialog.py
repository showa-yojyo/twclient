# -*- coding: utf-8 -*-

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

CSS = u'''
QTableView {
background-color: white;
alternate-background-color: whitesmoke;
}
'''

class PropertyDialog(QDialog):
    def __init__(self):
        super(PropertyDialog, self).__init__()
        self.list_entity = None
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

    def setup(self, list_entity):
        self.list_entity = list_entity
        self.setupTableContents(self.ui.tableWidget)
        self.setWindowTitle(u"{full_name} プロパティー".format(**list_entity))

    def setupTableContents(self, tableWidget):
        tableWidget.clearContents()
        tableWidget.setShowGrid(False)
        tableWidget.horizontalHeader().hide()
        tableWidget.verticalHeader().hide()

        list_entity = self.list_entity
        numrow = len(list_entity)

        tableWidget.setRowCount(numrow)
        tableWidget.setColumnCount(2)

        labels = QStringList([u'プロパティー', u'値'])
        tableWidget.setHorizontalHeaderLabels(labels)

        row = 0
        height = -1
        for k, v in sorted(list_entity.iteritems()):
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

        tableWidget.setStyleSheet(CSS)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PropertyDialog()
    window.show()
    sys.exit(app.exec_())
