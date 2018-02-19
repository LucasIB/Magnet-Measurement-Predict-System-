#from rn_predict import *
#import rn_predict
import load_dataset
import page_arch_train
import page_train
import plot
from PyQt4 import QtGui, QtCore

#try:
#    _fromUtf8 = QtCore.QString.fromUtf8
#except AttributeError:
#    def _fromUtf8(s):
#        return s

def createIntroPage():
    page = QtGui.QWizardPage()
    page.setTitle("Introduction to Neural Network for Magnet Measurements")

    #Labels of the introduction page
    label3 = QtGui.QLabel("Welcome to Neural Network IMA Software!\n\n"
                         "The objective is to outline the best way to predict the behavior of "
                          "the characteristics associated with magnetic measurements and to carry "
                          "out a parallel between the actual and predicted measurements.\n\n")

    label2 = QtGui.QLabel(" ")
    
    label = QtGui.QLabel("This software was developed by IMA Group. All rights reserved.")
    label.setAlignment(QtCore.Qt.AlignCenter)

    #Auto format label                     
    label.setWordWrap(True)
    label2.setWordWrap(True)
    label3.setWordWrap(True)
    label3.adjustSize()

    #Adds labels on widget
    layout = QtGui.QVBoxLayout()
    layout.addWidget(label2)
    layout.addWidget(label3)
    layout.addWidget(label2)
    layout.addWidget(label)
    
    page.setLayout(layout)

    return page

def createRegistrationPage():
    page = QtGui.QWizardPage()
    page.setTitle("Dataset registration")
    page.setSubTitle("Please fill field with name of your dataset")

    nameLabel, nameLineEdit  = QtGui.QLabel("Dataset name:"), QtGui.QLineEdit()
    nameLabel.setBuddy(nameLineEdit)
    
    groupBox = QtGui.QGroupBox("C&onstructor")
  
    qobjectCtorRadioButton = QtGui.QRadioButton("&QObject-style constructor")
    qwidgetCtorRadioButton = QtGui.QRadioButton("Q&Widget-style constructor")
    defaultCtorRadioButton = QtGui.QRadioButton("&Default constructor")
    copyCtorCheckBox = QtGui.QCheckBox("&Generate copy constructor and operator=")

    defaultCtorRadioButton.setChecked(True)

    defaultCtorRadioButton.toggled.connect(copyCtorCheckBox.setEnabled)


    groupBoxLayout = QtGui.QVBoxLayout()
    groupBoxLayout.addWidget(qobjectCtorRadioButton)
    groupBoxLayout.addWidget(qwidgetCtorRadioButton)
    groupBoxLayout.addWidget(defaultCtorRadioButton)
    groupBoxLayout.addWidget(copyCtorCheckBox)
    groupBox.setLayout(groupBoxLayout)

    layout = QtGui.QGridLayout()
    layout.addWidget(nameLabel, 0, 0)
    layout.addWidget(nameLineEdit, 0, 1)
    layout.addWidget(groupBox, 3, 0, 1, 2)
    page.setLayout(layout)

    return page

def createIntroductionPage():
    page = QtGui.QWizardPage()
    page.setTitle("Background Information")

    intro_groupBox_2 = QtGui.QGroupBox("Overview")

    label_0 = QtGui.QLabel("The Neural Fitting will help you select data and train a network, and evaluate its performance.\n\n "
                           "The neural network will be able to analyze and return whether the magnet is in or out of standards "
                           "through the general analysis of the magnet."
                           )
    label_0.setWordWrap(True)

    NN_groupBox_3 = QtGui.QGroupBox("Neural Network")

    label_1 = QtGui.QLabel("A feed-forward network with sigmoid hidden neurons and linear output neuron, can "
                           "fit multi-dimansional mapping problems arbitrary well, given consistent data and enough "
                           "neurons in its hidden layer.\n\n"
                           "The Neural Network works like a bellow example:"
                            )
    label_1.setWordWrap(True)

    #Neural Network image
    label_image = QtGui.QLabel()
    label_image.setPixmap(QtGui.QPixmap("imagens/neural_net2.png"))
    label_image.setScaledContents(True)

    #Layout for Intro GroupBox
    intro_gb_layout = QtGui.QVBoxLayout()
    intro_gb_layout.addWidget(label_0)
    intro_groupBox_2.setLayout(intro_gb_layout)

    #Layout for NN GroupBox
    NN_gb_layout = QtGui.QVBoxLayout()
    NN_gb_layout.addWidget(label_1)
    NN_gb_layout.addWidget(label_image)
    NN_groupBox_3.setLayout(NN_gb_layout)

    #Layout for both GroupBoxes
    mainLayout = QtGui.QVBoxLayout()
    mainLayout.addWidget(intro_groupBox_2)
    mainLayout.addWidget(NN_groupBox_3)
    page.setLayout(mainLayout)

    return page


def createConclusionPage():
    page = QtGui.QWizardPage()
    page.setTitle("Neural Network for Magnet Measurements")

    #Creating buttons on screen
    pushButton_2 = QtGui.QPushButton("Neural Network for Magnet Measurements")
    #pushButton_2.adjustSize()
    #pushButton_2.setGeometry(QtCore.QRect(0, 0, 101, 31))
    pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

    label = QtGui.QLabel("Therefore, it will be necessary to gather information or a dataset with characteristics of "
                         "previous measures and consequently classification so that the system can be trained to "
                         "identify those standards.")
    label.setWordWrap(True)

    layout = QtGui.QVBoxLayout()
    layout.addWidget(label)
    layout.addWidget(pushButton_2)#,2,2)
    page.setLayout(layout)
##    pushButton_2.clicked.connect(rn_predict.MainWindow())

    return page

def backprint():
    print("Action: back Page: " + wizard.currentPage().title())

def nextprint():
    print("Action: next Page: " + wizard.currentPage().title())

def commitprint():
    print("Action: commit Page: " + wizard.currentPage().title())

def finishprint():
    print("Action:finish Page: " + wizard.currentPage().title())

def cancelprint():
    print("Action:cancel Page: " + wizard.currentPage().title())

def init_prog():
    pass
#    #rn_predict.GUIThread()
#    rn_predict.screen()
#    QtGui.QApplication.processEvents()




if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)

    wizard = QtGui.QWizard()

    wizard.addPage(createIntroPage())
    wizard.addPage(createRegistrationPage())
    wizard.addPage(createIntroductionPage())
    wizard.addPage(createConclusionPage())
    
    wizard.setWizardStyle(wizard.ModernStyle)

    wizard.setPixmap(QtGui.QWizard.BannerPixmap,
                     QtGui.QPixmap('imagens/banner_app_medio.png'))
##                     QtGui.QPixmap('C:/Users/lucas.balthazar.ABTLUS/Desktop/RN_Predict System/imagens/logo_LNLS_png.png'))

##    wizard.setPixmap(QtGui.QWizard.LogoPixmap,
##                     QtGui.QPixmap('C:/Users/lucas.balthazar.ABTLUS/Desktop/RN_Predict System/imagens/logo_LNLS_png.png'))

##    wizard.setPixmap(QtGui.QWizard.WatermarkPixmap,
##                     QtGui.QPixmap('C:/Users/lucas.balthazar.ABTLUS/Desktop/RN_Predict System/imagens/LNLS_sal.jpg'))

##    wizard.setPixmap(QtGui.QWizard.LogoPixmap,
##                     QtGui.QPixmap('C:/Users/lucas.balthazar.ABTLUS/Desktop/RN_Predict System/imagens/lnls sirius logo_menor.png'))


##    wizard.button(QtGui.QWizard.BackButton).clicked.connect(backprint)
##    wizard.button(QtGui.QWizard.NextButton).clicked.connect(nextprint)
##    wizard.button(QtGui.QWizard.CommitButton).clicked.connect(commitprint)
    wizard.button(QtGui.QWizard.FinishButton).clicked.connect(init_prog)
##    wizard.button(QtGui.QWizard.CancelButton).clicked.connect(cancelprint)
    

    wizard.setWindowTitle("Neural Network for Magnetic Measurements - LNLS IMA Group")
    wizard.show()
##    print("Page :" + wizard.currentPage().title())

    sys.exit(wizard.exec_())
