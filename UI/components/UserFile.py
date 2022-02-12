from PyQt5 import QtWidgets, QtGui, QtCore
from  .utils import ext_ico_path,getSizeStr


class UserFile(QtWidgets.QHBoxLayout):
    def __init__(self, file:tuple,fileID:int, parent,removeUserFile):
        super(UserFile, self).__init__()
        self.fileID = fileID
        self.file = file
        self.removeUserFile = removeUserFile
        filename, filePath, fileSize = file
        self.filetype = filename.split('.')[-1].upper()
        self.parent = parent
        self.setObjectName("UserFile" + str(self.fileID))

		#fileTypeBtn
        path = ext_ico_path[self.filetype] if self.filetype in ext_ico_path.keys(
        ) else ext_ico_path["file"]
        self.fileTypeBtn = QtWidgets.QPushButton(self.parent)
        self.fileTypeBtn.setStyleSheet(
            "margin: 5px 10px;\n"
            "font-size: 15px;\n"
            "border-radius: 20px;\n"
            "padding: 4;\n"
            "background-color: rgb(237, 237, 237);"
        )
        self.fileTypeBtn.setObjectName("fileTypeBtn" + str(self.fileID))
        self.fileTypeBtn.setIcon(QtGui.QIcon(path))
        self.fileTypeBtn.setIconSize(QtCore.QSize(35, 35))

		#fileName
        self.fileName = QtWidgets.QLabel(filename[:20], self.parent)
        self.fileName.setStyleSheet(
            "text-align: left;\n"
            "padding-right: 10px;\n"
            "color: rgb(85, 0, 127);\n"
            "font: 75 11pt \"Verdana\";"
        )
        self.fileName.setObjectName("fileName" + str(self.fileID))
        self.fileName.setToolTip(filename)

        # fileSize
        self.fileSize = QtWidgets.QLabel(getSizeStr(fileSize), self.parent)
        self.fileSize.setStyleSheet(
            "text-align: left;\n"
            "padding-right: 10px;\n"
            "color: rgb(85, 0, 127);\n"
            "font: 75 11pt \"Verdana\";"
        )
        self.fileSize.setObjectName("fileSize" + str(self.fileID))

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
        self.deleteBtn.setObjectName("deleteBtn" + str(self.fileID))
        self.deleteBtn.setIcon(QtGui.QIcon('images/delete.png'))
        self.deleteBtn.setIconSize(QtCore.QSize(32, 32))
        self.deleteBtn.clicked.connect(self.deleteUserFile)

        self.addWidget(self.fileTypeBtn)
        self.addWidget(self.fileName)
        self.addWidget(self.fileSize)
        self.addWidget(self.deleteBtn)

        self.setStretch(0, 1)
        self.setStretch(1, 4)
        self.setStretch(2, 2)
        self.setStretch(3, 1)

    def deleteUserFile(self):
        try:
            self.removeUserFile(self.fileID)
        except Exception as e:
            print(e)
