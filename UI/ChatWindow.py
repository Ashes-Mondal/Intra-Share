from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot
from .components.SenderMsg import SenderMsg
from .components.UserMsg import UserMsg
from .components.ChatInput import ChatInput
from threading import Thread, currentThread,Event


class receiveMessagesThread(QtCore.QThread):
    my_signal = QtCore.pyqtSignal(int, str)

    def __init__(self, senderID: int,clientIns):
        super(QThread, self).__init__()
        self.senderID = senderID
        self.clientIns = clientIns
        self._isRunning = True
        
    def run(self):
        try:
            print("Unread Messages count:",self.clientIns.activeClients[self.senderID].messages.qsize())
            while self._isRunning:
                try:
                    message = self.clientIns.activeClients[self.senderID].messages.get(timeout=2)
                    if self._isRunning == False:
                        lst = [message]
                        while self.clientIns.activeClients[self.senderID].messages.empty() == False:
                            msg = self.clientIns.activeClients[self.senderID].messages.get()
                            lst.append(msg)
                        for msgs in lst:
                            self.clientIns.activeClients[self.senderID].messages.put(msgs)
                        return
                except Exception as e:
                    continue

                self.my_signal.emit(self.senderID, message)
        except Exception as err:
            print("Closing Thread:",currentThread().getName())
    
    def stop(self):
        self._isRunning = False


class ChatWindow(QtWidgets.QMainWindow):
    def __init__(self, receiverClientObj, clientIns, parent):
        super(ChatWindow, self).__init__(parent)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.parent = parent
        self.receiverClientObj = receiverClientObj
        self.clientIns = clientIns
        self.setFixedSize(969, 840)
        self.setupUi()
        try:
            self.startChatting(clientID=self.receiverClientObj.clientID)
        except Exception as e:
            print(e)
            self.close()

    def closeEvent(self, event):
        self.clientIns.stopSendingMessages(self.receiverClientObj.clientID)
        self.receiveMessagesThread.stop()
        self.receiveMessagesThread.quit()
        self.receiveMessagesThread.wait()
        event.accept()

    def onClick_send(self, message):
        if(len(message) == 0):
            return
        # print(message)
        try:
            self.clientIns.sendMessage(
                receiverID=self.receiverClientObj.clientID, message=message)
            # add message and spacer
            hbox1 = UserMsg(parent=self.chatWidget, message=message)
            self.verticalLayout_2.insertLayout(
                len(self.verticalLayout_2)-1, hbox1)
        except Exception as error:
            print(error)
            ret = QtWidgets.QMessageBox.warning(self, 'Failed to send...',f"{error}", QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Cancel)
            self.close()

    def StartButtonEvent(self):
        self.receiveMessagesThread = receiveMessagesThread(self.receiverClientObj.clientID,self.clientIns)
        self.receiveMessagesThread.my_signal.connect(self.buildSenderMessages)
        self.receiveMessagesThread.start()

    @pyqtSlot(int, str)
    def buildSenderMessages(self, clientID: int, message: str):
        # add message
        hbox1 = SenderMsg(parent=self.chatWidget, message=message)
        self.verticalLayout_2.insertLayout(len(self.verticalLayout_2)-1, hbox1)

    def startChatting(self, clientID: int):
        self.clientIns.intiateMessaging(clientID)
        self.StartButtonEvent()

    def setupUi(self):
        self.setObjectName("ChatWindow")
        self.resize(969, 740)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.chatScroll = QtWidgets.QScrollArea()
        self.chatWidget = QtWidgets.QWidget()

        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        spacerItem2 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.chatWidget.setLayout(self.verticalLayout_2)
        # Scroll Area Properties
        self.chatScroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.chatScroll.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.chatScroll.setWidgetResizable(True)
        self.chatScroll.setWidget(self.chatWidget)
        self.verticalLayout.addWidget(self.chatScroll)

        # component to send message
        self.chatHbox = ChatInput(self.centralwidget, self.onClick_send)
        self.verticalLayout.addLayout(self.chatHbox)
        self.verticalLayout.setStretch(0, 10)
        self.verticalLayout.setStretch(1, 1)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate(
            "ChatWindow", self.receiverClientObj.username))
        self.chatHbox.pushButton.setText(_translate("ChatWindow", "SEND"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = ChatWindow()
    sys.exit(app.exec_())
