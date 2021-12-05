import sys

# from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QComboBox, QLabel, QGridLayout, QCheckBox, QGroupBox
from PyQt5.QtWidgets import (QMainWindow, QApplication, QWidget, QPushButton, QAction, QComboBox, QLabel,
                             QGridLayout, QCheckBox, QGroupBox, QVBoxLayout, QHBoxLayout, QLineEdit, QPlainTextEdit)

from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import Qt

from itertools import cycle

from PyQt5.QtWidgets import QDialog, QVBoxLayout, QSizePolicy, QMessageBox

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import pandas as pd
import numpy as np
from numpy.polynomial.polynomial import polyfit

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve, auc
from sklearn.preprocessing import label_binarize

# Libraries to display decision tree
from pydotplus import graph_from_dot_data
from sklearn.tree import export_graphviz
import webbrowser

import warnings

warnings.filterwarnings("ignore")
import matplotlib.pyplot as plt

import random
import seaborn as sns

# %%-----------------------------------------------------------------------
import os

os.environ["PATH"] += os.pathsep + 'C:\\Program Files (x86)\\graphviz-2.38\\release\\bin'
# %%-----------------------------------------------------------------------


#::--------------------------------
# Default font size for all the windows
#::--------------------------------
font_size_window = 'font-size:18px'


class estimator(QMainWindow):
    send_fig = pyqtSignal(str)

    def __init__(self, para_list):
        self.f_in = lambda x: para_list[0] + float(x[0]) * para_list[1]
        self.f_out = lambda x: para_list[2] + float(x[1]) * para_list[3]

        self.Title = "Estimator"
        self.initUi()

    def pred(self, x):
        if type(x) != str:
            return 'please input, cannot interpret'
        xlist = x.split(',')
        if len(xlist) != 2:
            return 'please input number of parameters'
        predin = self.f_in(xlist)
        predout = self.f_out(xlist)

        return 'estimated fatality caused by indoor pollution is ' + str(
            predin) + 'estimated fatality caused by indoor pollution is ' + str(predout)

    def info(self):
        return 'enter the quantity of GDP and rate to estimate fataility per 100,000 people'


def main():
    #::-------------------------------------------------
    # Initiates the application
    #::-------------------------------------------------
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    ex = App()
    ex.show()
    sys.exit(app.exec_())


class App(QMainWindow):
    #::-------------------------------------------------------
    # This class creates all the elements of the application
    #::-------------------------------------------------------

    def __init__(self):
        super().__init__()
        self.left = 500
        self.top = 500
        self.Title = 'Effect of Pollution on Deaths'
        self.width = 800
        self.height = 600
        self.initUI()

    def initUI(self):
        #::- Creates the me nu and the items

        self.setWindowTitle(self.Title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        #::-----------------------------
        # Create the menu bar
        # and three items for the menu, File, EDA Analysis and ML Models
        #::-----------------------------
        mainMenu = self.menuBar()
        mainMenu.setStyleSheet('background-color: lightblue')

        fileMenu = mainMenu.addMenu('File')
        RegressionMenu = mainMenu.addMenu('Regression Analysis')

        #::--------------------------------------
        # Exit application
        # Creates the actions for the fileMenu item
        #::--------------------------------------

        exitButton = QAction(QIcon('enter.png'), 'Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)

        fileMenu.addAction(exitButton)


def GDP_pollution():
    #::- Defining the data set
    # input needed global GDP
    ## input needed global nitrogen
    global X
    global y
    global features_list
    global class_names
    pollution = pd.read_csv('Country wise GDP from 1994 to 2017.csv')
    X = pollution["GDP"]
    y = pollution[""]
    # Input needed ff_happiness = pd.read_csv('final_happiness_dataset.csv')
    ## input needed features_list = []
    class_names = ['Deaths']


if __name__ == '__main__':
    # Reading the Data and calling for the application
    #GDP_pollution()
    main()
