from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot
from mainwindow import Ui_MainWindow
import sys
from model import Model
import xlwt


class MainWindowUIClass(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.model = Model()

    def setupUi(self, MW):
        super().setupUi(MW)

    def refreshAll(self):
        self.lineEdit.setText(self.model.getFileName())

    def returnPressedSlot(self):
        fileName = self.lineEdit.text()
        if self.model.isValid(fileName):
            self.model.setFileName(self.lineEdit.text())
            self.refreshAll()
        else:
            m = QtWidgets.QMessageBox()
            m.setText("Invalid file name!\n" + fileName)
            m.setIcon(QtWidgets.QMessageBox.Warning)
            m.setStandardButtons(QtWidgets.QMessageBox.Ok
                                 | QtWidgets.QMessageBox.Cancel)
            m.setDefaultButton(QtWidgets.QMessageBox.Cancel)
            ret = m.exec_()
            self.lineEdit.setText("")
            self.refreshAll()

    def browseSlot(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
            None,
            "QFileDialog.getOpenFileName()",
            "",
            "All Files (*);;Python Files (*.py)",
            options=options)
        if fileName:
            self.model.setFileName(fileName)
            self.refreshAll()

    def applySlot(self):
        df = self.model.apply(self.progressBar)
        self.table_update(df)

    def clearSlot(self):
        self.tableWidget.setRowCount(0)
        self.model.clear()

    def exportSlot(self):
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(None, 'Save File', '', ".xls(*.xls)")
        wbk = xlwt.Workbook()
        sheet = wbk.add_sheet(sheetname='Sheet1', cell_overwrite_ok=True)
        style = xlwt.XFStyle()
        model = self.tableWidget.model()
        for c in range(model.columnCount()):
            text = model.headerData(c, QtCore.Qt.Horizontal)
            sheet.write(0, c + 1, text, style=style)

        for r in range(model.rowCount()):
            text = model.headerData(r, QtCore.Qt.Vertical)
            sheet.write(r + 1, 0, text, style=style)

        for c in range(model.columnCount()):
            for r in range(model.rowCount()):
                text = model.data(model.index(r, c))
                sheet.write(r + 1, c + 1, text)

        wbk.save(filename)

def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainWindowUIClass()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

main()