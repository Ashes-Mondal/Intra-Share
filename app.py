import sys,os
from http import client
from pydoc import cli
from PyQt5 import QtWidgets
from client.client import Client
from server.server import Server
from ui.login import Ui_MainWindow as Login

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ##client instance
    clientIns = Client()
    serverIns = Server()
    login = Login(clientIns)
    login.startUI()
    login.MainWindow.show()
    # login.closeEvent.wait()
    sys.exit(app.exec_())
