from PyQt5 import QtWidgets, QtGui, QtCore
from  .utils import ext_ico_path


class UserFile(QtWidgets.QHBoxLayout):
    def __init__(self, file: dict, parent):
        super(UserFile, self).__init__()
        self.file = file
        self.parent = parent
        self.setObjectName(file["fileName"] + "_Hbox")

		#fileTypeBtn
        path = ext_ico_path[file["type"]] if file["type"] in ext_ico_path.keys(
        ) else ext_ico_path["file"]
        self.fileTypeBtn = QtWidgets.QPushButton(self.parent)
        self.fileTypeBtn.setStyleSheet(
            "margin: 5px 10px;\n"
            "font-size: 15px;\n"
            "border-radius: 20px;\n"
            "padding: 4;\n"
            "background-color: rgb(237, 237, 237);"
        )
        self.fileTypeBtn.setObjectName(file["fileName"] + "fileTypeBtn")
        self.fileTypeBtn.setIcon(QtGui.QIcon(path))
        self.fileTypeBtn.setIconSize(QtCore.QSize(35, 35))

		#fileName
        self.fileName = QtWidgets.QLabel(file["fileName"], self.parent)
        self.fileName.setStyleSheet(
            "text-align: left;\n"
            "padding-right: 10px;\n"
            "color: rgb(85, 0, 127);\n"
            "font: 75 11pt \"Verdana\";"
        )
        self.fileName.setObjectName("fileName" + file["fileName"])
        self.fileName.setToolTip(file["fileName"])

        # fileSize
        self.fileSize = QtWidgets.QLabel(file["fileSize"], self.parent)
        self.fileSize.setStyleSheet(
            "text-align: left;\n"
            "padding-right: 10px;\n"
            "color: rgb(85, 0, 127);\n"
            "font: 75 11pt \"Verdana\";"
        )
        self.fileSize.setObjectName("fileSize" + file["fileName"])

        # deleteBtn
        self.deleteBtn = QtWidgets.QPushButton(self.parent)
        self.deleteBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.deleteBtn.setStyleSheet(
            "QPushButton {\n"
            "margin: 5px 10px;\n"
            "font-size: 15px;\n"
            "border-radius: 20px;\n"
            "padding: 4;\n"
            "background-color: rgb(237, 237, 237);"
            "}\n"
            "QPushButton::hover {\n"
            "    border: 2px solid red;\n"
            "    background-color: red;\n"
            "}\n"
        )
        self.deleteBtn.setObjectName("deleteBtn" + file["fileName"])
        self.deleteBtn.setIcon(QtGui.QIcon('images/delete.png'))
        self.deleteBtn.setIconSize(QtCore.QSize(32, 32))

        self.addWidget(self.fileTypeBtn)
        self.addWidget(self.fileName)
        self.addWidget(self.fileSize)
        self.addWidget(self.deleteBtn)

        self.setStretch(0, 1)
        self.setStretch(1, 4)
        self.setStretch(2, 2)
        self.setStretch(3, 1)
