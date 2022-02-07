import os
import sys

from PyQt5 import QtWidgets

from client import Client
from server import Server
from UI.login import Ui_MainWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    ##client instance
    clientIns = Client()
    
    ##client instance
    serverIns = Server()
    
    ui = Ui_MainWindow(clientIns)
    ui.startUI()
    ui.show()
    
    sys.exit(app.exec_())
