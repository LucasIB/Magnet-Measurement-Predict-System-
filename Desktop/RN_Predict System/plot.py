import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
plt.style.use('bmh')
from PyQt4 import QtCore, QtGui

from page_plot import *
'''
Default parameters for plot
        self.page_3.wt_graphs.canvas.ax.     
        self.page_3.wt_graphs.canvas.fig.tight_layout()
        self.page_3.wt_graphs.canvas.draw()
'''

class lib(object):
    def __init__(self):
        self.enter, self.out = 0, 0
        self.validation, self.testing = 0, 0
        self.training, self.y = 0, 0

lib = lib()

class Plot(QtGui.QMainWindow):
    def __init__(self, parent=None): 
        super(Plot,self).__init__(parent)
        self.page_3 = Ui_page_plotting()
        self.page_3.setupUi(self)

        self.move(QtGui.QDesktopWidget().availableGeometry().center().x() - self.geometry().width()/2,\
                  QtGui.QDesktopWidget().availableGeometry().center().y() - self.geometry().height()/2)

        self.page_3.pb_back.clicked.connect(self.back)
        self.predict_plot()
        
    def predict_plot(self):
        self.page_3.wt_graphs.canvas.ax.clear()
        self.page_3.wt_graphs.canvas.ax.plot(np.linspace(1, lib.training, lib.training),
                                             lib.enter[:lib.training],
                                             label='Data',
                                             color='black')
        self.page_3.wt_graphs.canvas.ax.plot(np.linspace(1, lib.training, lib.training),
                                                         lib.y,
                                                         label='predict',
                                                         color='red')
        self.page_3.wt_graphs.canvas.ax.legend(loc='best')
        self.page_3.wt_graphs.canvas.ax.set_title('Prediction x Real Magnetic Measuring')
        self.page_3.wt_graphs.canvas.ax.set_ylabel('[rad]')
        self.page_3.wt_graphs.canvas.ax.set_xlabel('# samples')
        self.page_3.wt_graphs.canvas.fig.tight_layout()
        self.page_3.wt_graphs.canvas.draw()

    def back(self):
        self.close()    
        
class Capture(object):
    def __init__(self, entrada, saida, train, val, test, y):
        lib.enter, lib.out = entrada, saida
        lib.validation, lib.testing = val, test
        lib.training, lib.y = train, y
    
