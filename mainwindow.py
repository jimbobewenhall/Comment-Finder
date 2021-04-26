from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot


class Ui_MainWindow(QObject):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 642)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 10, 181, 151))
        self.graphicsView.setObjectName("graphicsView")

        self.graphicsView_2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(610, 10, 181, 151))
        self.graphicsView_2.setObjectName("graphicsView_2")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 180, 451, 51))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.returnPressed.connect(self.returnPressedSlot)

        self.browseButton = QtWidgets.QPushButton(self.centralwidget)
        self.browseButton.setGeometry(QtCore.QRect(580, 180, 111, 51))
        self.browseButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.browseButton.setObjectName("browseButton")
        self.browseButton.clicked.connect(self.browseSlot)

        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(100, 250, 591, 31))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")

        self.applyButton = QtWidgets.QPushButton(self.centralwidget)
        self.applyButton.setGeometry(QtCore.QRect(260, 290, 111, 71))
        self.applyButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.applyButton.setObjectName("applyButton")
        self.applyButton.clicked.connect(self.applySlot)

        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        self.clearButton.setGeometry(QtCore.QRect(410, 290, 111, 71))
        self.clearButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clearButton.setObjectName("clearButton")
        self.clearButton.clicked.connect(self.clearSlot)

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(90, 380, 621, 181))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setObjectName("tableWidget")

        self.Export = QtWidgets.QPushButton(self.centralwidget)
        self.Export.setGeometry(QtCore.QRect(320, 570, 141, 41))
        self.Export.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Export.setObjectName("Export")
        self.Export.clicked.connect(self.exportSlot)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "File name"))
        self.browseButton.setText(_translate("MainWindow", "Browse"))
        self.applyButton.setText(_translate("MainWindow", "Apply"))
        self.clearButton.setText(_translate("MainWindow", "Clear"))
        self.Export.setText(_translate("MainWindow", "Export"))

    @pyqtSlot()
    def applySlot(self):
        pass

    @pyqtSlot()
    def clearSlot(self):
        pass

    @pyqtSlot()
    def exportSlot(self):
        pass

    @pyqtSlot()
    def browseSlot(self):
        pass

    def table_update(self, df):
        self.tableWidget.setRowCount(df.shape[0])
        self.tableWidget.setColumnCount(df.shape[1])
        self.tableWidget.setHorizontalHeaderLabels(df.columns.values.tolist())
        self.tableWidget.resizeColumnsToContents()
        for x in range(df.shape[0]):
            for y in range(df.shape[1]):
                self.tableWidget.setItem(x, y, QtWidgets.QTableWidgetItem(str(df.iloc[x,y])))
        QtCore.QCoreApplication.processEvents()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
