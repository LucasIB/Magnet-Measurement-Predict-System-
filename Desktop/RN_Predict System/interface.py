# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'predict_interface.ui'
#
# Created: Thu Sep 21 15:00:36 2017
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(989, 674)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/brain2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setIconSize(QtCore.QSize(26, 26))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 70, 431, 151))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pb_in_open = QtGui.QPushButton(self.groupBox)
        self.pb_in_open.setGeometry(QtCore.QRect(160, 80, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pb_in_open.setFont(font)
        self.pb_in_open.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/1351621523_Download.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pb_in_open.setIcon(icon1)
        self.pb_in_open.setIconSize(QtCore.QSize(30, 30))
        self.pb_in_open.setObjectName(_fromUtf8("pb_in_open"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 70, 41, 41))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8("imagens/multiple_inputs_filled1600.png")))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(80, 80, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 591, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 400, 431, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.input_summary = QtGui.QLabel(self.groupBox_2)
        self.input_summary.setGeometry(QtCore.QRect(10, 30, 361, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.input_summary.setFont(font)
        self.input_summary.setObjectName(_fromUtf8("input_summary"))
        self.pb_back = QtGui.QPushButton(self.centralwidget)
        self.pb_back.setEnabled(False)
        self.pb_back.setGeometry(QtCore.QRect(614, 600, 101, 31))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/1351621543_Previous.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pb_back.setIcon(icon2)
        self.pb_back.setIconSize(QtCore.QSize(20, 20))
        self.pb_back.setObjectName(_fromUtf8("pb_back"))
        self.pb_next = QtGui.QPushButton(self.centralwidget)
        self.pb_next.setEnabled(False)
        self.pb_next.setGeometry(QtCore.QRect(720, 600, 101, 31))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/1351621545_Next.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pb_next.setIcon(icon3)
        self.pb_next.setIconSize(QtCore.QSize(20, 20))
        self.pb_next.setObjectName(_fromUtf8("pb_next"))
        self.pb_cancel = QtGui.QPushButton(self.centralwidget)
        self.pb_cancel.setGeometry(QtCore.QRect(880, 600, 101, 31))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/1351621507_Delete.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pb_cancel.setIcon(icon4)
        self.pb_cancel.setIconSize(QtCore.QSize(20, 20))
        self.pb_cancel.setObjectName(_fromUtf8("pb_cancel"))
        self.pb_NN_start = QtGui.QPushButton(self.centralwidget)
        self.pb_NN_start.setEnabled(False)
        self.pb_NN_start.setGeometry(QtCore.QRect(10, 600, 191, 31))
        self.pb_NN_start.setIcon(icon)
        self.pb_NN_start.setIconSize(QtCore.QSize(22, 22))
        self.pb_NN_start.setObjectName(_fromUtf8("pb_NN_start"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 50, 991, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(920, 0, 51, 51))
        self.label_8.setText(_fromUtf8(""))
        self.label_8.setPixmap(QtGui.QPixmap(_fromUtf8("imagens/LNLS_sal.jpg")))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(30, 540, 31, 31))
        self.label_9.setText(_fromUtf8(""))
        self.label_9.setPixmap(QtGui.QPixmap(_fromUtf8("imagens/exclamation2.png")))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setEnabled(False)
        self.label_10.setGeometry(QtCore.QRect(70, 530, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setEnabled(True)
        self.label_11.setGeometry(QtCore.QRect(30, 540, 31, 31))
        self.label_11.setText(_fromUtf8(""))
        self.label_11.setPixmap(QtGui.QPixmap(_fromUtf8("imagens/check.png")))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setEnabled(False)
        self.groupBox_3.setGeometry(QtCore.QRect(490, 70, 421, 151))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.ch_Bn = QtGui.QCheckBox(self.groupBox_3)
        self.ch_Bn.setGeometry(QtCore.QRect(20, 80, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ch_Bn.setFont(font)
        self.ch_Bn.setObjectName(_fromUtf8("ch_Bn"))
        self.ch_Sn = QtGui.QCheckBox(self.groupBox_3)
        self.ch_Sn.setGeometry(QtCore.QRect(20, 110, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ch_Sn.setFont(font)
        self.ch_Sn.setObjectName(_fromUtf8("ch_Sn"))
        self.ch_Nn = QtGui.QCheckBox(self.groupBox_3)
        self.ch_Nn.setGeometry(QtCore.QRect(20, 50, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ch_Nn.setFont(font)
        self.ch_Nn.setObjectName(_fromUtf8("ch_Nn"))
        self.radioButton = QtGui.QRadioButton(self.groupBox_3)
        self.radioButton.setGeometry(QtCore.QRect(300, 60, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.label_7 = QtGui.QLabel(self.groupBox_3)
        self.label_7.setGeometry(QtCore.QRect(210, 30, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.sb_Nn = QtGui.QSpinBox(self.groupBox_3)
        self.sb_Nn.setGeometry(QtCore.QRect(210, 50, 42, 22))
        self.sb_Nn.setMinimum(1)
        self.sb_Nn.setMaximum(15)
        self.sb_Nn.setProperty("value", 2)
        self.sb_Nn.setObjectName(_fromUtf8("sb_Nn"))
        self.sb_Sn = QtGui.QSpinBox(self.groupBox_3)
        self.sb_Sn.setGeometry(QtCore.QRect(210, 110, 42, 22))
        self.sb_Sn.setMinimum(1)
        self.sb_Sn.setMaximum(15)
        self.sb_Sn.setProperty("value", 3)
        self.sb_Sn.setObjectName(_fromUtf8("sb_Sn"))
        self.sb_Bn = QtGui.QSpinBox(self.groupBox_3)
        self.sb_Bn.setGeometry(QtCore.QRect(210, 80, 42, 22))
        self.sb_Bn.setMinimum(1)
        self.sb_Bn.setMaximum(15)
        self.sb_Bn.setObjectName(_fromUtf8("sb_Bn"))
        self.groupBox_5 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_5.setEnabled(False)
        self.groupBox_5.setGeometry(QtCore.QRect(20, 240, 431, 151))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.label_6 = QtGui.QLabel(self.groupBox_5)
        self.label_6.setGeometry(QtCore.QRect(70, 60, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_5 = QtGui.QLabel(self.groupBox_5)
        self.label_5.setGeometry(QtCore.QRect(20, 50, 41, 41))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setPixmap(QtGui.QPixmap(_fromUtf8("imagens/target-icon-2.png")))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.ch_disY = QtGui.QCheckBox(self.groupBox_5)
        self.ch_disY.setGeometry(QtCore.QRect(160, 100, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ch_disY.setFont(font)
        self.ch_disY.setObjectName(_fromUtf8("ch_disY"))
        self.ch_disX = QtGui.QCheckBox(self.groupBox_5)
        self.ch_disX.setGeometry(QtCore.QRect(160, 70, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ch_disX.setFont(font)
        self.ch_disX.setObjectName(_fromUtf8("ch_disX"))
        self.ch_angle = QtGui.QCheckBox(self.groupBox_5)
        self.ch_angle.setGeometry(QtCore.QRect(160, 40, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ch_angle.setFont(font)
        self.ch_angle.setObjectName(_fromUtf8("ch_angle"))
        self.label_12 = QtGui.QLabel(self.groupBox_5)
        self.label_12.setGeometry(QtCore.QRect(340, 20, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.sb_angle = QtGui.QSpinBox(self.groupBox_5)
        self.sb_angle.setGeometry(QtCore.QRect(340, 40, 42, 22))
        self.sb_angle.setMinimum(1)
        self.sb_angle.setMaximum(3)
        self.sb_angle.setProperty("value", 2)
        self.sb_angle.setObjectName(_fromUtf8("sb_angle"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(False)
        self.pushButton.setGeometry(QtCore.QRect(640, 470, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/Lupa2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon5)
        self.pushButton.setIconSize(QtCore.QSize(20, 20))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pb_gen_Dataset = QtGui.QPushButton(self.centralwidget)
        self.pb_gen_Dataset.setEnabled(False)
        self.pb_gen_Dataset.setGeometry(QtCore.QRect(590, 420, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pb_gen_Dataset.setFont(font)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8("imagens/engine.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pb_gen_Dataset.setIcon(icon6)
        self.pb_gen_Dataset.setIconSize(QtCore.QSize(20, 20))
        self.pb_gen_Dataset.setObjectName(_fromUtf8("pb_gen_Dataset"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 989, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Predict Analysis", None))
        self.groupBox.setTitle(_translate("MainWindow", "Get input data from workspace ", None))
        self.label_2.setText(_translate("MainWindow", "Input data to present to the network", None))
        self.pb_in_open.setToolTip(_translate("MainWindow", "<html><head/><body><p>Load the input data to generate the Machine Learning training dataset</p></body></html>", None))
        self.label_4.setText(_translate("MainWindow", "Inputs:", None))
        self.label.setText(_translate("MainWindow", "Neural Network and Prediction System for magnet measurements", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Summary", None))
        self.input_summary.setText(_translate("MainWindow", "No inputs selected.", None))
        self.pb_back.setText(_translate("MainWindow", "  Back", None))
        self.pb_next.setText(_translate("MainWindow", "  Next", None))
        self.pb_cancel.setText(_translate("MainWindow", " Cancel", None))
        self.pb_NN_start.setText(_translate("MainWindow", "   Neural Network Start", None))
        self.label_10.setText(_translate("MainWindow", "Select inputs and targts tool, then click [Next]", None))
        self.groupBox_3.setToolTip(_translate("MainWindow", "<html><head/><body><p>The input attributes are limited to a maximum of 6 to avoid noise in the approximations.</p></body></html>", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "From inputs select attributes for training", None))
        self.ch_Bn.setText(_translate("MainWindow", "avg_L.Bn(T/m^n-2)", None))
        self.ch_Sn.setText(_translate("MainWindow", "avg_L.Sn(T/m^n-2)", None))
        self.ch_Nn.setText(_translate("MainWindow", "avg_L.Nn(T/m^n-2)", None))
        self.radioButton.setText(_translate("MainWindow", "Normalizado", None))
        self.label_7.setText(_translate("MainWindow", "n-order:", None))
        self.groupBox_5.setTitle(_translate("MainWindow", "Target data defining desired network output", None))
        self.label_6.setText(_translate("MainWindow", "Targets:", None))
        self.ch_disY.setText(_translate("MainWindow", "Displacement Y (um)", None))
        self.ch_disX.setText(_translate("MainWindow", "Displacement X (um)", None))
        self.ch_angle.setText(_translate("MainWindow", "avg_angle(rad)  ", None))
        self.label_12.setText(_translate("MainWindow", "n-order:", None))
        self.pushButton.setText(_translate("MainWindow", "View Dataset", None))
        self.pb_gen_Dataset.setText(_translate("MainWindow", "Generate Dataset from Data", None))

