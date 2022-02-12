import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from colors import bcolors
from .utils import recvall

class ReceiveFileThread(QtCore.QThread):
    progress = QtCore.pyqtSignal(int)
    def __init__(self,parameters):
        super(ReceiveFileThread, self).__init__()
        clientObj, conn, pause1, file,filelock = parameters
        self.conn = conn
        self.file = file
        self.filelock = filelock
        self.pauseEvent = pause1
        self.clientObj = clientObj

    def run(self):
        fileID, start, end, filesize, filepath,completed_bytes = self.file
        print(f'{bcolors["WARNING"]}[CLIENT]{bcolors["ENDC"]}Downloading path:= {bcolors["UNDERLINE"]}{filepath}{bcolors["ENDC"]}')
        if fileID in self.clientObj.fileTaking.keys():
            self.clientObj.fileTaking[fileID][3] = self.pauseEvent
        else:
            self.clientObj.fileTaking[fileID] = [start,0,False,self.pauseEvent,filepath]
        with open(filepath, 'wb') as output:
            output.seek(4096 * start)
            self.progress.emit(round((completed_bytes/filesize)*100))
            while start < end:
                try:
                    data = recvall(self.conn, min(4096, filesize - completed_bytes))
                    if not data:
                        print(f'{bcolors["FAIL"]}[CLIENT]_receiveFile error! {bcolors["ENDC"]}')
                        print(f'{bcolors["HEADER"]}Reason:{bcolors["ENDC"]} Client went offline!')
                        break
                    output.write(data)
                    completed_bytes += len(data)
                    self.progress.emit(round((completed_bytes/filesize)*100))
                    start += 1
                    if(self.pauseEvent.is_set()):
                        self.pauseEvent.clear()
                        with self.filelock:
                            self.clientObj.fileTaking[fileID] = [start, completed_bytes, True, self.pauseEvent,filepath]
                        self.pauseEvent.wait()
                        self.pauseEvent.clear()
                        self.clientObj.fileTaking[fileID][2] = False
                except Exception as error:
                    print(f'{bcolors["FAIL"]}[CLIENT]Failed to listen to {bcolors["ENDC"]}')
                    print(f'{bcolors["HEADER"]}Reason:{bcolors["ENDC"]} {error}')
                    break
                
            if self.clientObj.fileTaking[fileID][1] == filesize:
                with self.filelock:
                    self.clientObj.fileTaking.pop(fileID)
                print(f'{bcolors["WARNING"]}[CLIENT]{bcolors["ENDC"]}Download completed 😊\n>>', end='')
            # closing the connection
            self.conn.close()
            sys.exit()

    def PauseOrPlay(self,state:bool):
        self.pauseEvent.set()

