from PyQt5 import QtWidgets, QtGui, QtCore
from .utils import ext_ico_path


class DownloadFile(QtWidgets.QVBoxLayout):
    def __init__(self, details: dict, parent):
        super(DownloadFile, self).__init__()
        self.details = details
        self.parent = parent
        self.setObjectName(details["fileName"] + "_Hbox")
        _translate = QtCore.QCoreApplication.translate

        self.dlFileInfoHbox = QtWidgets.QHBoxLayout()
        self.dlFileInfoHbox.setContentsMargins(-1, -1, 0, -1)
        self.dlFileInfoHbox.setObjectName(
            "dlFileInfoHbox" + details["fileName"])

        self.dlFileInfo = QtWidgets.QLabel(self.parent)
        self.dlFileInfo.setStyleSheet(
            "text-align: left;\n"
            "margin-top: 10px;\n"
            "color: rgb(85, 0, 127);\n"
            "font: 75 10pt \"Verdana\";"
        )
        self.dlFileInfo.setObjectName("dlFileInfo" + details["fileName"])
        info = details["fileName"][:20] + " | " + \
            details["owner"] + " | " + details["size"]
        self.dlFileInfo.setText(_translate("MainWindow", info))
        self.dlFileInfo.setToolTip(details["fileName"])
        self.dlFileInfoHbox.addWidget(self.dlFileInfo)
        self.addLayout(self.dlFileInfoHbox)

        self.dlFileProgressHbox = QtWidgets.QHBoxLayout()
        self.dlFileProgressHbox.setObjectName("dlFileProgressHbox")

        self.dlProgressBar = QtWidgets.QProgressBar(self.parent)
        self.dlProgressBar.setProperty("value", 95)
        self.dlProgressBar.setObjectName("dlProgressBar")
        self.dlFileProgressHbox.addWidget(self.dlProgressBar)

        self.pOr = QtWidgets.QPushButton(self.parent)
        self.pOr.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
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
        self.pOr.setIcon(QtGui.QIcon('images/pause.png'))
        self.pOr.setIconSize(QtCore.QSize(32, 32))
        self.dlFileProgressHbox.addWidget(self.pOr)

        self.dlFileProgressHbox.setStretch(0, 25)
        self.dlFileProgressHbox.setStretch(1, 1)
        self.addLayout(self.dlFileProgressHbox)
