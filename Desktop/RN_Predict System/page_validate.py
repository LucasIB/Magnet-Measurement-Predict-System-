# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'page_validation.ui'
#
# Created: Wed Sep 20 14:52:49 2017
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

class Ui_page_validate(object):
    def setupUi(self, page_validate):
        page_validate.setObjectName(_fromUtf8("page_validate"))
        page_validate.resize(989, 674)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/brain2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        page_validate.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(page_validate)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 591, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 50, 991, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 80, 481, 481))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(60, 60, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(50, 110, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(50, 150, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(50, 190, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.cb_validate = QtGui.QComboBox(self.groupBox)
        self.cb_validate.setGeometry(QtCore.QRect(140, 150, 69, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cb_validate.setFont(font)
        self.cb_validate.setObjectName(_fromUtf8("cb_validate"))
        self.cb_validate.addItem(_fromUtf8(""))
        self.cb_validate.addItem(_fromUtf8(""))
        self.cb_validate.addItem(_fromUtf8(""))
        self.cb_testing = QtGui.QComboBox(self.groupBox)
        self.cb_testing.setGeometry(QtCore.QRect(140, 190, 69, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cb_testing.setFont(font)
        self.cb_testing.setObjectName(_fromUtf8("cb_testing"))
        self.cb_testing.addItem(_fromUtf8(""))
        self.cb_testing.addItem(_fromUtf8(""))
        self.cb_testing.addItem(_fromUtf8(""))
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(150, 110, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(380, 60, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.count_1 = QtGui.QLabel(self.groupBox)
        self.count_1.setGeometry(QtCore.QRect(385, 113, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.count_1.setFont(font)
        self.count_1.setObjectName(_fromUtf8("count_1"))
        self.count_2 = QtGui.QLabel(self.groupBox)
        self.count_2.setGeometry(QtCore.QRect(385, 152, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.count_2.setFont(font)
        self.count_2.setObjectName(_fromUtf8("count_2"))
        self.count_3 = QtGui.QLabel(self.groupBox)
        self.count_3.setGeometry(QtCore.QRect(385, 190, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.count_3.setFont(font)
        self.count_3.setObjectName(_fromUtf8("count_3"))
        self.pb_defaults = QtGui.QPushButton(self.groupBox)
        self.pb_defaults.setGeometry(QtCore.QRect(190, 430, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pb_defaults.setFont(font)
        self.pb_defaults.setObjectName(_fromUtf8("pb_defaults"))
        self.bargraph = QtGui.QLabel(self.groupBox)
        self.bargraph.setGeometry(QtCore.QRect(10, 50, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bargraph.setFont(font)
        self.bargraph.setText(_fromUtf8(""))
        self.bargraph.setPixmap(QtGui.QPixmap(_fromUtf8("imagens/Bar-Chart-icon.png")))
        self.bargraph.setScaledContents(True)
        self.bargraph.setObjectName(_fromUtf8("bargraph"))
        self.bar_blue = QtGui.QLabel(self.groupBox)
        self.bar_blue.setGeometry(QtCore.QRect(20, 90, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bar_blue.setFont(font)
        self.bar_blue.setText(_fromUtf8(""))
        self.bar_blue.setPixmap(QtGui.QPixmap(_fromUtf8("imagens/Bar_blue.png")))
        self.bar_blue.setScaledContents(True)
        self.bar_blue.setObjectName(_fromUtf8("bar_blue"))
        self.bar_red = QtGui.QLabel(self.groupBox)
        self.bar_red.setGeometry(QtCore.QRect(10, 140, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bar_red.setFont(font)
        self.bar_red.setText(_fromUtf8(""))
        self.bar_red.setPixmap(QtGui.QPixmap(_fromUtf8("imagens/Bar-Red.png")))
        self.bar_red.setScaledContents(True)
        self.bar_red.setObjectName(_fromUtf8("bar_red"))
        self.bar_green = QtGui.QLabel(self.groupBox)
        self.bar_green.setGeometry(QtCore.QRect(0, 180, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bar_green.setFont(font)
        self.bar_green.setText(_fromUtf8(""))
        self.bar_green.setPixmap(QtGui.QPixmap(_fromUtf8("imagens/Bar-green.png")))
        self.bar_green.setScaledContents(True)
        self.bar_green.setObjectName(_fromUtf8("bar_green"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(500, 80, 481, 481))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label_8 = QtGui.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(20, 30, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_10 = QtGui.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(40, 80, 421, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(40, 170, 421, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(self.groupBox_2)
        self.label_12.setGeometry(QtCore.QRect(40, 270, 441, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_14 = QtGui.QLabel(self.groupBox_2)
        self.label_14.setGeometry(QtCore.QRect(10, 60, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setText(_fromUtf8(""))
        self.label_14.setPixmap(QtGui.QPixmap(_fromUtf8("imagens/Bar_blue.png")))
        self.label_14.setScaledContents(True)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_16 = QtGui.QLabel(self.groupBox_2)
        self.label_16.setGeometry(QtCore.QRect(0, 160, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setText(_fromUtf8(""))
        self.label_16.setPixmap(QtGui.QPixmap(_fromUtf8("imagens/Bar-Red.png")))
        self.label_16.setScaledContents(True)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.label_18 = QtGui.QLabel(self.groupBox_2)
        self.label_18.setGeometry(QtCore.QRect(-10, 260, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setText(_fromUtf8(""))
        self.label_18.setPixmap(QtGui.QPixmap(_fromUtf8("imagens/Bar-green.png")))
        self.label_18.setScaledContents(True)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.pb_next = QtGui.QPushButton(self.centralwidget)
        self.pb_next.setEnabled(True)
        self.pb_next.setGeometry(QtCore.QRect(720, 600, 101, 31))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/1351621545_Next.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pb_next.setIcon(icon1)
        self.pb_next.setIconSize(QtCore.QSize(20, 20))
        self.pb_next.setObjectName(_fromUtf8("pb_next"))
        self.pb_back = QtGui.QPushButton(self.centralwidget)
        self.pb_back.setEnabled(True)
        self.pb_back.setGeometry(QtCore.QRect(614, 600, 101, 31))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/1351621543_Previous.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pb_back.setIcon(icon2)
        self.pb_back.setIconSize(QtCore.QSize(20, 20))
        self.pb_back.setObjectName(_fromUtf8("pb_back"))
        self.pb_cancel = QtGui.QPushButton(self.centralwidget)
        self.pb_cancel.setGeometry(QtCore.QRect(880, 600, 101, 31))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/1351621507_Delete.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pb_cancel.setIcon(icon3)
        self.pb_cancel.setIconSize(QtCore.QSize(20, 20))
        self.pb_cancel.setObjectName(_fromUtf8("pb_cancel"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 40, 331, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        page_validate.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(page_validate)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 989, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        page_validate.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(page_validate)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        page_validate.setStatusBar(self.statusbar)

        self.retranslateUi(page_validate)
        self.cb_validate.setCurrentIndex(1)
        self.cb_testing.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(page_validate)

    def retranslateUi(self, page_validate):
        page_validate.setWindowTitle(_translate("page_validate", "Validation and Test Data", None))
        self.label.setText(_translate("page_validate", "Validation and Test Data", None))
        self.groupBox.setTitle(_translate("page_validate", "Select Percentages", None))
        self.label_2.setText(_translate("page_validate", "Random divide up the xxx samples:", None))
        self.label_3.setText(_translate("page_validate", "Training:", None))
        self.label_4.setText(_translate("page_validate", "Validation:", None))
        self.label_5.setText(_translate("page_validate", "Testing:", None))
        self.cb_validate.setItemText(0, _translate("page_validate", "20 %", None))
        self.cb_validate.setItemText(1, _translate("page_validate", "15 %", None))
        self.cb_validate.setItemText(2, _translate("page_validate", "10 %", None))
        self.cb_testing.setItemText(0, _translate("page_validate", "20 %", None))
        self.cb_testing.setItemText(1, _translate("page_validate", "15 %", None))
        self.cb_testing.setItemText(2, _translate("page_validate", "10 %", None))
        self.label_6.setText(_translate("page_validate", "70 % (Default)", None))
        self.label_7.setText(_translate("page_validate", "Samples:", None))
        self.count_1.setText(_translate("page_validate", "count_1", None))
        self.count_2.setText(_translate("page_validate", "count_2", None))
        self.count_3.setText(_translate("page_validate", "count_3", None))
        self.pb_defaults.setText(_translate("page_validate", "Restore Defaults", None))
        self.groupBox_2.setTitle(_translate("page_validate", "Explanation", None))
        self.label_8.setText(_translate("page_validate", "Three Kinds of Samples:", None))
        self.label_10.setText(_translate("page_validate", "Training:\n"
"\n"
"These are presented to the network during training, and the network is\n"
"adjusted acording to its error.", None))
        self.label_11.setText(_translate("page_validate", "Validation:\n"
"\n"
" These are used to measure network generalization, and to halt training\n"
" when generalization stops improving.", None))
        self.label_12.setText(_translate("page_validate", "Testing:\n"
"\n"
" These have no effect on training and so provide an independent measure\n"
" of network performance during and after training.", None))
        self.pb_next.setText(_translate("page_validate", "  Next", None))
        self.pb_back.setText(_translate("page_validate", "  Back", None))
        self.pb_cancel.setText(_translate("page_validate", " Cancel", None))
        self.label_9.setText(_translate("page_validate", "Set aside some samples for validation and testing.", None))

