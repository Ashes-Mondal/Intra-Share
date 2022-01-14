import socket,sys,json
from threading import Thread,Lock
from queue import Queue
from colors import bcolors
from utils import encodeJSON
class client_struct:
    def __init__(self,clientID: int,username: str,online: bool = True):
        self.clientID = clientID
        self.username = username
        self.online = online
        self.unread_messages =[]
        self.clientIP = None
        
        ##File sharing attributes
        self.port2 = None
        self.filesTaking = []
        self.filesGiving = []
        ##Channel
        self.client = None
        self.sendFileReq = Queue()
        self.getFileRes = Queue()
    
    def __lt__(self, obj):
        ##is self less than obj?
        if (self.online == True and obj.online == True) or (self.online == False and obj.online == False):
            return  self.username<obj.username
        else:
            return self.online
    
    def __gt__(self, obj):
        ##is self greater than obj?
        if (self.online == True and obj.online == True) or (self.online == False and obj.online == False):
            return  self.username>obj.username
        else:
            return self.online == False

class ServerInteraction:
    def __init__(self):
        #<-----------Different channels---------->
        ##request channel
        self.clientReq_Channel = Queue()
        
        ##response channel
        self.sendMessageRes_Channel = Queue()
        self.updateUsernameRes_Channel = Queue()
        self.getPortRes_Channel = Queue()
        #<-----------******************---------->
        
        self.hostedFiles = []
            
        self._lock = Lock()
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
        with self._lock:
            for clientID in self.activeClients.keys():
                self.activeClients[clientID].online = False
            
            for username,clientID in allClients:
                if clientID == self.clientID:
                    continue
                
                if clientID in self.activeClients.keys():
                    self.activeClients[clientID].username = username
                    self.activeClients[clientID].online = True
                    continue
                self.activeClients[clientID] = client_struct(clientID, username)
            
            ##sorting active Clients
            self.activeClients = dict(sorted(self.activeClients.items(), key=lambda x:x[1]))
    
    def _processReceivedMessage(self,data):
        senderID = data['sender']
        message = data['message']
        if self.activeMessagingClient!=None and self.activeMessagingClient.clientID == senderID:
            ##client is talking to that client
            username = self.activeMessagingClient.username
            print(f'{bcolors["OKCYAN"]}<{username}>{bcolors["ENDC"]}{message}',end='\n')
        else:
            with self._lock:
                self.activeClients[senderID].unread_messages.append(message)