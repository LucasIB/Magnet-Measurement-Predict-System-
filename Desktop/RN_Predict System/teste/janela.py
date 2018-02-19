# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'janela.ui'
#
# Created: Thu Sep 14 16:11:10 2017
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow2(object):
    def setupUi(self, MainWindow2):
        MainWindow2.setObjectName(_fromUtf8("MainWindow2"))
        MainWindow2.resize(993, 700)
        self.centralwidget = QtGui.QWidget(MainWindow2)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(390, 80, 181, 111))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(280, 250, 371, 211))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.pushButton = QtGui.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(70, 40, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(130, 110, 151, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        MainWindow2.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 993, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow2.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow2)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow2.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow2)

    def retranslateUi(self, MainWindow2):
        MainWindow2.setWindowTitle(_translate("MainWindow2", "MainWindow", None))
        self.label.setText(_translate("MainWindow2", "Oi, tudo bem?", None))
        self.pushButton.setText(_translate("MainWindow2", "PushButton", None))
        self.label_2.setText(_translate("MainWindow2", "Tem que  manter isso, viu?", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow2", "Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow2", "Tab 2", None))

