import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QTextBrowser, QPushButton, QVBoxLayout


class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.le = QLineEdit()
        self.le.returnPressed.connect(self.append_text)

        self.sb = QPushButton('SEND')
        self.sb.clicked.connect(self.append_text)

        self.tb = QTextBrowser()
        self.tb.setAcceptRichText(True)
        self.tb.setOpenExternalLinks(True)

        self.clear_btn = QPushButton('Clear')
        self.clear_btn.pressed.connect(self.clear_text)

        vbox = QVBoxLayout()
        vbox.addWidget(self.le, 0)
        vbox.addWidget(self.sb, 1)
        vbox.addWidget(self.tb, 2)
        vbox.addWidget(self.clear_btn, 3)

        self.setLayout(vbox)

        self.setWindowTitle('QTextBrowser')
        # self.setGeometry(300, 300, 300, 300)
        self.setFixedHeight(800)
        self.setFixedWidth(800)
        self.show()

    def append_text(self):
        text = self.le.text()
        self.tb.append(text)
        self.le.clear()

    def clear_text(self):
        self.tb.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
