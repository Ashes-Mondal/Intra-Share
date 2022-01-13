import socket,sys,json
from threading import Thread,Lock,Event
from queue import Queue
from colors import bcolors

def encodeJSON(input: dict):
    return str(json.dumps(input)).encode()

class client_struct:
    def __init__(self,clientID: int,username: str):
        self.clientID = clientID
        self.username = username
        self.online = True
        self.unread_messages =[]

class ServerInteraction:
    def __init__(self):
        self.CRQ = Queue()## Client's Request Queue
        self.SRCRQ = Queue()## Server's Response To Client's Request Queue
        self.SFL = list()##Shared File list
            
        self.__lock = Lock()
        ##Server config
        self.server_addr = None
        self.server_password = None
        ##Client config
        self.client = None
        self.clientID = None
        self.clientIP = socket.gethostbyname(socket.gethostname())
        self.port1 = None##messaging port
        self.clientCredentials = {"username":None,"password":None}
        ##Public attributes
        self.activeMessagingClient = None
        self.activeClients = {}
    
    def _passwordVerification(self):
        response = {"type":"server_password","data":self.server_password}
        self.client.sendall(encodeJSON(response))
        
        ##waiting for server response
        server_response = str(self.client.recv(4096),'utf-8')
        if len(server_response) == 0:
            print(f'{bcolors["FAIL"]}[CLIENT]Server went offline!{bcolors["ENDC"]}')
            self.client.close()
            sys.exit()
        server_response = json.loads(server_response)
        ##Checking for errors
        if server_response["data"]==None:
            raise Exception(server_response["error"])
    
    def _login(self):
        response = {"type":"client_authentication","data":self.clientCredentials}
        self.client.sendall(encodeJSON(response))
        
        ##waiting for server response
        server_response = str(self.client.recv(4096),'utf-8')
        if len(server_response) == 0:
            print(f'{bcolors["FAIL"]}[CLIENT]Server went offline!{bcolors["ENDC"]}')
            self.client.close()
            sys.exit()
        server_response = json.loads(server_response)
        
        ##Checking for errors
        if server_response["data"]==None:
            raise Exception(server_response["error"])
        
        return server_response
        
    
    def _giveServerPorts(self,port1:int,port2:int):
        response = {"type":"client_ports","data":{"port1":port1,"port2":port2}}
        self.client.sendall(encodeJSON(response))
        
        ##waiting for server response
        server_response = str(self.client.recv(4096),'utf-8')
        if len(server_response) == 0:
            print(f'{bcolors["FAIL"]}[CLIENT]Server went offline!{bcolors["ENDC"]}')
            self.client.close()
            sys.exit()
        server_response = json.loads(server_response)
        
        ##Checking for errors
        if server_response["data"]==None:
            raise Exception(server_response["error"])
        return server_response["data"]
    
    def _updateActiveClientsList(self,allClients):
        ##O(n + m)
        with self.__lock:
            for clientID in self.activeClients.keys():
                self.activeClients[clientID].online = False
            
            for i,details in enumerate(allClients):
                username = details[0]
                clientID = details[1]
                if self.clientID == clientID:
                    continue
                
                if clientID in self.activeClients.keys():
                    self.activeClients[clientID].username = username
                    self.activeClients[clientID].online = True
                    continue
                self.activeClients[clientID] = client_struct(clientID, username)
            
            for clientID in list(self.activeClients.keys()):
                if self.activeClients[clientID].online == False and len(self.activeClients[clientID].unread_messages) == 0:
                    del self.activeClients[clientID]
    
    def _processReceivedMessage(self,data):
        senderID = data['sender']
        message = data['message']
        if self.activeMessagingClient!=None and self.activeMessagingClient.clientID == senderID:
            username = self.activeMessagingClient.username
            print(f'{bcolors["OKCYAN"]}<{username}>{bcolors["ENDC"]}{message}',end='\n')
        else:
            with self.__lock:
                print(len(self.activeClients))
                self.activeClients[senderID].unread_messages.append(message)