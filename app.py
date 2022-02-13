import os
import sys

from PyQt5 import QtWidgets

from client import Client
from UI.login import Ui_MainWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    ##client instance
    clientIns = Client()
    
    ui = Ui_MainWindow(clientIns)
    ui.startUI()
    ui.show()
    
    sys.exit(app.exec_())
