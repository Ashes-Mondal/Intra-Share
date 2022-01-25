import json
import os
import socket
import sys
from getpass import getpass
from threading import Event, Thread, current_thread 

from tabulate import tabulate

from Client.fileSharing import FileSharingFunctionalities
from Client.serverInteraction import ServerInteraction, client_struct
from Client.utils import (
    encodeJSON,
    getAppLastState,
    getDownloadDiectory,
    getFiles,
    saveAppLastState,
    encrypt_message,
    get_keys,
    generate_RSA_keys
)
from colors import bcolors

SERVER_IP = '192.168.0.174'
SERVER_PORT = 9999
SERVER_PASSWORD = ""
USER_CREDENTIALS = {
    "username": "",
    "password": ""
}


class Client(ServerInteraction, FileSharingFunctionalities):
    def __init__(self):
        self.closeEvent = Event()
        ServerInteraction.__init__(self)
        FileSharingFunctionalities.__init__(self)

    # Objective1:Open file sharing socket and accept incomming connection
    def _acceptConnections(self):
        # Caches all new established connections
        print(
            f'{bcolors["WARNING"]}[CLIENT]{bcolors["ENDC"]}Caching all new established connections...')
        while True:
            try:
                client = self.file_socket.accept()

                # listen to client for requests
                t = Thread(target=self._listenClientForRequests, args=(
                    client,), name=f'_listenClientForRequests_{client[0]}')
                t.start()
            except socket.error as error:
                print(
                    f'{bcolors["FAIL"]}[SERVER]Accepting connection error{bcolors["ENDC"]}')
                print(f'{bcolors["HEADER"]}Reason:{bcolors["ENDC"]} {error}')
                self.closeApplication()

    def __openFileSharingSocket(self):
        try:
            self.file_socket = socket.socket()
            self.file_socket.bind(('', 0))
            self.clientIP, self.port2 = self.file_socket.getsockname()
            self.file_socket.listen(10)
            print(
                f'{bcolors["WARNING"]}[CLIENT]{bcolors["ENDC"]}Opened file sharing socket')
            # Thread1:Accepts connections
            t1 = Thread(target=self._acceptConnections,
                        daemon=True, name=f'_acceptConnections')
            t1.start()
        except socket.error as error:
            print(
                f'{bcolors["FAIL"]}[SERVER] Failed to open file Sharing socket {bcolors["ENDC"]}')
            print(f'{bcolors["HEADER"]}Reason:{bcolors["ENDC"]} {error}')
            raise error

    # Objective2:Listen to the server
    def __listenToServer(self):
        print(
            f'{bcolors["WARNING"]}[CLIENT]{bcolors["ENDC"]}{current_thread().getName()} is online...')
        while True:
            try:
                server_response = str(self.client.recv(4096), 'utf-8')
                if len(server_response) == 0:
                    print(
                        f'{bcolors["FAIL"]}[CLIENT]Server went offline!{bcolors["ENDC"]}')
                    self.closeApplication()
                elif server_response == ' ':
                    continue
                server_response = json.loads(server_response)

                # debug server response
                # print(server_response) if server_response['type'] != 'server_update' else None

                if server_response['type'] == 'server_update':
                    self._updateActiveClientsList(server_response['data'])
                elif server_response['type'] == 'got_message':
                    self._processReceivedMessage(server_response['data'])
                elif server_response['type'] == 'client_request_response_SM':
                    self.sendMessageRes_Channel.put(server_response)
                elif server_response['type'] == 'client_request_response_UU':
                    self.updateUsernameRes_Channel.put(server_response)
                elif server_response['type'] == 'client_request_response_GP':
                    self.getPortRes_Channel.put(server_response)
                elif server_response['type'] == 'client_request_response_GF':
                    self.getFileListRes_Channel.put(server_response)
                elif server_response['type'] == 'client_request_response_INF':
                    self.insertFilesRes_Channel.put(server_response)
                elif server_response['type'] == 'client_request_response_DF':
                    self.deleteFileRes_Channel.put(server_response)
                elif server_response['type'] == 'client_request_response_SF':
                    self.searchFileRes_Channel.put(server_response)
                elif server_response['type'] == 'client_request_response_CPK':
                    self.getPublicKeyRes_Channel.put(server_response)
            except socket.error as error:
                print(
                    f'{bcolors["FAIL"]}[CLIENT]Failed to listen to server{bcolors["ENDC"]}')
                print(f'{bcolors["HEADER"]}Reason:{bcolors["ENDC"]} {error}')
                self.closeApplication()

    # Objective3:Send requests to server
    def __sendRequestToServer(self):
        print(
            f'{bcolors["WARNING"]}[CLIENT]{bcolors["ENDC"]}{current_thread().getName()} is online...')
        while True:
            try:
                request = self.clientReq_Channel.get()
                self.client.sendall(encodeJSON(request))
                self.clientReq_Channel.task_done()
            except Exception as error:
                print(
                    f'{bcolors["FAIL"]}[CLIENT]Failed to send request to server{bcolors["ENDC"]}')
                print(f'{bcolors["HEADER"]}Reason:{bcolors["ENDC"]} {error}')

    def __connectToServer(self):
        self.client = socket.socket()
        self.client.settimeout(5)
        self.client.connect(self.server_addr)
        self.client.settimeout(None)
        self.clientIP, self.port1 = self.client.getsockname()

        # Fullfill server's initial needs
        server_request = str(self.client.recv(4096), 'utf-8')
        if len(server_request) == 0:
            print(
                f'{bcolors["FAIL"]}[CLIENT]Server went offline!{bcolors["ENDC"]}')
            self.client.close()
            sys.exit()
        server_request = json.loads(server_request)
        if server_request['type'] == 'password_verification':
            self._passwordVerification()
        
        ##Successfully connected to server
        print(f'{bcolors["WARNING"]}[CLIENT]{bcolors["ENDC"]}Connected to the server.')
        print(f'{bcolors["WARNING"]}[CLIENT]{bcolors["ENDC"]}clientIP:{self.clientIP} port1:{self.port1} port2:{self.port2}')
    
    ## Public methods
    def downloadFile(self,clientID:int,fileID:int,filename: str,filesize:int):
        ##check if client is online
        if self.activeClients[clientID].online == False:
            raise Exception("Client Offline!")
        ##Select download directory
        download_directory = getDownloadDiectory()
        
        ##manipulate chunks
        start = 0
        end = (filesize//4096) + 1 if (filesize%4096) else 0
        
        ##get address from server ,create socket and then establish connection
        clientAddr = self.getAddrOfClient(clientID)
        conn = socket.socket()
        conn.settimeout(5)
        conn.connect(clientAddr)
        conn.settimeout(None)
        
        ##send download_request
        request = {"type":"download_request","data":{"fileID":fileID,"start":start,"end":end}}
        conn.sendall(encodeJSON(request))

        ##waiting for the response
        response = str(conn.recv(4096),'utf-8')
        if len(response) == 0:
            print(f'{bcolors["FAIL"]}[CLIENT]Failed to download file := "{filename}"{bcolors["ENDC"]}')
            print(f'{bcolors["HEADER"]}Reason:{bcolors["ENDC"]} Client went offline')
            conn.close()
            raise Exception(f'Failed to download file, client went offline')
        response = json.loads(response)
        if response["error"]!=None:
            raise Exception(response["error"])
        
        pause1 = Event()
        t1 = Thread(target=self._receiveFile,args=(conn,pause1,start,end,filename,filesize,download_directory ),daemon=True,name=f'_receiveFile_{filename}')
        t2 = Thread(target=self._clientInteraction,args=(conn, pause1),daemon=True,name=f'_clientInteraction_{filename}')
        t1.start()
        t2.start()
        
        t1.join()
        conn.close()
    
    def closeClient(self):
        print(
            f'{bcolors["WARNING"]}[CLIENT]{bcolors["ENDC"]}Closing connection with server...')
        self.client.close()
        print(
            f'{bcolors["WARNING"]}[CLIENT]{bcolors["ENDC"]}Closing file socket...')
        self.file_socket.close()

    def startClient(self, server_addr: tuple, clientCredentials: dict, server_password: str = None):
        # Setting all intial login variables
        self.server_addr = server_addr
        self.server_password = server_password
        self.clientCredentials = clientCredentials
        try:
            self.__openFileSharingSocket()
            self.__connectToServer()
            self._login()
            pubkey, privkey = get_keys(self.clientCredentials['username'])
            if privkey == None:
                pubkey, privkey = generate_RSA_keys(
                    self.clientCredentials['username'])
            server_response = self._giveServerMetadata(
                self.port1, self.port2, pubkey.decode('utf-8'))
            # set filelist in a dictionary
            for file in server_response["fileList"]:
                fileID, filename, filePath, fileSize, ID, username, status = file
                self.hostedFiles[fileID] = (filename, filePath, fileSize)

            self.clientID = server_response["clientID"]
            prevState = getAppLastState(
                username=self.clientCredentials['username'], server_addr=self.server_addr)
            for client in prevState:
                with self._lock:
                    obj = client_struct(
                        client.clientID, client.username, online=False)
                    obj.messages = client.messages or []
                    obj.filesTaking = client.filesTaking or []
                    self.activeClients[client.clientID] = obj

            # Successfully authenticated
            welcome_response = str(self.client.recv(4096), 'utf-8')
            if len(welcome_response) == 0:
                print(
                    f'{bcolors["FAIL"]}[CLIENT]Server went offline!{bcolors["ENDC"]}')
                self.client.close()
                sys.exit()
            welcome_response = json.loads(welcome_response)
            print(f'{bcolors["OKGREEN"]}[SERVER]{bcolors["ENDC"]}{bcolors["OKCYAN"]}{welcome_response["data"]}{bcolors["ENDC"]} {bcolors["UNDERLINE"]}{self.server_addr}{bcolors["ENDC"]}')

            # GET all members of the server
            with self._lock:
                for clientID, username in server_response["members"]:
                    if clientID == self.clientID:
                        continue
                    if clientID in self.activeClients.keys():
                        self.activeClients[clientID].username = username
                        continue
                    self.activeClients[clientID] = client_struct(
                        clientID, username, online=False)

            # Thread2:Listen to server
            t2 = Thread(target=self.__listenToServer,
                        daemon=True, name=f'_listenToServer')
            t2.start()

            # Thread3:Send requests to server
            t3 = Thread(target=self.__sendRequestToServer,
                        daemon=True, name=f'__sendRequestToServer')
            t3.start()
        except Exception as error:
            print(
                f'{bcolors["FAIL"]}[CLIENT]Failed to connect to server {self.server_addr}{bcolors["ENDC"]}')
            print(f'{bcolors["HEADER"]}Reason:{bcolors["ENDC"]} {error}')
            self.closeClient()
            raise error

    def closeApplication(self):
        saveAppLastState(
            self.clientCredentials['username'], self.server_addr, self.activeClients)
        self.closeClient()
        self.closeEvent.set()
    ##!---------- > xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx < ------------!##

    ##!---------- > Messaging methods < ------------!##

    def intiateMessaging(self, clientID: int):
        if clientID not in self.activeClients.keys():
            raise Exception("clientID not found in the list!")
        receiver = self.activeClients[clientID]
        if receiver.online == False:
            raise Exception(
                f'{self.activeClients[clientID].username} not online!')

        if clientID in self.activeMessagingClient.keys():
            raise Exception("Already talking to the client!")
        print(f'{bcolors["WARNING"]}[CLIENT]{bcolors["ENDC"]} {bcolors["UNDERLINE"]}{self.clientCredentials["username"]}{bcolors["ENDC"]} can now send messages to {bcolors["UNDERLINE"]}{receiver.username}{bcolors["ENDC"]}')

    def sendMessage(self, receiverID, message):
        receiver = self.activeClients[receiverID]
        if receiver.online == False:
            raise Exception("Client not online!")
        if receiver.pubkey == None:
            pubkey = self._getClientPublicKey(clientID=receiverID)
        bundle = encrypt_message(pubkey=pubkey, message=message)
        request = {
            "type": "send_message",
            "data": {
                "sender": self.clientID,
                "receiver": receiverID,
                "bundle": bundle
            }
        }
        try:
            self.clientReq_Channel.put(request)
            # Waiting for response from server
            server_response = self.sendMessageRes_Channel.get(timeout=5)
            if server_response["data"] == None:
                print(f'{bcolors["OKGREEN"]}[SERVER]{bcolors["ENDC"]} {bcolors["FAIL"]}{server_response["error"]}{bcolors["ENDC"]}', end='\n')
                raise Exception(server_response["error"])
            print(f'<{bcolors["HEADER"]}{self.clientCredentials["username"]}>{bcolors["ENDC"]} {message}', end='\n')
            self.sendMessageRes_Channel.task_done()
        except Exception as error:
            print(f'{bcolors["FAIL"]}[CLIENT]{bcolors["ENDC"]}Error sending message!')
            print(f'{bcolors["HEADER"]}Reason:{bcolors["ENDC"]} {error}')
            raise error
    ##!---------- > xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx < ------------!##

    ##!--------------- > Search methods < ---------------!##

    def searchFiles(self, filename: str):
        request = {"type": "search_file", "data": filename}
        self.clientReq_Channel.put(request)
        # Waiting for response from server
        server_response = self.searchFileRes_Channel.get(timeout=5)
        self.searchFileRes_Channel.task_done()
        if server_response["data"] == None:
            print(
                f'{bcolors["FAIL"]}[CLIENT]{bcolors["ENDC"]}Error deleting the file')
            print(
                f'{bcolors["HEADER"]}Reason:{bcolors["ENDC"]} {server_response["error"]}')
            raise Exception(f'{server_response["error"]}')
        with self._lock:
            self.displayFiles.clear()
            if len(server_response["data"]):
                for file in server_response["data"]:
                    fileID, filename, filesize, ID, username, status = file
                    self.displayFiles[fileID] = (
                        filename, filesize, ID, username, status)
        return self.displayFiles

    def searchUsers(self, search: str):
        lst = []
        for ClientID, clientOBJ in self.activeClients.items():
            if clientOBJ.username == self.clientCredentials["username"]:
                continue
            username = str.lower(clientOBJ.username)
            if str.lower(search) in username:
                lst.append(
                    (clientOBJ.clientID, clientOBJ.username, clientOBJ.online))
        return lst
    ##!---------- > xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx < ------------!##

    ##!---------- > Download methods < ------------!##

    def getAddrOfClient(self, clientID: int):
        request = {"type": "get_addr", "data": clientID}
        self.clientReq_Channel.put(request)
        # Waiting for response from server
        server_response = self.getPortRes_Channel.get(timeout=5)
        self.getPortRes_Channel.task_done()
        if server_response["data"] == None:
            raise Exception(f'{clientID} not online!')
        else:
            return tuple(server_response["data"])

    def downloadFile(self, clientID: int, fileID: int, filename: str, filesize: int, download_directory):
        # manipulate chunks
        start = 0
        end = (filesize//4096) + 1 if (filesize % 4096) else 0

        # get address from server ,create socket and then establish connection
        clientAddr = self.getAddrOfClient(clientID)
        conn = socket.socket()
        conn.settimeout(5)
        conn.connect(clientAddr)
        conn.settimeout(None)

        # send download_request
        request = {"type": "download_request", "data": {
            "fileID": fileID, "start": start, "end": end}}
        conn.sendall(encodeJSON(request))

        # waiting for the response
        response = str(conn.recv(4096), 'utf-8')
        if len(response) == 0:
            print(
                f'{bcolors["FAIL"]}[CLIENT]Failed to download file := "{filename}"{bcolors["ENDC"]}')
            print(
                f'{bcolors["HEADER"]}Reason:{bcolors["ENDC"]} Client went offline')
            conn.close()
            raise Exception(f'Failed to download file, client went offline')
        response = json.loads(response)
        if response["error"] != None:
            raise Exception(response["error"])

        t1 = Thread(target=self._receiveFile, args=(conn, start, end, filename,
                    filesize, download_directory), daemon=True, name=f'_receiveFile_{filename}')
        t2 = Thread(target=self._clientInteraction, args=(conn,),
                    daemon=True, name=f'_clientInteraction_{filename}')
        t1.start()
        t2.start()

        t1.join()
        conn.close()
        print(
            f'{bcolors["WARNING"]}[CLIENT]{bcolors["ENDC"]}Download completed 😊\n>>', end='')
    ##!---------- > xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx < ------------!##

    ##!---------- > Shared files methods < ------------!##

    def insertFiles(self):
        files = getFiles()
        request = {"type": "insert_new_files", "data": files}
        self.clientReq_Channel.put(request)
        # Waiting for response from server
        server_response = self.insertFilesRes_Channel.get(timeout=5)
        self.insertFilesRes_Channel.task_done()
        if server_response["data"] == None:
            print(
                f'{bcolors["FAIL"]}[CLIENT]{bcolors["ENDC"]}Error inserting files')
            print(
                f'{bcolors["HEADER"]}Reason:{bcolors["ENDC"]} {server_response["error"]}')
            raise Exception(f'{server_response["error"]}')
        failed = []
        with self._lock:
            for i, fileID in enumerate(server_response["data"]):
                if fileID == None:
                    failed.append(files[i])
                    continue
                self.hostedFiles[fileID] = files[i]
        if len(failed):
            print(
                f'{bcolors["FAIL"]}[CLIENT]{bcolors["ENDC"]}Failed to insert {len(failed)} files.')
            raise Exception(failed)

    def deleteFile(self, fileID: int):
        if fileID not in self.hostedFiles.keys():
            raise Exception("No such fileID found!")
        request = {"type": "delete_file", "data": fileID}
        self.clientReq_Channel.put(request)
        # Waiting for response from server
        server_response = self.deleteFileRes_Channel.get(timeout=5)
        self.deleteFileRes_Channel.task_done()
        if server_response["data"] == None:
            print(
                f'{bcolors["FAIL"]}[CLIENT]{bcolors["ENDC"]}Error deleting the file')
            print(
                f'{bcolors["HEADER"]}Reason:{bcolors["ENDC"]} {server_response["error"]}')
            raise Exception(f'{server_response["error"]}')
        with self._lock:
            del self.hostedFiles[fileID]

    def getFileListOfClient(self, clientID: int):
        if clientID not in self.activeClients.keys():
            raise Exception("No such client exists!")
        request = {"type": "get_file_list", "data": clientID}
        self.clientReq_Channel.put(request)
        # Waiting for response from server
        server_response = self.getFileListRes_Channel.get(timeout=5)
        self.getFileListRes_Channel.task_done()
        if server_response["data"] == None:
            print(
                f'{bcolors["FAIL"]}[CLIENT]{bcolors["ENDC"]}Error getting file list!')
            print(
                f'{bcolors["HEADER"]}Reason:{bcolors["ENDC"]} {server_response["error"]}')
            raise Exception(f'{server_response["error"]}')
        with self._lock:
            self.displayFiles.clear()
            if len(server_response["data"]):
                for file in server_response["data"]:
                    fileID, filename, filesize, filepath, ID, username, status = file
                    self.displayFiles[fileID] = (
                        filename, filesize, ID, username, status)
        return self.displayFiles
    ##!---------- > xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx < ------------!##

    ##!---------- > updateUsername method < ------------!##

    def updateUsername(self, username):
        request = {"type": "update_client_username", "data": username}
        try:
            self.clientReq_Channel.put(request)

            # Waiting for response from server
            server_response = self.updateUsernameRes_Channel.get(timeout=5)

            if server_response["data"] != None:
                self.clientCredentials["username"] = username
                print(
                    f'{bcolors["OKGREEN"]}[SERVER]{bcolors["ENDC"]} {bcolors["OKCYAN"]}{server_response["data"]}{bcolors["ENDC"]}', end='\n')
            else:
                print(
                    f'{bcolors["OKGREEN"]}[SERVER]{bcolors["ENDC"]} {bcolors["FAIL"]}{server_response["error"]}{bcolors["ENDC"]}', end='\n')
            self.updateUsernameRes_Channel.task_done()
        except Exception as error:
            print(f'[Username update error]:= {error}')
    ##!---------- > xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx < ------------!##


class InteractiveShell(Client):
    def __init__(self):
        Client.__init__(self)
        try:
            USER_CREDENTIALS["username"] = input("USERNAME:")
            USER_CREDENTIALS["password"] = getpass(prompt="PASSWORD:")
            self.startClient(server_addr=(SERVER_IP, SERVER_PORT),
                             server_password=SERVER_PASSWORD, clientCredentials=USER_CREDENTIALS)
        except Exception as e:
            sys.exit()

        # Thread4:Start interacting with the application
        t4 = Thread(target=self.__startShell,
                    daemon=True, name=f'__startShell')
        t4.start()

        # Close event
        self.closeEvent.wait()
        sys.exit()

    def __displayClients(self):
        if len(self.activeClients) == 0:
            print(
                f'{bcolors["OKBLUE"]}No other active clients found!{bcolors["ENDC"]}')
        else:
            table = []
            headers = [
                f'{bcolors["OKGREEN"]}ID{bcolors["ENDC"]}',
                f'{bcolors["OKGREEN"]}Username{bcolors["ENDC"]}',
                f'{bcolors["OKGREEN"]}Status{bcolors["ENDC"]}'
            ]
            for clientID, clientOBJ in self.activeClients.items():
                if clientOBJ.online:
                    status = f'{bcolors["OKGREEN"]}Online{bcolors["ENDC"]}'
                else:
                    status = f'{bcolors["FAIL"]}Offline{bcolors["ENDC"]}'
                table.append([clientID, clientOBJ.username, status])
            print(tabulate(table, headers, tablefmt="presto"))

    def __displaySharedFileList(self):
        if len(self.hostedFiles) == 0:
            print(f'{bcolors["OKBLUE"]}No files found!{bcolors["ENDC"]}')
        else:
            table = []
            headers = [
                f'{bcolors["OKGREEN"]}fileID{bcolors["ENDC"]}',
                f'{bcolors["OKGREEN"]}filename{bcolors["ENDC"]}',
                f'{bcolors["OKGREEN"]}size(bytes){bcolors["ENDC"]}',
                # f'{bcolors["OKGREEN"]}location{bcolors["ENDC"]}'
            ]

            for fileID, fileDetails in self.hostedFiles.items():
                filename, filesize, path = fileDetails
                table.append([fileID, filename, filesize])
            print(tabulate(table, headers, tablefmt="presto"))

    def __showFoundFiles(self):
        if len(self.displayFiles) == 0:
            print(f'{bcolors["OKBLUE"]}No files found!{bcolors["ENDC"]}')
        else:
            table = []
            headers = [
                f'{bcolors["OKGREEN"]}fileID{bcolors["ENDC"]}',
                f'{bcolors["OKGREEN"]}filename{bcolors["ENDC"]}',
                f'{bcolors["OKGREEN"]}size(bytes){bcolors["ENDC"]}',
                f'{bcolors["OKGREEN"]}ID{bcolors["ENDC"]}',
                f'{bcolors["OKGREEN"]}username{bcolors["ENDC"]}',
                f'{bcolors["OKGREEN"]}status{bcolors["ENDC"]}'
            ]

            for fileID, fileOBJ in self.displayFiles.items():
                filename, filesize, ID, username, status = fileOBJ
                if status:
                    status = f'{bcolors["OKGREEN"]}Online{bcolors["ENDC"]}'
                else:
                    status = f'{bcolors["FAIL"]}Offline{bcolors["ENDC"]}'
                table.append(
                    [fileID, filename, filesize, ID, username, status])
            print(tabulate(table, headers, tablefmt="presto"))

    def __showFoundUsers(self, users: list):
        if len(users) == 0:
            print(f'{bcolors["OKBLUE"]}No users found!{bcolors["ENDC"]}')
        else:
            table = []
            headers = [
                f'{bcolors["OKGREEN"]}ID{bcolors["ENDC"]}',
                f'{bcolors["OKGREEN"]}username{bcolors["ENDC"]}',
                f'{bcolors["OKGREEN"]}status{bcolors["ENDC"]}'
            ]
            for user in users:
                ID, username, status = user
                if status:
                    status = f'{bcolors["OKGREEN"]}Online{bcolors["ENDC"]}'
                else:
                    status = f'{bcolors["FAIL"]}Offline{bcolors["ENDC"]}'
                table.append((ID, username, status))
            print(tabulate(table, headers, tablefmt="presto"))

    def __receiveMessages(self, clientID: int):
        while True:
            message = self.activeClients[clientID].messages.get()
            username = self.activeClients[clientID].username
            print(
                f'{bcolors["OKCYAN"]}<{username}>{bcolors["ENDC"]}{message}', end='\n')

    def __startSendingMessages(self, clientID: int):
        receiveMessages_thread = Thread(target=self.__receiveMessages, args=(
            clientID,), daemon=True, name=f'receiveMessages_thread{clientID}')
        receiveMessages_thread.start()

        while True:
            message = input(f'')
            if message == 'q':
                print(f'{bcolors["WARNING"]}[CLIENT]{bcolors["ENDC"]} Closing messaging with {bcolors["UNDERLINE"]}{self.activeClients[clientID].username}{bcolors["ENDC"]}')
                break
            else:
                try:
                    self.sendMessage(clientID, message)
                except Exception as error:
                    print(f'{bcolors["FAIL"]}[SERVER]Failed to send message to {bcolors["ENDC"]}{bcolors["UNDERLINE"]}{self.activeClients[clientID].username}{bcolors["ENDC"]}')
                    print(f'{bcolors["HEADER"]}Reason:{bcolors["ENDC"]} {error}')

    def __startShell(self):
        print('Starting interactive shell...')
        while True:
            command = input('>>')
            if len(command) == 0:
                continue
            if command == "list":
                self.__displayClients()
            elif 'message' in command:
                clientID = command.split(" ")[1]
                if clientID.isdigit():
                    clientID = int(clientID)

                    # intiateMessaging
                    try:
                        self.intiateMessaging(clientID)
                        # send_msg_thread = Thread(target=self.__startSendingMessages, args=(
                        #     clientID,), daemon=True, name=f'__startSendingMessages{clientID}')
                        # send_msg_thread.start()
                        # send_msg_thread.join()
                        self.__startSendingMessages(clientID)
                    except Exception as error:
                        print(
                            f'{bcolors["WARNING"]}[CLIENT]{bcolors["ENDC"]}{error}')
                        continue
                else:
                    print(f'{bcolors["WARNING"]}[CLIENT]{bcolors["ENDC"]}{bcolors["FAIL"]}{clientID} not a digit!{bcolors["ENDC"]}')
            elif command == 'q':
                self.closeApplication()
            elif "update username to" in command:
                newUsername = command.split(" ")[3]
                self.updateUsername(newUsername)
            elif "get address" in command:
                try:
                    clientID = int(command.split(" ")[2])
                    res = self.getAddrOfClient(clientID)
                    print(
                        f'{bcolors["OKGREEN"]}[SERVER]{bcolors["ENDC"]} {res}')
                except Exception as error:
                    print(f'"{command}" is an invalid command.')
            elif "get files" in command:
                try:
                    clientID = int(command.split(" ")[2])
                    self.getFileListOfClient(clientID)
                    self.__showFoundFiles()
                except Exception as error:
                    print(f'"{command}" is an invalid command.')
            elif command == "show my files":
                try:
                    self.__displaySharedFileList()
                except Exception as error:
                    print(f'"{command}" is an invalid command.')
            elif "download file" in command:
                try:
                    fileID = int(command.split(" ")[2])

                    # Initial checks
                    if fileID not in self.displayFiles.keys():
                        raise Exception("No such file displaying!")
                    filename, filesize, ID, username, status = self.displayFiles[fileID]
                    # check if client is online
                    if self.activeClients[ID].online == False:
                        raise Exception("Client Offline!")

                    # Select download directory
                    download_directory = getDownloadDiectory()

                    # start download in  new thread
                    download_file_thread = Thread(target=self.downloadFile, args=(ID, fileID, filename, int(
                        filesize), download_directory), daemon=True, name=f'download_file_thread{ID}')
                    download_file_thread.start()
                    # self.downloadFile()
                except Exception as error:
                    print(f'"{command}" is an invalid command.', str(error))
            elif command == "insert files":
                try:
                    self.insertFiles()
                except Exception as error:
                    print(f'"{command}" is an invalid command.', str(error))
            elif "delete file" in command:
                try:
                    fileID = int(command.split(" ")[2])
                    self.deleteFile(fileID)
                except Exception as error:
                    print(f'"{command}" is an invalid command.', str(error))
            elif "search files" in command:
                try:
                    filename = command[13:]
                    self.searchFiles(filename)
                    self.__showFoundFiles()
                except Exception as error:
                    print(f'"{command}" is an invalid command.', str(error))
            elif "search users" in command:
                try:
                    search = command[13:]
                    res = self.searchUsers(search)
                    self.__showFoundUsers(res)
                except Exception as error:
                    print(f'"{command}" is an invalid command.', str(error))
            else:
                print(f'"{command}" is an invalid command.')


if __name__ == "__main__":
    InteractiveShell()
