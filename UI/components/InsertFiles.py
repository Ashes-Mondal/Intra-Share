from PyQt5 import QtWidgets, QtGui, QtCore


class InsertFiles(QtWidgets.QHBoxLayout):
    def __init__(self, parent):
        super(InsertFiles, self).__init__()
        self.parent = parent
        self.setObjectName("Insert" + "_Hbox")
        _translate = QtCore.QCoreApplication.translate

        text = "Share files  "
        self.insertFilesBtn = QtWidgets.QPushButton(parent=self.parent)
        self.insertFilesBtn.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.insertFilesBtn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.insertFilesBtn.setText(text)
        self.insertFilesBtn.setIcon(QtGui.QIcon('images/plus.png'))
        self.insertFilesBtn.setIconSize(QtCore.QSize(25, 25))
        self.insertFilesBtn.setStyleSheet(
            "QPushButton {\n"
            "    font: 75 18pt \"Georgia\";\n"
            "    padding: 5px;\n"
            # "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
            "background-color:rgb(0, 0, 0);\n"
            "    color:rgba(255, 255, 255, 210);\n"
            "    border: 2px solid black;\n"
            "    border-radius:5px;\n"
            "font-weight: bold;\n"
            "}\n"
            "\n"
            "QPushButton::hover {\n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
            "}\n"
            "\n"
            "QPushButton::pressed {\n"
            "    padding-left:5px;\n"
            "    padding-top:5px;\n"
            "    background-color:rgba(105, 118, 132, 200);\n"
            "}")
        self.insertFilesBtn.setObjectName("insertFilesBtn")
        self.addWidget(self.insertFilesBtn)
