import sys
from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import QPropertyAnimation, QPoint, QEasingCurve
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCharts import QChart, QChartView, QPieSeries, QPieSlice

import pyqtgraph as pg
from pyqtgraph.graphicsItems.PlotDataItem import dataType

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
import matplotlib.pyplot as plt
# from PySide2 import QtWidgets
# from PyQt5 import QtWidgets
from qt_material import apply_stylesheet

from dash_bo import Ui_MainWindow

import pandas as pd
import pyqtgraph as pg
from pyqtgraph.Qt import QtGui
import numpy as np
from matplotlib import cm

import seaborn as sns
import matplotlib.pyplot as ptl
#import seabornplot
import data_games



class MainWindow(QMainWindow):
    siz1= 0
    siz2= 0

    sizx= 0
    sizy= 0
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)


        self.ui.boto_menu.clicked.connect(lambda: self.move_menu(self.ui.frame_barra_menu, self.siz1, self.sizx))
        self.ui.boto_tool.clicked.connect(lambda: self.move_menu(self.ui.frame_barra_tool, self.siz2, self.sizy))
        self.ui.boto_tool.setMaximumSize(0,0)

        self.ui.boto_max.hide()
        
        ####BOTO####
        self.ui.boto_cerrar.clicked.connect(lambda: self.close())
        self.ui.boto_max.clicked.connect(lambda: self.maxi_window())
        self.ui.boto_restaurar.clicked.connect(self.rest_window)
        self.ui.boto_min.clicked.connect(self.showMinimized)

        self.ui.boto_men1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page))
        self.ui.boto_men2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        self.ui.boto_men3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))

        self.ui.combo_championName.addItems(data_games.get_list_champ())
        self.ui.combo_elo.addItems(data_games.get_list_elo())

        self.ui.boto_pred.clicked.connect(lambda: self.obtener_data_champ_all(self.ui.page,
                                        self.ui.page_2, self.ui.page_3))
        self.showMaximized()
        self.show()

    def obtener_data_champ_all(self, pag1, pag2, pag3):
        print(self.ui.combo_championName.currentText())
        #data_games.data_elo(self.ui.combo_elo.currentText())
        data= data_games.box_dens_corr_champ(self.ui.combo_championName.currentText(), self.ui.combo_elo.currentText())
        self.box_plot(data[0])

        cake= self.box_plot(data[0])
        cak1= self.dens_barr(data[0])
        cak2= self.corr_plot(data[1])

        act1= FigureCanvas(cake)
        act2= FigureCanvas(cak1)
        act3= FigureCanvas(cak2)

        act1.setStyleSheet("background-color:transparent;")
        act2.setStyleSheet("background-color:transparent;")
        act2.setStyleSheet("background-color:transparent;")

        for i in reversed(range(pag1.layout().count())):
            pag1.layout().itemAt(i).widget().setParent(None)

        for i in reversed(range(pag2.layout().count())):
            pag2.layout().itemAt(i).widget().setParent(None)
        
        for i in reversed(range(pag3.layout().count())):
            pag3.layout().itemAt(i).widget().setParent(None)

        pag1.layout().addWidget(act1)
        pag2.layout().addWidget(act2)
        pag3.layout().addWidget(act3)

        self.ui.lab_win_rate.setText(str(data[3]))
        self.ui.lab_vece_jugado.setText(str(data[2]))

        #print(data)

    def box_plot(self, sweet):
        g = sns.FacetGrid(sweet, legend_out= False)

        f,axes = ptl.subplots(2,2, figsize=(15,15))
        ordx= [0, 1, 0, 1]
        ordy= [0, 0, 1, 1]
        for column, ox, oy in zip(sweet.iloc[:, 1:], ordx, ordy):
            ax= sns.boxplot(sweet[column], ax=axes[ox, oy])
        #plt.show()
        fig = ax.get_figure()
        return fig

    def dens_barr(self, sweet):
        g = sns.FacetGrid(sweet, legend_out= False)
        f,axes = ptl.subplots(2,2, figsize=(15,15))
        ordx= [0, 1, 0, 1]
        ordy= [0, 0, 1, 1]
        for column, ox, oy in zip(sweet.iloc[:, 1:], ordx, ordy):
                ax= sns.distplot(sweet[column], ax=axes[ox, oy])
        fig = ax.get_figure()
        return fig

    def corr_plot(self, sweet):
        correlation = sweet.corr()
        ptl.figure(figsize=(10,10))
        ax=sns.heatmap(correlation, vmax=1, square=True, annot=True, cmap="viridis")
        ptl.title("MATRIZ DE CORRELACIÓN")
        return ax.get_figure()

    def remove_widgets():
        pass        



    def move_menu(self, menu, lonx, lony):
        #self.clickPosition = event.globalPos()
        vi= menu.width()
        print('vi: ', vi)

        extend=0
        
        #self.ui.frame_barra_menu
        
        if vi==0:
            extend= lonx
            menu.setMinimumSize(extend,lony)
            #menu.setMaximumWidth(extend)
            #self.ui.frame_barra_menu.setMaximumWidth
        else:
            #self.siz1= menu.size().width()
            self.update_data()
            menu.setMaximumSize(extend,lony)
            print('oh me ejecuto')
            #self.ui.frame_barra_menu.resize(extend,844)
            #self.ui.frame_barra_menu.setGeometry()

        self.animacion = QPropertyAnimation(menu, b'minimumWidth')
        self.animacion.setDuration(400)
        self.animacion.setStartValue(vi)
        self.animacion.setEndValue(extend)
        self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animacion.start()

        print( vi, ' <> ',extend)
        print('ra: ',self.siz1, ' & ',self.sizx)
        print('ga: ',self.siz2, ' & ',self.sizy)
        #print(vi)

    def update_data(self):
        if(self.ui.frame_barra_menu.size().width()!=0):
            self.siz1=self.ui.frame_barra_menu.size().width()
        if(self.ui.frame_barra_tool.size().width()!=0):
            self.siz2=self.ui.frame_barra_tool.size().width()
        if(self.ui.frame_barra_menu.size().height()!=0):
            self.sizx=self.ui.frame_barra_menu.size().height()
        if(self.ui.frame_barra_tool.size().height()!=0):
            self.sizy=self.ui.frame_barra_tool.size().height()
	

    def rest_window(self): 
        self.showNormal()		
        self.ui.boto_restaurar.hide()
        self.ui.boto_max.show()
        self.update_data()


    def maxi_window(self): 
        self.showMaximized()
        self.ui.boto_max.hide()
        self.ui.boto_restaurar.show()
        self.update_data()

    def desplegar_ventana(self, event):
        pass



if __name__== '__main__':
    print('raaaa')
    app= QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_cyan.xml')
    window= MainWindow()
    sys.exit(app.exec_())
