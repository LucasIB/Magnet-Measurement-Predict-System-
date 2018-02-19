from PyQt4 import QtCore, QtGui
from page_validate import *
import page_arch_train

class lib(object):
    def __init__(self):
        self.samples = 0

lib = lib()

class Janela(QtGui.QMainWindow):
    def __init__(self, parent=None): 
        super(Janela,self).__init__(parent)
        self.page_1 = Ui_page_validate()
        self.page_1.setupUi(self)

        self.move(QtGui.QDesktopWidget().availableGeometry().center().x() - self.geometry().width()/2,\
                  QtGui.QDesktopWidget().availableGeometry().center().y() - self.geometry().height()/2)

        self.page_1.pb_defaults.clicked.connect(self.defaults)
        self.page_1.pb_back.clicked.connect(self.closeEvent)
        self.page_1.pb_next.clicked.connect(self.next_)
        self.page_1.pb_cancel.clicked.connect(self.Cancel)
        self.page_1.cb_validate.activated.connect(self.val_percent)
        self.page_1.cb_testing.activated.connect(self.test_percent)

        self.val_per = 0.50    #Default

        self.setStatus("Random divide up the %d samples" % lib.samples)
        self.counter_1()
      
    def val_percent(self):
        if self.page_1.cb_validate.currentIndex() == 0:     #20%
            self.val_per = 0.66
            self.page_1.cb_testing.setCurrentIndex(2)
            
        elif self.page_1.cb_validate.currentIndex() == 1:   #15%
            self.val_per = 0.50
            self.page_1.cb_testing.setCurrentIndex(1)

        elif self.page_1.cb_validate.currentIndex() == 2:   #10%
            self.val_per = 0.33
            self.page_1.cb_testing.setCurrentIndex(0)

        self.counter_2()

    def test_percent(self):
        if self.page_1.cb_testing.currentIndex() == 0:      #20%
            self.test_per = 0.66
            self.page_1.cb_validate.setCurrentIndex(2)

        elif self.page_1.cb_testing.currentIndex() == 1:    #15%
            self.val_per = 0.50
            self.page_1.cb_validate.setCurrentIndex(1)

        elif self.page_1.cb_testing.currentIndex() == 2:    #10%
            self.val_per = 0.33
            self.page_1.cb_validate.setCurrentIndex(0)

        self.counter_2()

    def counter_1(self):
        total = lib.samples
        self.count_train = int(total*0.7)                                #Default 70% for trainer
        self.counter_2()
        return self.page_1.count_1.setText(str(self.count_train))

    def counter_2(self):
        self.diff = lib.samples - self.count_train                       #Diff between total and 0.7%*total
        self.per = int(self.diff*self.val_per)
        self.counter_3()
        return self.page_1.count_2.setText(str(self.per))

    def counter_3(self):
        self.rest = self.diff - self.per                                     #Diff between validation and testing data
        return self.page_1.count_3.setText(str(self.rest))

    def defaults(self):
        self.val_per = 0.50  #Default
        self.page_1.cb_testing.setCurrentIndex(1)
        self.page_1.cb_validate.setCurrentIndex(1)
        self.counter_1()

    def setStatus(self, text):
        txt=""
        try:
            txt = QtCore.QString.fromUtf8(text)
        except AttributeError:
            txt = text
        self.page_1.label_2.setText(txt)
        QtGui.QApplication.processEvents()

    def Cancel(self):
        self.close()

    def closeEvent(self, event):
        self.deleteLater()

    def next_(self):
        window = page_arch_train.Janela_NN_train(self)
        window.show()
        self.Enviar()

    def Enviar(self):
        treinamento, validation = self.count_train, self.per
        teste = self.rest
        page_arch_train.Capturar2(treinamento, validation, teste)


class Capture(object):
    def __init__(self, samples):
        lib.samples = samples

