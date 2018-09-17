from PyQt5.uic.properties import QtWidgets
import sys
import login
from login import *
from MainWinC import *
from PyQt5.QtWidgets import QApplication,QMainWindow

class Client(Ui_LoginWin,Ui_MainWindowC):
    def __init__(self):
        MainWindow = QMainWindow()
        ui = login.Ui_LoginWin()
        ui.setupUi(MainWindow)
        MainWindow.show()

if __name__ == '__main__':
    app=QApplication(sys.argv)
    ClientP=Client()
    sys.exit(app.exec_())