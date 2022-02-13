from PyQt5 import QtCore, QtGui, QtWidgets

class MainHeading:
    def __init__(self, centralwidget) -> None:
        self.label_heading = QtWidgets.QLabel(centralwidget)
        self.label_heading.setGeometry(QtCore.QRect(260, 30, 641, 61))
        self.label_heading.setStyleSheet("border: 2px solid red;\n"
        "border-radius: 10px;\n"
        "padding-left: 10;\n"
        "padding-right: 10;\n"
        "color: rgb(85, 255, 255);\n"
        "background-color: rgb(85, 0, 127);")
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label_heading.setFont(font)
        self.label_heading.setObjectName("label_heading")

        _translate = QtCore.QCoreApplication.translate
        self.label_heading.setText(_translate("MainWindow", "WELCOME TO THE LOCAL DC++ PROJECT"))
