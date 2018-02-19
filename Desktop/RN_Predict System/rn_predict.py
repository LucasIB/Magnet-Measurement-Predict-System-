#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
`  @@@@@@@@`-@@@@@@@@@@@@@@@@@@@  `
`  @@@@@@@     .@@@@@@@@@@@@@@@@  `
`  @@@@@:    `@@@:.   -@@@@@@@@@  `
`  @@@@:   .@@:`       .@@@@@@@@  `
`  @@@@  `@@-   `.@@@@@@@@@@@@@@  `
`  @@@. -@: .@@@@@- ``      .@@@  `
`  @@@ -@.:@@-              `@@@  `
`  @@@.@@@@@@@@@:-``@@@@@@. `@@@  `
`  @@@@@-    .@@@@@:`   .@@@@@@@  `
`  @@@@        @@@@@@@:`    .:@@  `
`  @@@@        @@@@@@@@@@`        `
`                                 `
MACHINE LEARNING AND NEURAL NETWORK FOR MAGNETIC MEASUREMENTS ANALYSIS
Created on 14/09/2017
@author: lucas.balthazar
'''
#interface
import threading
import sys
from PySide import QtGui
from PyQt4 import QtCore, QtGui
from interface import *
import load_dataset
import page_validation
import page_arch_train
        
class MainWindow(QtGui.QMainWindow):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.move(QtGui.QDesktopWidget().availableGeometry().center().x() - self.geometry().width()/2,\
                  QtGui.QDesktopWidget().availableGeometry().center().y() - self.geometry().height()/2)

        self.trainpar = (self.ui.ch_Nn, self.ui.ch_Bn, self.ui.ch_disX, \
                         self.ui.ch_Sn, self.ui.ch_angle, self.ui.ch_disY)

        self.trainsp = (self.ui.sb_Nn, self.ui.sb_Bn, self.ui.sb_Sn, self.ui.sb_angle)

        self.ui.pb_in_open.clicked.connect(self.data_in)
        self.ui.pb_gen_Dataset.clicked.connect(self.config_data)
        self.ui.pb_next.clicked.connect(self.next_)
        self.ui.pb_cancel.clicked.connect(self.closeEvent)
##        self.ui.pb_NN_start.clicked.connect(self...)

        self.ui.label_11.setVisible(False)

    def data_in(self):
        try:
            self.dados = load_dataset.Cross_check()
            self.files = self.dados.Load_Files()    
            self.setStatus("Data entry made successfully")
            QtGui.QMessageBox.information(self,'Info','Files successfully updated.',QtGui.QMessageBox.Ok)
            self.ui.pb_gen_Dataset.setEnabled(True)
            self.ui.groupBox_3.setEnabled(True)
            self.ui.groupBox_5.setEnabled(True)
            QtGui.QApplication.processEvents()
        except:
            #raise NameError("Failed to open data. Check this.")
            QtGui.QMessageBox.critical(self,'Warning','Can not open files. Select valid files.',QtGui.QMessageBox.Ok)

    def config_data(self):
        self.enter = []
        self.outs = []
        values = []
        targets = []
        flag = True
        try:
            for i in range(len(self.dados.files)):
                self.dados.Data[i].multipoledf.index = self.dados.Data[i].multipoledf['n']
                if self.trainpar[0].isChecked():
                    Nn_mean = self.dados.Data[i].multipoledf[self.trainpar[0].text()][self.trainsp[0].value()]    #Normal Quadrupole
                    values.append(Nn_mean)
                if self.trainpar[1].isChecked():
                    Bn_mean = self.dados.Data[i].multipoledf[self.trainpar[1].text()][self.trainsp[1].value()]    #Module
                    values.append(Bn_mean)
                if self.trainpar[3].isChecked():
                    Sn_mean = self.dados.Data[i].multipoledf[self.trainpar[3].text()][self.trainsp[2].value()]    #Skew Sextupole
                    values.append(Sn_mean)
                if self.trainpar[4].isChecked():
                    self.roll_mean = self.dados.Data[i].multipoledf[self.trainpar[4].text()][self.trainsp[3].value()]    #Angle [rad]
                    self.outs.append([self.roll_mean])
                if self.trainpar[2].isChecked():
                    self.desl_x = self.dados.Data[i].deslo_x
                if self.trainpar[5].isChecked():
                    self.desl_y = self.dados.Data[i].deslo_y
                self.enter.append(values)
                targets = self.targets()
                values = []
                QtGui.QApplication.processEvents()
                           
            self.saida = targets

            print(self.enter[:5])
            print('Tamanho de enter: ',len(self.enter))

            print(self.saida[:5])
            print('Tamanho da saida: ',len(self.saida))         
            
            QtGui.QMessageBox.information(self,'Info','Files successfully configurated.',QtGui.QMessageBox.Ok)
            self.Envia()     #Send data for further processing
            QtGui.QApplication.processEvents()

        except:
            flag = False
            self.setStatus("Fail configurate data. Please, try again")
            QtGui.QMessageBox.warning(self,'Warning','Can not to configure files. Please, try again.',QtGui.QMessageBox.Ok)

        while flag:
            self.ui.label_10.setText("Files uploaded")
            self.ui.label_9.setVisible(False)
            self.ui.label_11.setVisible(True)
            self.ui.pb_next.setEnabled(True)
            self.ui.pb_NN_start.setEnabled(True)
            break

    def targets(self):
        if self.trainpar[2].isChecked() and self.trainpar[5].isChecked():
            self.outs.append([self.desl_x, self.desl_y])
        elif self.trainpar[2].isChecked():
            self.desl_x = self.dados.Data[0].deslo_x                                  #Displacement X [um]
            self.outs.append([self.desl_x])
        elif self.trainpar[5].isChecked():
            self.desl_y = self.dados.Data[0].deslo_y                                  #Displacement Y [um]
            self.outs.append([self.desl_y])
        return self.outs

    def next_(self):
        samples = len(self.enter)
        page_validation.Capture(samples)
        window = page_validation.Janela(self)
        window.show()
                            
    def setStatus(self, text):
        txt=""
        try:
            txt = QtCore.QString.fromUtf8(text)
        except AttributeError:
            txt = text
        self.ui.input_summary.setText(txt)
        QtGui.QApplication.processEvents()

    def Envia(self):
        entrada, saida = self.enter, self.saida
        page_arch_train.Capturar(entrada, saida)

    def closeEvent(self, event):
        self.deleteLater()

            
#class GUIThread(threading.Thread):
#    def __init__(self):
#        threading.Thread.__init__(self)
#        self.start()

#    def run(self):
#        self.app = QtGui.QApplication(sys.argv)
#        self.myapp = MainWindow()
#        self.myapp.show()
#        self.app.exec_()


#t = GUIThread()
        
class screen(object):
    def __init__(self):
        self.app = QtGui.QApplication(sys.argv)
        self.myapp = MainWindow()
        self.myapp.show()
        self.app.exec_()
        
        
t = screen()
