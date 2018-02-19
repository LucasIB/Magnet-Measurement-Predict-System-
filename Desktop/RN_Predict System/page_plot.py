# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'page_plot.ui'
#
# Created: Fri Sep 22 10:48:41 2017
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

class Ui_page_plotting(object):
    def setupUi(self, page_plotting):
        page_plotting.setObjectName(_fromUtf8("page_plotting"))
        page_plotting.resize(989, 674)
        self.centralwidget = QtGui.QWidget(page_plotting)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.wt_graphs = matplotlibWidget(self.centralwidget)
        self.wt_graphs.setGeometry(QtCore.QRect(0, 0, 991, 501))
        self.wt_graphs.setObjectName(_fromUtf8("wt_graphs"))
        self.pb_back = QtGui.QPushButton(self.centralwidget)
        self.pb_back.setEnabled(True)
        self.pb_back.setGeometry(QtCore.QRect(880, 600, 101, 31))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/1351621543_Previous.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pb_back.setIcon(icon)
        self.pb_back.setIconSize(QtCore.QSize(20, 20))
        self.pb_back.setObjectName(_fromUtf8("pb_back"))
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(390, 510, 201, 141))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        page_plotting.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(page_plotting)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 989, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        page_plotting.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(page_plotting)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        page_plotting.setStatusBar(self.statusbar)

        self.retranslateUi(page_plotting)
        QtCore.QMetaObject.connectSlotsByName(page_plotting)

    def retranslateUi(self, page_plotting):
        page_plotting.setWindowTitle(_translate("page_plotting", "Plot", None))
        self.pb_back.setText(_translate("page_plotting", "  Back", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("page_plotting", "Accuracy", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("page_plotting", "Percentage", None))

from plot_widget import matplotlibWidget
