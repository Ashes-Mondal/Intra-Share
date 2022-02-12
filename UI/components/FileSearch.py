from PyQt5 import QtWidgets, QtGui,QtCore


class FileSearch(QtWidgets.QHBoxLayout):
    def __init__(self, parent,searchForFiles):
        super(FileSearch, self).__init__()
        self.parent = parent
        self.searchForFiles = searchForFiles
        self.setObjectName("file_search" + "_Hbox")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.parent)
        self.lineEdit_2.setStyleSheet(
            "text-align: left;\n"
            "padding: 3;\n"
            "padding-left: 10;\n"
            "padding-right: 10;\n"
            "border: 2px solid black;\n"
            "color: rgb(85, 0, 127);\n"
            "font: 75 11pt \"MS Sans Serif\";"
        )
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.parent)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(
            "padding: 4;\n"
            "padding-left: 10;\n"
            "padding-right: 10;\n"
            "color: rgb(85, 0, 127);\n"
            "background-color: rgb(255, 255, 127);\n"
            "text-align: left;\n"
            "border: 2px solid black;\n"
            "font: 75 11pt \"MS Sans Serif\";"
        )
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.searchFiles)
        self.addWidget(self.lineEdit_2)
        self.addWidget(self.pushButton_2)

    def searchFiles(self):
        self.searchForFiles(self.lineEdit_2.text())
