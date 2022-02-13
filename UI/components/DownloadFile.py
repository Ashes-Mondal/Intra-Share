from PyQt5 import QtWidgets, QtGui, QtCore

from UI.components.ReceiveFileThread import ReceiveFileThread
from .utils import getSizeStr
from PyQt5.QtWidgets import QMessageBox


class DownloadFile(QtWidgets.QVBoxLayout):
    def __init__(self, file:tuple, fileID: int, parent, dwnloadThread, isPaused: bool, clientIns, removeDownload, filepath: str, removeDownloadFile, downloadFileProgress):
        super(DownloadFile, self).__init__()
        self.removeDownloadFile = removeDownloadFile
        self.downloadFileProgress = downloadFileProgress
        self.filepath = filepath
        self.removeDownload = removeDownload
        self.dwnloadThread = dwnloadThread
        if self.dwnloadThread != None:
            self.dwnloadThread.stopSig.connect(self.stopFileTransfer)
        self.clientIns = clientIns
        self.isPaused = isPaused
        self.fileID = fileID
        self.file = file
        fileName, fileSize, userID, username, status = file
        self.completed_bytes = 0
        if self.fileID in self.clientIns.activeClients[userID].fileTaking.keys():
            k = self.clientIns.activeClients[userID].fileTaking[self.fileID]
            self.completed_bytes = k[1]
        # print("fileID completed_bytes:",self.completed_bytes)
        self.parent = parent
        self.setObjectName("DownloadFile" + str(fileID))
        _translate = QtCore.QCoreApplication.translate

        self.dlFileInfoHbox = QtWidgets.QHBoxLayout()
        self.dlFileInfoHbox.setContentsMargins(-1, -1, 0, -1)
        self.dlFileInfoHbox.setObjectName("dlFileInfoHbox" + str(fileID))

        self.dlFileInfo = QtWidgets.QLabel(self.parent)
        self.dlFileInfo.setStyleSheet(
            "text-align: left;\n"
            "margin-top: 10px;\n"
            "color: rgb(85, 0, 127);\n"
            "font: 75 10pt \"Verdana\";"
        )
        self.dlFileInfo.setObjectName("dlFileInfo" + str(fileID))
        info = fileName[:20] + " | " + \
            username + " | " + getSizeStr(int(fileSize))
        self.dlFileInfo.setText(_translate("MainWindow", info))
        self.dlFileInfo.setToolTip(fileName)
        self.dlFileInfoHbox.addWidget(self.dlFileInfo)
        self.addLayout(self.dlFileInfoHbox)

        self.dlFileProgressHbox = QtWidgets.QHBoxLayout()
        self.dlFileProgressHbox.setObjectName(
            "dlFileProgressHbox" + str(fileID))

        self.dlProgressBar = QtWidgets.QProgressBar(self.parent)
        self.dlProgressBar.setProperty("value", round((self.completed_bytes/int(fileSize))*100))
        self.dlProgressBar.setObjectName("dlProgressBar" + str(fileID))
        self.dlFileProgressHbox.addWidget(self.dlProgressBar)

        self.pOr = QtWidgets.QPushButton(self.parent)
        self.pOr.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pOr.clicked.connect(self.PauseOrPlay)
        self.pOr.setStyleSheet(
            "QPushButton {\n"
            "font-size: 25px;\n"
            "border-radius: 20px;\n"
            "padding: 4;\n"
            "background-color: rgb(237, 237, 237);\n"
            "}\n"
            "QPushButton::hover {\n"
            "    border: 2px solid #ffffff;\n"
            "    background-color: #ffffff;\n"
            "}\n"
        )
        if self.dwnloadThread == None:
            self.pOr.setIcon(QtGui.QIcon('images/play.png'))
            self.pOr.setIconSize(QtCore.QSize(32, 32))
        else:
            self.pOr.setIcon(QtGui.QIcon('images/pause.png'))
            self.pOr.setIconSize(QtCore.QSize(32, 32))

        self.clear = QtWidgets.QPushButton(self.parent)
        self.clear.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clear.clicked.connect(self.clearDownload)
        self.clear.setStyleSheet(
            "QPushButton {\n"
            "font-size: 25px;\n"
            "border-radius: 20px;\n"
            "padding: 4;\n"
            "background-color: rgb(237, 237, 237);\n"
            "}\n"
            "QPushButton::hover {\n"
            "    border: 2px solid #ffffff;\n"
            "    background-color: #ffffff;\n"
            "}\n"
        )
        self.clear.setIcon(QtGui.QIcon('images/cancel.png'))
        self.clear.setIconSize(QtCore.QSize(32, 32))

        self.dlFileProgressHbox.addWidget(self.pOr)
        self.dlFileProgressHbox.addWidget(self.clear)

        self.dlFileProgressHbox.setStretch(0, 25)
        self.dlFileProgressHbox.setStretch(1, 1)
        self.addLayout(self.dlFileProgressHbox)

    def PauseOrPlay(self):
        if self.clientIns.activeClients[self.file[2]].online:
            if self.dwnloadThread == None:
                self.openReceiveFileThread()
                self.isPaused = False
                self.pOr.setIcon(QtGui.QIcon('images/pause.png'))
                self.pOr.setIconSize(QtCore.QSize(32, 32))
            else:
                self.dwnloadThread.PauseOrPlay()
                if self.isPaused:
                    self.isPaused = False
                    self.pOr.setIcon(QtGui.QIcon('images/pause.png'))
                    self.pOr.setIconSize(QtCore.QSize(32, 32))
                else:
                    self.isPaused = True
                    self.pOr.setIcon(QtGui.QIcon('images/play.png'))
                    self.pOr.setIconSize(QtCore.QSize(32, 32))
        else:
            ret = QMessageBox.warning(self.parent, 'Failed to start!',
                                      f"{self.file[3]} not online!", QMessageBox.Ok, QMessageBox.Cancel)

    def clearDownload(self):
        if self.isPaused == False:
            self.isPaused = True
            self.pOr.setIcon(QtGui.QIcon('images/play.png'))
            self.pOr.setIconSize(QtCore.QSize(32, 32))
            self.dwnloadThread.PauseOrPlay()
            
        ret = QMessageBox.question(self.parent, 'Are you sure?', "Do you want to remove the file from downloads?",
                                   QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if ret == QMessageBox.Yes:
            if self.dwnloadThread:
                self.dwnloadThread.exit(0)
            self.removeDownload(userID=self.file[2], fileID=self.fileID)
            print("CLEARED RUNNED!" )

    def openReceiveFileThread(self):
        fileName, fileSize, userID, username, status = self.file
        print(userID, self.fileID, fileName, int(fileSize), self.filepath)
        parameters = self.clientIns.downloadFile(userID, self.fileID, fileName, int(fileSize), self.filepath)
        self.dwnloadThread = ReceiveFileThread(parameters)
        self.dwnloadThread.finished.connect(lambda: print(f"dwnloadThread finished {self.fileID}"))
        self.dwnloadThread.finishedSig.connect(self.removeDownloadFile)
        self.dwnloadThread.progress.connect(self.downloadFileProgress)
        self.dwnloadThread.stopSig.connect(self.stopFileTransfer)
        self.completed_bytes = self.dwnloadThread.file[-1]
        self.dlProgressBar.setProperty("value", self.completed_bytes)
        self.dwnloadThread.start()

    def stopFileTransfer(self):
        print("stopFileTransfer called")
        del self.dwnloadThread
        self.dwnloadThread = None
        if self.isPaused == False:
            self.isPaused = True
            self.pOr.setIcon(QtGui.QIcon('images/play.png'))
            self.pOr.setIconSize(QtCore.QSize(32, 32))
        self.clientIns.activeClients[self.file[2]].fileTaking[self.fileID][3] = None
