import string
import random
from PyQt5 import QtWidgets, QtGui,QtCore


class SenderMsg(QtWidgets.QHBoxLayout):
    def __init__(self, parent,message):
        super(SenderMsg, self).__init__()
        self.parent = parent
        randomSTR = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        self.setObjectName(randomSTR + "_Hbox")

        self.label = QtWidgets.QLabel(message,self.parent)
        self.label.setStyleSheet(
            "padding: 10px;\n"
            "color: rgb(255, 255, 255);\n"
            "background-color: rgb(0, 0, 0);\n"
            "background-color: rgb(0, 85, 0);\n"
            "border: 2px solid rgb(255, 255, 255);\n"
            "border-radius: 10px"
        )
        self.label.setWordWrap(True)
        self.label.setObjectName("label"+randomSTR)
        self.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.addItem(spacerItem)
        if len(message) >= 25:
            self.setStretch(0, 1)
            self.setStretch(1, 1)