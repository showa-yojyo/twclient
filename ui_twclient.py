# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'twclient.ui'
#
# Created: Sun Apr 29 15:22:58 2012
#      by: PyQt4 UI code generator 4.8.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(450, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.verticalLayout.addWidget(self.comboBox)
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setOpenLinks(False)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.verticalLayout.addWidget(self.textBrowser)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 450, 19))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_O = QtGui.QMenu(self.menubar)
        self.menu_O.setObjectName(_fromUtf8("menu_O"))
        self.menu_D = QtGui.QMenu(self.menu_O)
        self.menu_D.setObjectName(_fromUtf8("menu_D"))
        self.menu_U = QtGui.QMenu(self.menu_O)
        self.menu_U.setObjectName(_fromUtf8("menu_U"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionSettings = QtGui.QAction(MainWindow)
        self.actionSettings.setObjectName(_fromUtf8("actionSettings"))
        self.actionAppAbout = QtGui.QAction(MainWindow)
        self.actionAppAbout.setObjectName(_fromUtf8("actionAppAbout"))
        self.actionRefresh = QtGui.QAction(MainWindow)
        self.actionRefresh.setObjectName(_fromUtf8("actionRefresh"))
        self.actionUserShow = QtGui.QAction(MainWindow)
        self.actionUserShow.setObjectName(_fromUtf8("actionUserShow"))
        self.menu_D.addAction(self.actionRefresh)
        self.menu_U.addAction(self.actionUserShow)
        self.menu_O.addAction(self.menu_D.menuAction())
        self.menu_O.addAction(self.menu_U.menuAction())
        self.menu_O.addSeparator()
        self.menu_O.addAction(self.actionAppAbout)
        self.menu_O.addAction(self.actionSettings)
        self.menu_O.addSeparator()
        self.menu_O.addAction(self.actionExit)
        self.menubar.addAction(self.menu_O.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.comboBox, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), MainWindow.onComboChanged)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QObject.connect(self.actionRefresh, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.onTimelineRefresh)
        QtCore.QObject.connect(self.actionAppAbout, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.onAppAbout)
        QtCore.QObject.connect(self.actionUserShow, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.onUserShow)
        QtCore.QObject.connect(self.actionSettings, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.onAppSettings)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Twitter Client", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_O.setTitle(QtGui.QApplication.translate("MainWindow", "操作(&O)", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_D.setTitle(QtGui.QApplication.translate("MainWindow", "表示(&D)", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_U.setTitle(QtGui.QApplication.translate("MainWindow", "ユーザー(&U)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "終了(&X)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setStatusTip(QtGui.QApplication.translate("MainWindow", "アプリケーションを終了する", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSettings.setText(QtGui.QApplication.translate("MainWindow", "設定(&S)...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAppAbout.setText(QtGui.QApplication.translate("MainWindow", "このアプリについて(&A)...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRefresh.setText(QtGui.QApplication.translate("MainWindow", "タイムラインを更新(&R)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRefresh.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+R", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUserShow.setText(QtGui.QApplication.translate("MainWindow", "ユーザーを表示(&U)...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUserShow.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+U", None, QtGui.QApplication.UnicodeUTF8))

