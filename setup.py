from commentFinder import *
from mainwindow import *
from model import *
from PyQt5 import sip
import sip
import PyQt5.sip
from docx import Document
from lxml import etree
import zipfile
import docx
from docx import *
import pandas as pd
from mainwindow import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot
from mainwindow import Ui_MainWindow
import sys
import xlwt


from cx_Freeze import setup, Executable


setup(name = "reandurllib" ,
      version = "0.1" ,
      description = "" ,
      executables = [Executable("App.py")])