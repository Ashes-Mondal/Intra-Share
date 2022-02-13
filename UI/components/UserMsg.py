import string
import random
from PyQt5 import QtWidgets, QtGui, QtCore


class UserMsg(QtWidgets.QHBoxLayout):
    def __init__(self, parent, message):
        super(UserMsg, self).__init__()
        self.parent = parent
        randomSTR = ''.join(random.choices(
            string.ascii_uppercase + string.digits, k=10))
        self.setObjectName(randomSTR + "_Hbox")

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(message, self.parent)
        self.label.setStyleSheet(
            "padding: 10px;\n"
            "background-color: rgb(255, 255, 255);\n"
            "color: rgb(0, 0, 0);\n"
            "border: 2px solid rgb(0,0,0);\n"
            "border-radius: 10px;\n"
            "font-size: 20px\n"
        )
        # self.label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label" + randomSTR)
        self.addWidget(self.label)
        if len(message) >= 25:
            self.setStretch(0, 1)
            self.setStretch(1, 1)
