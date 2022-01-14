from http import client
from pydoc import cli
from client import Client
from components.login import Ui_MainWindow
from PyQt5 import QtWidgets
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    clientIns = Client()
    ui = Ui_MainWindow(clientIns)
    ui.startUI()
    ui.MainWindow.show()
    clientIns.closeEvent.wait()
    sys.exit(app.exec_())
