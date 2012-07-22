# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'userform.ui'
#
# Created: Sun Jul 22 22:25:14 2012
#      by: PyQt4 UI code generator 4.9.1
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
        Dialog.resize(450, 600)
        Dialog.setStyleSheet(_fromUtf8(""))
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setMargin(9)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.textBrowserUser = QStatusBrowser(Dialog)
        self.textBrowserUser.setOpenLinks(False)
        self.textBrowserUser.setObjectName(_fromUtf8("textBrowserUser"))
        self.gridLayout.addWidget(self.textBrowserUser, 0, 0, 1, 1)
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setIconSize(QtCore.QSize(32, 32))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabFollow = QtGui.QWidget()
        self.tabFollow.setObjectName(_fromUtf8("tabFollow"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tabFollow)
        self.verticalLayout_2.setContentsMargins(0, -1, 0, 0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.labelUpdates = QtGui.QLabel(self.tabFollow)
        self.labelUpdates.setObjectName(_fromUtf8("labelUpdates"))
        self.horizontalLayout.addWidget(self.labelUpdates)
        self.labelFollows = QtGui.QLabel(self.tabFollow)
        self.labelFollows.setObjectName(_fromUtf8("labelFollows"))
        self.horizontalLayout.addWidget(self.labelFollows)
        self.labelFollowedBy = QtGui.QLabel(self.tabFollow)
        self.labelFollowedBy.setObjectName(_fromUtf8("labelFollowedBy"))
        self.horizontalLayout.addWidget(self.labelFollowedBy)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.stackedWidgetFollower = QtGui.QStackedWidget(self.tabFollow)
        self.stackedWidgetFollower.setObjectName(_fromUtf8("stackedWidgetFollower"))
        self.pageStatusUpdates = QtGui.QWidget()
        self.pageStatusUpdates.setObjectName(_fromUtf8("pageStatusUpdates"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.pageStatusUpdates)
        self.verticalLayout_8.setMargin(0)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.textBrowserStatusUpdates = QStatusBrowser(self.pageStatusUpdates)
        self.textBrowserStatusUpdates.setOpenLinks(False)
        self.textBrowserStatusUpdates.setObjectName(_fromUtf8("textBrowserStatusUpdates"))
        self.verticalLayout_8.addWidget(self.textBrowserStatusUpdates)
        self.stackedWidgetFollower.addWidget(self.pageStatusUpdates)
        self.pageFollows = QtGui.QWidget()
        self.pageFollows.setObjectName(_fromUtf8("pageFollows"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.pageFollows)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.textBrowserFollows = UserItemBrowser(self.pageFollows)
        self.textBrowserFollows.setOpenLinks(False)
        self.textBrowserFollows.setObjectName(_fromUtf8("textBrowserFollows"))
        self.verticalLayout_3.addWidget(self.textBrowserFollows)
        self.stackedWidgetFollower.addWidget(self.pageFollows)
        self.pageFollowedBy = QtGui.QWidget()
        self.pageFollowedBy.setObjectName(_fromUtf8("pageFollowedBy"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.pageFollowedBy)
        self.verticalLayout_6.setMargin(0)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.textBrowserFollowedBy = UserItemBrowser(self.pageFollowedBy)
        self.textBrowserFollowedBy.setOpenLinks(False)
        self.textBrowserFollowedBy.setObjectName(_fromUtf8("textBrowserFollowedBy"))
        self.verticalLayout_6.addWidget(self.textBrowserFollowedBy)
        self.stackedWidgetFollower.addWidget(self.pageFollowedBy)
        self.verticalLayout_2.addWidget(self.stackedWidgetFollower)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/resource/followers.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tabFollow, icon, _fromUtf8(""))
        self.tabList = QtGui.QWidget()
        self.tabList.setObjectName(_fromUtf8("tabList"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tabList)
        self.verticalLayout_5.setContentsMargins(0, -1, 0, 0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.labelLists = QtGui.QLabel(self.tabList)
        self.labelLists.setObjectName(_fromUtf8("labelLists"))
        self.horizontalLayout_2.addWidget(self.labelLists)
        self.labelListedBy = QtGui.QLabel(self.tabList)
        self.labelListedBy.setObjectName(_fromUtf8("labelListedBy"))
        self.horizontalLayout_2.addWidget(self.labelListedBy)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.stackedWidgetList = QtGui.QStackedWidget(self.tabList)
        self.stackedWidgetList.setObjectName(_fromUtf8("stackedWidgetList"))
        self.pageLists = QtGui.QWidget()
        self.pageLists.setObjectName(_fromUtf8("pageLists"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.pageLists)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.textBrowserLists = ListItemBrowser(self.pageLists)
        self.textBrowserLists.setOpenLinks(False)
        self.textBrowserLists.setObjectName(_fromUtf8("textBrowserLists"))
        self.verticalLayout_4.addWidget(self.textBrowserLists)
        self.stackedWidgetList.addWidget(self.pageLists)
        self.pageListedBy = QtGui.QWidget()
        self.pageListedBy.setObjectName(_fromUtf8("pageListedBy"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.pageListedBy)
        self.verticalLayout_7.setMargin(0)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.textBrowserListedBy = ListItemBrowser(self.pageListedBy)
        self.textBrowserListedBy.setOpenLinks(False)
        self.textBrowserListedBy.setObjectName(_fromUtf8("textBrowserListedBy"))
        self.verticalLayout_7.addWidget(self.textBrowserListedBy)
        self.stackedWidgetList.addWidget(self.pageListedBy)
        self.verticalLayout_5.addWidget(self.stackedWidgetList)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/resource/lists.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tabList, icon1, _fromUtf8(""))
        self.tabFav = QtGui.QWidget()
        self.tabFav.setObjectName(_fromUtf8("tabFav"))
        self.verticalLayout = QtGui.QVBoxLayout(self.tabFav)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.textBrowserFav = QStatusBrowser(self.tabFav)
        self.textBrowserFav.setOpenLinks(False)
        self.textBrowserFav.setObjectName(_fromUtf8("textBrowserFav"))
        self.verticalLayout.addWidget(self.textBrowserFav)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/resource/favorites.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tabFav, icon2, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)
        self.gridLayout.setRowStretch(1, 1)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        self.stackedWidgetFollower.setCurrentIndex(0)
        self.stackedWidgetList.setCurrentIndex(0)
        QtCore.QObject.connect(self.labelFollows, QtCore.SIGNAL(_fromUtf8("linkActivated(QString)")), Dialog.onLinkActivated)
        QtCore.QObject.connect(self.labelFollowedBy, QtCore.SIGNAL(_fromUtf8("linkActivated(QString)")), Dialog.onLinkActivated)
        QtCore.QObject.connect(self.labelLists, QtCore.SIGNAL(_fromUtf8("linkActivated(QString)")), Dialog.onLinkActivated)
        QtCore.QObject.connect(self.labelListedBy, QtCore.SIGNAL(_fromUtf8("linkActivated(QString)")), Dialog.onLinkActivated)
        QtCore.QObject.connect(self.labelUpdates, QtCore.SIGNAL(_fromUtf8("linkActivated(QString)")), Dialog.onLinkActivated)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.textBrowserUser, self.tabWidget)
        Dialog.setTabOrder(self.tabWidget, self.textBrowserFav)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "@{screen_name} - とにかくシンプルな Twitter クライアント", None, QtGui.QApplication.UnicodeUTF8))
        self.labelUpdates.setText(QtGui.QApplication.translate("Dialog", "<a href=\"updates\">{updates} ツイート</a>", None, QtGui.QApplication.UnicodeUTF8))
        self.labelFollows.setText(QtGui.QApplication.translate("Dialog", "<a href=\"follows\">{follows} 人をフォロー</a>", None, QtGui.QApplication.UnicodeUTF8))
        self.labelFollowedBy.setText(QtGui.QApplication.translate("Dialog", "<a href=\"followed_by\">{followed_by} 人がフォロー</a>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.tabFollow), QtGui.QApplication.translate("Dialog", "最新のツイートとフォロワーを表示", None, QtGui.QApplication.UnicodeUTF8))
        self.labelLists.setText(QtGui.QApplication.translate("Dialog", "<a href=\"lists\">公開リスト</a>", None, QtGui.QApplication.UnicodeUTF8))
        self.labelListedBy.setText(QtGui.QApplication.translate("Dialog", "<a href=\"listed_by\">{listed_by} 個のリストにいる</a>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.tabList), QtGui.QApplication.translate("Dialog", "このユーザーに関係するリストを表示", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.tabFav), QtGui.QApplication.translate("Dialog", "このユーザーのお気に入りツイートを表示", None, QtGui.QApplication.UnicodeUTF8))

from listitembrowser import ListItemBrowser
from qstatusbrowser import QStatusBrowser
from useritembrowser import UserItemBrowser
import twclient_rc
