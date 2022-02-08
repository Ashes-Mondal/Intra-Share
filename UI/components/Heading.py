from PyQt5 import QtWidgets

class Heading(QtWidgets.QLabel):
    def __init__(self,text: str,parent):
        super(Heading, self).__init__(text,parent)
        self.setEnabled(True)
        self.setStyleSheet(
            "text-align: left;\n"
            "padding-left: 10;\n"
            "padding-right: 10px;\n"
            "border: 2px solid black;\n"
            "color: rgb(85, 0, 127);\n"
            "background-color: rgb(255, 255, 127);\n"
            "font: 75 14pt \"MS Sans Serif\";"
        )
        self.setObjectName(text)