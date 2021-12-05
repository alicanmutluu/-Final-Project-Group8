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
    #--------------------------------------------------------------------------------
    # Implementation of Estimator using the (fill this)  dataset
    # the methods in this class are
    #       _init_ : initialize the class
    #       initUi : creates the canvas and all the elements in the canvas
    #       update : populates the elements of the canvas base on the parameters
    #               chosen by the user
    #---------------------------------------------------------------------------------
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

    def initUi(self):
        #::-----------------------------------------------------------------
        #  Create the canvas and all the element to create a dashboard with
        #  all the necessary elements to present the results from the algorithm
        #  The canvas is divided using a  grid loyout to facilitate the drawing
        #  of the elements
        #::-----------------------------------------------------------------

        self.setWindowTitle(self.Title)
        self.setStyleSheet(font_size_window)

        self.main_widget = QWidget(self)

        self.layout = QGridLayout(self.main_widget)

        self.groupBox1 = QGroupBox('Ed Estimator')
        self.groupBox1Layout= QGridLayout()   # Grid
        self.groupBox1.setLayout(self.groupBox1Layout)

        # We create a checkbox of each Features
        self.feature0 = QCheckBox(features_list[0],self)
        self.feature1 = QCheckBox(features_list[1],self)
        self.feature2 = QCheckBox(features_list[2], self)
        self.feature3 = QCheckBox(features_list[3], self)
        self.feature4 = QCheckBox(features_list[4],self)
        self.feature5 = QCheckBox(features_list[5],self)
        self.feature6 = QCheckBox(features_list[6], self)
        self.feature7 = QCheckBox(features_list[7], self)
        self.feature0.setChecked(True)
        self.feature1.setChecked(True)
        self.feature2.setChecked(True)
        self.feature3.setChecked(True)
        self.feature4.setChecked(True)
        self.feature5.setChecked(True)
        self.feature6.setChecked(True)
        self.feature7.setChecked(True)

        self.lblPercentTest = QLabel('Percentage for Test :')
        self.lblPercentTest.adjustSize()

        self.txtPercentTest = QLineEdit(self)
        self.txtPercentTest.setText("80")

        self.btnExecute = QPushButton("ED Estimator")
        self.btnExecute.clicked.connect(self.update)

        self.groupBox1Layout.addWidget(self.feature0,0,0)
        self.groupBox1Layout.addWidget(self.feature1,0,1)
        self.groupBox1Layout.addWidget(self.feature2,1,0)
        self.groupBox1Layout.addWidget(self.feature3,1,1)
        self.groupBox1Layout.addWidget(self.feature4,2,0)
        self.groupBox1Layout.addWidget(self.feature5,2,1)
        self.groupBox1Layout.addWidget(self.feature6,3,0)
        self.groupBox1Layout.addWidget(self.feature7,3,1)
        self.groupBox1Layout.addWidget(self.lblPercentTest,4,0)
        self.groupBox1Layout.addWidget(self.txtPercentTest,4,1)
        self.groupBox1Layout.addWidget(self.btnExecute,5,0)

        self.groupBox2 = QGroupBox('Results from the model')
        self.groupBox2Layout = QVBoxLayout()
        self.groupBox2.setLayout(self.groupBox2Layout)

        self.lblResults = QLabel('Results:')
        self.lblResults.adjustSize()
        self.txtResults = QPlainTextEdit()
        self.lblAccuracy = QLabel('Accuracy:')
        self.txtAccuracy = QLineEdit()

        self.groupBox2Layout.addWidget(self.lblResults)
        self.groupBox2Layout.addWidget(self.txtResults)
        self.groupBox2Layout.addWidget(self.lblAccuracy)
        self.groupBox2Layout.addWidget(self.txtAccuracy)

    def update(self):
        '''
        Estimator
        Populating the dashboard using the parameters chosen by the user
          then the results are presented in graphics and reports in the canvas
        :return:None
        '''

        # processing the parameters

        self.list_corr_features = pd.DataFrame([])
        if self.feature0.isChecked():
            if len(self.list_corr_features)==0:
                ##self.list_corr_features = feature_dataset_name[features_list[0]]
            else:
                #self.list_corr_features = pd.concat([self.list_corr_features, feature_dataset_name[features_list[0]]],axis=1)

        if self.feature1.isChecked():
            if len(self.list_corr_features) == 0:
                self.list_corr_features = feature_dataset_name[features_list[1]]
            else:
                self.list_corr_features = pd.concat([self.list_corr_features, feature_dataset_name[features_list[1]]],axis=1)

        if self.feature2.isChecked():
            if len(self.list_corr_features) == 0:
                self.list_corr_features = feature_dataset_name[features_list[2]]
            else:
                self.list_corr_features = pd.concat([self.list_corr_features, feature_dataset_name[features_list[2]]],axis=1)

        if self.feature3.isChecked():
            if len(self.list_corr_features) == 0:
                self.list_corr_features = feature_dataset_name[features_list[3]]
            else:
                self.list_corr_features = pd.concat([self.list_corr_features, ff_happiness[features_list[3]]],axis=1)

        if self.feature4.isChecked():
            if len(self.list_corr_features) == 0:
                self.list_corr_features = feature_dataset_name[features_list[4]]
            else:
                self.list_corr_features = pd.concat([self.list_corr_features, ff_happiness[features_list[4]]],axis=1)

        if self.feature5.isChecked():
            if len(self.list_corr_features) == 0:
                self.list_corr_features = feature_dataset_name[features_list[5]]
            else:
                self.list_corr_features = pd.concat([self.list_corr_features, ff_happiness[features_list[5]]],axis=1)

        if self.feature6.isChecked():
            if len(self.list_corr_features) == 0:
                self.list_corr_features = feature_dataset_name[features_list[6]]
            else:
                self.list_corr_features = pd.concat([self.list_corr_features, ff_happiness[features_list[6]]],axis=1)

        if self.feature7.isChecked():
            if len(self.list_corr_features) == 0:
                self.list_corr_features = feature_dataset_name[features_list[7]]
            else:
                self.list_corr_features = pd.concat([self.list_corr_features, ff_happiness[features_list[7]]],axis=1)


        vtest_per = float(self.txtPercentTest.text())

        # Clear the graphs to populate them with the new information

        self.ax1.clear()
        self.ax2.clear()
        self.ax3.clear()
        self.ax4.clear()
        self.txtResults.clear()
        self.txtResults.setUndoRedoEnabled(False)

        vtest_per = vtest_per / 100

        # Assign the X and y to run the Random Forest Classifier

        X_dt =  self.list_corr_features
        y_dt = feature_dataset_name["Happiness.Scale"]

        class_le = LabelEncoder()

        # fit and transform the class

        y_dt = class_le.fit_transform(y_dt)

        # split the dataset into train and test

        X_train, X_test, y_train, y_test = train_test_split(X_dt, y_dt, test_size=vtest_per, random_state=100)

        # perform training with entropy.
        # Decision tree with entropy

        #specify random forest classifier
        self.clf_rf = RandomForestClassifier(n_estimators=100, random_state=100)

        # perform training
        self.clf_rf.fit(X_train, y_train)

        #-----------------------------------------------------------------------

        # predicton on test using all features
        y_pred = self.clf_rf.predict(X_test)
        y_pred_score = self.clf_rf.predict_proba(X_test)


        # confusion matrix for RandomForest
        conf_matrix = confusion_matrix(y_test, y_pred)

        # clasification report

        self.ff_class_rep = classification_report(y_test, y_pred)
        self.txtResults.appendPlainText(self.ff_class_rep)

        # accuracy score

        self.ff_accuracy_score = accuracy_score(y_test, y_pred) * 100
        self.txtAccuracy.setText(str(self.ff_accuracy_score))




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
