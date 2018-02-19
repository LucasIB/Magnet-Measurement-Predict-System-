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
@author: lucas.balthazar
'''
from PyQt4 import QtCore, QtGui
from page_train import *

#Library for predicts
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split

#Library for Neural Networks
from pybrain.datasets import SupervisedDataSet
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised import BackpropTrainer

import plot

class lib(object):
    def __init__(self):
       self.samples, self.training = 0, 0
       self.validation, self.testing = 0, 0
       self.entrada, self.saida = 0, 0
       
lib = lib()

class Janela_NN_train(QtGui.QMainWindow):
    def __init__(self, parent=None): 
        super(Janela_NN_train,self).__init__(parent)
        self.page_2 = Ui_page_arch_train()
        self.page_2.setupUi(self)

        self.move(QtGui.QDesktopWidget().availableGeometry().center().x() - self.geometry().width()/2,\
                  QtGui.QDesktopWidget().availableGeometry().center().y() - self.geometry().height()/2)

        self.page_2.pb_back.clicked.connect(self.Cancel)
        self.page_2.pb_next.clicked.connect(self.next)
        self.page_2.pb_cancel.clicked.connect(self.closeEvent)
        self.page_2.pb_train.clicked.connect(self.dataset_manipulation)
        self.page_2.pb_teste.clicked.connect(self.test_data)
        self.page_2.pb_default.clicked.connect(self.default)
        self.page_2.pb_plot.clicked.connect(self.plotting)
        self.page_2.pb_predict.clicked.connect(self.predicting)
    
    def dataset_manipulation(self):
        self.dataset = SupervisedDataSet(len(lib.entrada[0]), len(lib.saida[0]))

        ## Number of neurons in Hidden Layer
        nr_neurons = self.page_2.sb_nr_neurons.value()

        ## Number os epochs
        nr_epochs = self.page_2.sb_nr_epochs.value()

        ## Leaning rate:
        learn_rate = self.page_2.sb_rate.value()

        ## Momentum:
        momentum = self.page_2.sb_momentum.value()


        ## Adding Train Samples
        for i in range(lib.training):
            self.dataset.addSample(lib.entrada[i], lib.saida[i])
        print('Training: %d' % lib.training) 

        ## Buid Network
        self.network = buildNetwork(self.dataset.indim, nr_neurons, self.dataset.outdim, bias=True)

        ## Back Propagation Trainer
        self.trainer = BackpropTrainer(self.network, self.dataset, learn_rate, momentum)

        self.page_2.count_1.setText(str(lib.training))
        self.page_2.count_2.setText(str(lib.validation))
        self.page_2.count_3.setText(str(lib.testing))
        QtGui.QApplication.processEvents()
        
        self.train_epochs(nr_epochs)

    def train_epochs(self, epochs):
        for epoch in range(epochs):
            self.trainer.train()
        self.page_2.pb_teste.setEnabled(True)

    def test_data(self):
        test_data = SupervisedDataSet(len(lib.entrada[0]), len(lib.saida[0]))
        for i in range(lib.training, (lib.validation+lib.testing)):
            self.dataset.addSample(lib.entrada[i], lib.saida[i])

        print('Testing: %d' % lib.testing) 

##        self.trainer.testOnData(test_data, verbose=True)     Still not operating, investigate

    def predicting(self):
        try:
            self.K = self.page_2.sb_nr_neighbors.value()

            #k-Nearest Neighbors Regression
            self.knn = KNeighborsRegressor(n_neighbors=self.K)

            #Train machine until training range
            self.y_ = self.knn.fit(lib.entrada[:lib.training],
                                   lib.saida[:lib.training]).predict(lib.entrada[:lib.training])
    ##        self.y_ = self.knn.fit(lib.entrada,
    ##                               lib.saida).predict(lib.entrada)
        except:
            QtGui.QMessageBox.warning(self,'Warning','Can not to predict files. Please, try again.',QtGui.QMessageBox.Ok)
            QtGui.QApplication.processEvents()


    def plotting(self):
        plot.Capture(lib.entrada, lib.saida, lib.training,
                     lib.validation, lib.testing, self.y_)
        
        window = plot.Plot(self)
        window.show()       
        
    def next(self):
        pass

    def Cancel(self):
        self.close()

    def closeEvent(self, event):
        self.deleteLater()

    def default(self):
        self.page_2.sb_nr_epochs.setValue(100)
        self.page_2.sb_rate.setValue(0.01)
        self.page_2.sb_momentum.setValue(0.99)

class Capturar(object):
    def __init__(self, entrada, saida):
        lib.entrada = entrada
        lib.saida = saida

class Capturar2(object):
    def __init__(self, treinamento, validation, teste):
        lib.training = treinamento
        lib.validation = validation
        lib.testing = teste
