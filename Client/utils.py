import json
import os
import pickle
import sys
import threading
from queue import Queue

import tkinter as tk
from tkinter import filedialog


def encodeJSON(input: dict):
    return str(json.dumps(input)).encode()

def getFiles():
    root = tk.Tk()
    root.withdraw()

    filepaths = filedialog.askopenfilenames()
    files = []
    for filepath in filepaths:
        filename = filepath.split("/")[-1]
        filesize = os.path.getsize(filepath)
        files.append((filename,filesize,filepath))
    return files

def getFile():
    root = tk.Tk()
    root.withdraw()

    filepath = filedialog.askopenfilename()
    filename = filepath.split("/")[-1]
    filesize = os.path.getsize(filepath)
    return (filename,filesize,filepath)

def getDownloadDiectory():
    root = tk.Tk()
    root.withdraw()

    dirpath = filedialog.askdirectory()
    return dirpath

class pickling_struct:
    def __init__(self,client):
        self.clientID = client.clientID
        self.username = client.username
        self.unread_messages = client.unread_messages
        self.filesTaking = client.filesTaking
        self.filesGiving = client.filesTaking
    
    def debug(self):
        print(f'clientID: {self.clientID}')
        print(f'username: {self.username}')
        print(f'unread_messages: {self.unread_messages}')
        print(f'filesTaking: {self.filesTaking}')
        print(f'filesGiving: {self.filesGiving}\n')

def saveAppLastState(username,server_addr,activeClients: dict):
    filename = os.path.join(f'bin/app_{username}.bin')
    if os.path.isdir('bin') == False:
        os.mkdir("bin")
    with open(filename,mode='wb') as f:
        pickle.dump(server_addr,f)
        for k,client in activeClients.items():
            # client.debug()
            if len(client.unread_messages) == 0 and len(client.filesGiving) == 0 and len(client.filesTaking) == 0:
                continue
            obj = pickling_struct(client)
            pickle.dump(obj,f)

def getAppLastState(username,server_addr):
    filename = os.path.join(f'bin/app_{username}.bin')
    if os.path.isdir('bin') == False:
        os.mkdir("bin")
        return {}
    if os.path.isfile(filename) == False:
        return {}
    with open(filename,mode='rb') as f:
        nList = []
        addr = pickle.load(f)
        if server_addr==addr:
            while True:
                try:
                    obj = pickle.load(f)
                    # obj.debug()
                    nList.append(obj)
                except Exception as e:
                    break
    return nList
