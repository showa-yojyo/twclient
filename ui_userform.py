# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'userform.ui'
#
# Created: Tue Jun 05 23:26:18 2012
#      by: PyQt4 UI code generator 4.8.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(500, 640)
        Dialog.setStyleSheet(_fromUtf8(""))
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setMargin(9)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.textBrowser = QStatusBrowser(Dialog)
        self.textBrowser.setOpenLinks(False)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setIconSize(QtCore.QSize(32, 32))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabTimeLine = QtGui.QWidget()
        self.tabTimeLine.setObjectName(_fromUtf8("tabTimeLine"))
        self.tabWidget.addTab(self.tabTimeLine, _fromUtf8(""))
        self.tabList = QtGui.QWidget()
        self.tabList.setObjectName(_fromUtf8("tabList"))
        self.tabWidget.addTab(self.tabList, _fromUtf8(""))
        self.tabFav = QtGui.QWidget()
        self.tabFav.setObjectName(_fromUtf8("tabFav"))
        self.tabWidget.addTab(self.tabFav, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)
        self.gridLayout.setRowStretch(1, 1)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "{screen_name} - とにかくシンプルな Twitter クライアント", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTimeLine), QtGui.QApplication.translate("Dialog", "Time-line", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabList), QtGui.QApplication.translate("Dialog", "Lists", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabFav), QtGui.QApplication.translate("Dialog", "Favorites", None, QtGui.QApplication.UnicodeUTF8))

from qstatusbrowser import QStatusBrowser
