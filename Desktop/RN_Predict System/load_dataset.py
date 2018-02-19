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
Created on 19/07/2017
@author: lucas.balthazar

Main script to open the files
'''
#Import Library
import numpy as np
import time
import datetime
import sys
import pandas as pd
from PySide import QtGui

class Cross_check(object):
    def __init__(self):
        self.file = np.array([])
        self.Raw = np.array([])
        self.Current = np.array([])
        self.Multipoles = np.array([])
        self.Curves = np.array([])
        self.multipoleseries = pd.Series()
        self.curveseries = pd.Series()
        self.multipoledf = None
        self.curvesdf = None
        ## Desloc_Y ##
        self.dip_skew = None
        self.quad_normal = None
        ## Desloc_X ##
        self.dip_normal = None
        self.deslo_y = None
        self.deslo_x = None
        
        
    def Load_Files(self):
        """
        Load the input files.
        """
        app=QtGui.QApplication.instance()
        if not app:
            app = QtGui.QApplication(sys.argv)
        file_path = QtGui.QFileDialog.getOpenFileNames()
        self.files = self.sortList(file_path[0])
        self.Load_Data()

    def sortList(self,list):            #Função pega todos os dados e organiza-os por data de entrada, impossibilitando as informções aleatórias.
        index = np.array([])
        for i in range(len(list)):
            index = np.append(index, time.mktime(datetime.datetime.strptime(list[i][list[i].find('.dat')-13:list[i].find('.dat')], '%y%m%d_%H%M%S').timetuple()))
        index = index.argsort()

        File_List = np.array([])
        for i in range(len(list)):
            File_List = np.append(File_List,list[index[i]])

        return File_List

    def Load_Data(self):                #Função pega todos os dados da bobina e organiza-os.
        #try:
        self.Data = np.array([])
        n = len(self.files)
        for i in range(n):
            self.Data = np.append(self.Data, Cross_check())
            self.Data[i].file = self.files[i] 
            arq = open(self.Data[i].file)
            self.Data[i].Raw = np.array(arq.read().splitlines())

            #Read Currents
            index_current = np.where(np.char.find(self.Data[i].Raw,'main_coil_current_avg') > -1)[0][0]
            current = float(self.Data[i].Raw[index_current].split('\t')[1])
            self.Data[i].Current = current

            # Read Multipoles
            index_multipoles = np.where(np.char.find(self.Data[i].Raw,'Reading Data') > -1)[0][0] + 3
            multipoles = self.Data[i].Raw[index_multipoles:index_multipoles+15]
            for value in multipoles:
                self.Data[i].Multipoles = np.append(self.Data[i].Multipoles,value.split('\t'))
            self.Data[i].Multipoles = self.Data[i].Multipoles.reshape(15,13).astype(np.float64)

            # Read Curves
            index_curves = np.where(np.char.find(self.Data[i].Raw,'Raw Data Stored') > -1)[0][0] + 3 
            curves = self.Data[i].Raw[index_curves:]
            for value in curves:
                self.Data[i].Curves = np.append(self.Data[i].Curves,value[:-1].split('\t'))
            self.Data[i].Curves = self.Data[i].Curves.reshape(int(len(curves)),int(len(self.Data[i].Curves)/len(curves))).astype(np.float64) * 1e-12

        #Read Columns names
        index_multipoles = np.where(np.char.find(self.Data[0].Raw,'Reading Data') > -1)[0][0] + 2
        self.Columns = np.array(self.Data[0].Raw[index_multipoles].split('\t'))
        self.makeTable()
        self.displacement()
        #except:
         #     print('Fail')
                
    def makeTable(self):        
        for i in range(len(self.Data)):
            self.Data[i].multipoleseries = self.Data[i].multipoleseries.append(pd.Series([self.Data[i].Multipoles],index=[self.Data[i].Current]))
            self.Data[i].curveseries = self.Data[i].curveseries.append(pd.Series([self.Data[i].Curves],index=[self.Data[i].Current]))
         
            self.Data[i].multipoledf = pd.DataFrame(self.Data[i].multipoleseries.iloc[0], 
                                                    columns=self.Columns,
                                                    index=np.char.mod('%d',np.linspace(1, 15, 15)))
            
            _npoints = self.Data[i].curveseries.iloc[0].shape[0]
            _ncurves = self.Data[i].curveseries.iloc[0].shape[1]
            
            self.Data[i].curvesdf = pd.DataFrame(self.Data[i].curveseries.iloc[0],
                                                 index = np.char.mod('%d',np.linspace(1, _npoints, _npoints)),
                                                 columns = np.char.mod('%d',np.linspace(1, _ncurves, _ncurves)))
    def displacement(self):
        for i in range(len(self.Data)):
            #Dipolo skew
            self.Data[i].dip_skew = self.Data[i].multipoledf.iloc[:,3][0]
            #Dipolo normal
            self.Data[i].dip_normal = self.Data[i].multipoledf.iloc[:,1][0]
            #Quadrupolo normal
            self.Data[i].quad_normal = self.Data[i].multipoledf.iloc[:,1][1]
            #Cálculo do deslocamento Y (para Quadrupolo)
            self.Data[i].deslo_y = (self.Data[i].dip_skew/self.Data[i].quad_normal/1e-6)
            #Cálculo do deslocamento X (para Quadrupolo)
            self.Data[i].deslo_x = (self.Data[i].dip_normal/self.Data[i].quad_normal/1e-6)


##if __name__ == '__main__':
##    load_dataset = Cross_check()
##    load_dataset.Load_Files()

