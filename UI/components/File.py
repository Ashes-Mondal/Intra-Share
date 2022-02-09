from PyQt5 import QtWidgets, QtGui, QtCore
from .utils import ext_ico_path


class File(QtWidgets.QHBoxLayout):
    def __init__(self, file: dict, parent):
        super(File, self).__init__()
        self.file = file
        self.parent = parent
        self.setObjectName(file["fileName"] + "_Hbox")
        _translate = QtCore.QCoreApplication.translate

		#fileType
        path = ext_ico_path[file["type"]] if file["type"] in ext_ico_path.keys(
        ) else ext_ico_path["file"]
        self.fileType = QtWidgets.QPushButton(self.parent)
        self.fileType.setStyleSheet(
            "margin: 5px 7px;\n"
            "font-size: 15px;\n"
            "border-radius: 20px;\n"
            "padding: 4;\n"
            "background-color: rgb(237, 237, 237);"
        )
        self.fileType.setObjectName("fileType_" + file["fileName"])
        self.fileType.setIcon(QtGui.QIcon(path))
        self.fileType.setIconSize(QtCore.QSize(35, 35))


		#fileName
        self.fileName = QtWidgets.QLabel(self.parent)
        self.fileName.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.fileName.setStyleSheet(
            "text-align: center;\n"
            "padding-right: 10px;\n"
            "color: rgb(85, 0, 127);\n"
            "font: 75 11pt \"Verdana\";"
        )
        self.fileName.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.fileName.setObjectName("fileName" + file["fileName"])
        self.fileName.setText(_translate("MainWindow", file["fileName"][:20]))
        self.fileName.setToolTip(file["fileName"])

		#ownerName
        self.ownerName = QtWidgets.QLabel(self.parent)
        self.ownerName.setStyleSheet(
            "text-align: center;\n"
            "padding-left: 10;\n"
            "padding-right: 10px;\n"
            "color: rgb(85, 0, 127);\n"
            "font: 75 11pt \"Verdana\";"
        )
        self.ownerName.setAlignment(QtCore.Qt.AlignCenter)
        self.ownerName.setObjectName("ownerName" + file["fileName"])
        self.ownerName.setText(_translate("MainWindow", file["owner"].upper()))

		#fileSize
        self.fileSize = QtWidgets.QLabel(self.parent)
        self.fileSize.setStyleSheet(
            "text-align: center;\n"
            "color: rgb(85, 0, 127);\n"
            "font: 75 11pt \"Verdana\";"
        )
        self.fileSize.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.fileSize.setObjectName("fileSize" + file["fileName"])
        self.fileSize.setText(_translate("MainWindow", file["size"]))

		#dwnloadBtn
        self.dwnloadBtn = QtWidgets.QPushButton(self.parent)
        self.dwnloadBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dwnloadBtn.setStyleSheet(
            "QPushButton {\n"
            "margin: 5px 10px;\n"
            "font-size: 15px;\n"
            "border-radius: 20px;\n"
            "padding: 4;\n"
            "background-color: rgb(237, 237, 237);"
            "}\n"
            "QPushButton::hover {\n"
            "    border: 2px solid #ffffff;\n"
            "    background-color: #ffffff;\n"
            "}\n"
        )
        self.dwnloadBtn.setObjectName("dwnloadBtn_" + file["fileName"])
        self.dwnloadBtn.setIcon(QtGui.QIcon('images/download.png'))
        self.dwnloadBtn.setIconSize(QtCore.QSize(32, 32))

		#adding widgets
        self.addWidget(self.fileType)
        self.addWidget(self.fileName)
        self.addWidget(self.ownerName)
        self.addWidget(self.fileSize)
        self.addWidget(self.dwnloadBtn)

        self.setStretch(0, 1)
        self.setStretch(1, 4)
        self.setStretch(2, 4)
        self.setStretch(3, 4)
        self.setStretch(4, 1)