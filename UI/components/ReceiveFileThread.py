import sys
import tqdm
from PyQt5 import QtCore, QtGui, QtWidgets
from colors import bcolors
from .utils import recvall
import socket

class ReceiveFileThread(QtCore.QThread):
    progress = QtCore.pyqtSignal(int,int)
    finishedSig = QtCore.pyqtSignal(int,int)
    stopSig = QtCore.pyqtSignal()
    def __init__(self,parameters):
        super(ReceiveFileThread, self).__init__()
        clientObj, conn, pause1, file,filelock = parameters
        self.conn = conn
        self.file = file
        self.filelock = filelock
        self.pauseEvent = pause1
        self.clientObj = clientObj

    def run(self):
        try:
            fileID, start, end, filesize, filepath,completed_bytes = self.file
            print(f'{bcolors["WARNING"]}[CLIENT]{bcolors["ENDC"]}Downloading path:= {bcolors["UNDERLINE"]}{filepath}{bcolors["ENDC"]}')
            if fileID in self.clientObj.fileTaking.keys():
                self.clientObj.fileTaking[fileID][3] = self.pauseEvent
            else:
                self.clientObj.fileTaking[fileID] = [start,0,False,self.pauseEvent,filepath]
            tqdmBar = tqdm.tqdm(range(int(filesize)), f'{bcolors["OKGREEN"]}Downloading{bcolors["ENDC"]}', unit="B", unit_scale=True, unit_divisor=1024,)
            with open(filepath, 'wb') as output:
                output.seek(4096 * start)
                tqdmBar.update(completed_bytes)
                self.progress.emit(fileID,round((completed_bytes/filesize)*100))
                print("STARTED...")
                self.pauseEvent.clear()
                while start < end:
                    try:
                        data = recvall(self.conn, min(4096, filesize - completed_bytes))
                        if not data:
                            print(f'{bcolors["FAIL"]}[CLIENT]_receiveFile error! {bcolors["ENDC"]}')
                            print(f'{bcolors["HEADER"]}Reason:{bcolors["ENDC"]} Client went offline!')
                            with self.filelock:
                                self.clientObj.fileTaking[fileID] = [start, completed_bytes, True, self.pauseEvent,filepath]
                            if completed_bytes == filesize:
                                self.finishedSig.emit(self.clientObj.clientID,self.file[0])
                            else:
                                print("Stopping the thread..!")
                                self.stopSig.emit()
                            break
                        output.write(data)
                        completed_bytes += len(data)
                        tqdmBar.update(len(data))
                        self.progress.emit(fileID,round((completed_bytes/filesize)*100))
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
                        with self.filelock:
                            self.clientObj.fileTaking[fileID] = [start, completed_bytes, True, self.pauseEvent,filepath]
                        self.stopSig.emit()
                        print("Stopping the thread..!")
                        break
                    
                if completed_bytes == filesize:
                    with self.filelock:
                        self.clientObj.fileTaking.pop(fileID)
                    print(f'{bcolors["WARNING"]}[CLIENT]{bcolors["ENDC"]}Download completed 😊\n>>', end='')
                    self.finishedSig.emit(self.clientObj.clientID,self.file[0])
                # closing the connection
                self.conn.close()
        except Exception as e:
            print(e)

    def PauseOrPlay(self):
        self.pauseEvent.set()

