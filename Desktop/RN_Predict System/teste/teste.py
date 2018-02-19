from PyQt4 import QtCore, QtGui
import threading
import sys

# Interface
from janela import *
from main import *

class Janela(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui_2 = Ui_MainWindow2()
        self.ui_2.setupUi(self)


class Main_Window(QtGui.QMainWindow):     #Interface Gráfica
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pb_janela1.clicked.connect(self.janela_um)

    def janela_um(self):
        window = Janela(self)
        window.show()

class Interface_rc_analysis(object):
    def __init__(self):
        # Inicia Interface Grafica
        self.App = QtGui.QApplication(sys.argv)
        self.myapp = Main_Window()
        self.myapp.show()
        self.App.exec_()


a = Interface_rc_analysis()
