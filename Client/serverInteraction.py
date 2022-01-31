import socket
import sys
import json
from threading import Thread, Lock
from queue import Queue

from colors import bcolors
from .utils import encodeJSON,decrypt_message


class client_struct:
    def __init__(self, clientID: int, username: str, online: bool = True):
        self.clientID = clientID
        self.username = username
        self.online = online
        # self.unread_messages =[]

        self.messages = Queue()
        self.pubkey = None

        # File sharing attributes
        self.filesTaking = {}

    def __lt__(self, obj):
        # is self less than obj?
        if (self.online == True and obj.online == True) or (self.online == False and obj.online == False):
            return self.username < obj.username
        else:
            return self.online

    def __gt__(self, obj):
        # is self greater than obj?
        if (self.online == True and obj.online == True) or (self.online == False and obj.online == False):
            return self.username > obj.username
        else:
            return self.online == False

    def debug(self):
        print(f'clientID: {self.clientID}')
        print(f'username: {self.username}')
        print(f'messages: {list(self.messages.queue)}')
        print(f'filesTaking: {self.filesTaking}')
        print(f'filesGiving: {self.filesGiving}\n')


class ServerInteraction:
    def __init__(self):
        # <-----------Different channels---------->
        # request channel
        self.clientReq_Channel = Queue()

        # response channel
        self.sendMessageRes_Channel = Queue()
        self.updateUsernameRes_Channel = Queue()
        self.getPortRes_Channel = Queue()
        self.getFileListRes_Channel = Queue()
        self.insertFilesRes_Channel = Queue()
        self.deleteFileRes_Channel = Queue()
        self.searchFileRes_Channel = Queue()
        self.getPublicKeyRes_Channel = Queue()
        # <-----------******************---------->

        self._lock = Lock()

        # Active Messaging clients
        self.activeMessagingClient = {}
        # Server config
        self.server_addr = None
        self.server_password = None
        # Client config
        self.client = None
        self.clientID = None
        self.clientIP = socket.gethostbyname(socket.gethostname())
        self.port1 = None  # messaging port
        self.clientCredentials = {"username": None, "password": None}
        # Public attributes
        self.activeClients = {}

    def _passwordVerification(self):
        response = {"type": "server_password", "data": self.server_password}
        self.client.sendall(encodeJSON(response))

        # waiting for server response
        server_response = str(self.client.recv(4096), 'utf-8')
        if len(server_response) == 0:
            print(
                f'{bcolors["FAIL"]}[CLIENT]Server went offline!{bcolors["ENDC"]}')
            self.client.close()
            sys.exit()
        server_response = json.loads(server_response)
        # Checking for errors
        if server_response["data"] == None:
            raise Exception(server_response["error"])

    def _login(self):
        response = {"type": "client_authentication",
                    "data": self.clientCredentials}
        self.client.sendall(encodeJSON(response))

        # waiting for server response
        server_response = str(self.client.recv(4096), 'utf-8')
        if len(server_response) == 0:
            print(
                f'{bcolors["FAIL"]}[CLIENT]Server went offline!{bcolors["ENDC"]}')
            self.client.close()
            sys.exit()
        server_response = json.loads(server_response)

        # Checking for errors
        if server_response["data"] == None:
            raise Exception(server_response["error"])

        return server_response

    def _giveServerMetadata(self, port1: int, port2: int,pubkey):
        response = {"type": "client_ports", "data": {
            "port1": port1, "port2": port2, "pubkey":pubkey}}
        self.client.sendall(encodeJSON(response))

        # waiting for server response
        server_response = str(self.client.recv(4096), 'utf-8')
        if len(server_response) == 0:
            print(
                f'{bcolors["FAIL"]}[CLIENT]Server went offline!{bcolors["ENDC"]}')
            self.client.close()
            sys.exit()
        server_response = json.loads(server_response)

        # Checking for errors
        if server_response["data"] == None:
            raise Exception(server_response["error"])
        return server_response["data"]

    def _updateActiveClientsList(self, allClients):
        with self._lock:
            for clientID in self.activeClients.keys():
                self.activeClients[clientID].online = False

            for username, clientID in allClients:
                if clientID == self.clientID:
                    continue

                if clientID in self.activeClients.keys():
                    self.activeClients[clientID].username = username
                    self.activeClients[clientID].online = True
                    continue
                self.activeClients[clientID] = client_struct(
                    clientID, username)

            # sorting active Clients
            self.activeClients = dict(
                sorted(self.activeClients.items(), key=lambda x: x[1]))

    def _processReceivedMessage(self, data):
        senderID = data['sender']
        bundle = data['bundle']
        message = decrypt_message(self.clientCredentials["username"], bundle=bundle)
        self.activeClients[senderID].messages.put(message)
    
    def _getClientPublicKey(self, clientID: int):
        request = {
            "type": "get_pubkey",
            "data":clientID
        }
        self.clientReq_Channel.put(request)
        # Waiting for response from server
        server_response = self.getPublicKeyRes_Channel.get(timeout=5)
        if server_response["data"] == None:
            print(f'{bcolors["OKGREEN"]}[SERVER]{bcolors["ENDC"]} {bcolors["FAIL"]}{server_response["error"]}{bcolors["ENDC"]}', end='\n')
            raise Exception(server_response["error"])
        self.getPublicKeyRes_Channel.task_done()
        return server_response["data"].encode()
