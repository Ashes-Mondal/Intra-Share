import socket,sys,json,time
from threading import Thread,Lock,Event
from getpass import getpass
from colors import bcolors
from serverInteraction import ServerInteraction
from fileSharing import FileSharingFunctionalities

SERVER_IP = '192.168.1.15'
SERVER_PORT = 9999
SERVER_PASSWORD = 'qwerty'
USER_CREDENTIALS = {
    "username":"",
    "password":"password"
}

def encodeJSON(input: dict):
    return str(json.dumps(input)).encode()

class Client(ServerInteraction,FileSharingFunctionalities):
    def __init__(self):
        self._lock = Lock()
        self._closeEvent = Event()
        ServerInteraction.__init__(self)
        FileSharingFunctionalities.__init__(self)
    
    ##Objective1:Open file sharing socket and accept incomming connection
    def _acceptConnections(self):
        ## Caches all new established connections
        print(f'{bcolors["WARNING"]}[CLIENT]{bcolors["ENDC"]}Caching all new established connections...')
        while True:
            try:
                client = self.file_socket.accept()
                
                #listen to client for requests
                t = Thread(target=self._listenClientForRequests,args=(client,),name=f'_listenClientForRequests_{client[0]}')
                t.start()
            except socket.error as error:
                print(f'{bcolors["FAIL"]}[SERVER]Accepting connection error{bcolors["ENDC"]}')
                print(f'{bcolors["HEADER"]}Reason:{bcolors["ENDC"]} {error}')
                self._close
                self.closeApplication()
    
    def __openFileSharingSocket(self):
        try:
            self.file_socket = socket.socket()
            self.file_socket.bind(('',0))
            self.clientIP,self.port2 = self.file_socket.getsockname()
            self.file_socket.listen(10)
            print(f'{bcolors["WARNING"]}[CLIENT]{bcolors["ENDC"]}Opened file sharing socket')
            #Thread1:Accepts connections
            t1 = Thread(target=self._acceptConnections,daemon=True,name=f'_acceptConnections')
            t1.start()
        except socket.error as error:
            print(f'{bcolors["FAIL"]}[SERVER] Failed to open file Sharing socket {bcolors["ENDC"]}')
            print(f'{bcolors["HEADER"]}Reason:{bcolors["ENDC"]} {error}')
            raise error
    
    ##Objective2:Connect to server and listen in background
    def __listenToServer(self):
        print(f'{bcolors["WARNING"]}[CLIENT]{bcolors["ENDC"]}Listening to server...')
        while True:
            try:
                server_response = str(self.client.recv(4096),'utf-8')
                if len(server_response) == 0:
                    print(f'{bcolors["FAIL"]}[CLIENT]Server went offline!{bcolors["ENDC"]}')
                    self.closeApplication()
                elif server_response == ' ':continue
                server_response = json.loads(server_response)
                
                if server_response['type'] == 'server_update':
                    self._updateActiveClientsList(server_response['data'])
                elif server_response['type'] == 'got_message':
                    self._processReceivedMessage(server_response['data'])
                elif server_response['type'] == 'client_request_response':
                    self.SRCRQ.put(server_response)
            except socket.error as error:
                print(f'{bcolors["FAIL"]}[CLIENT]Failed to listen to server{bcolors["ENDC"]}')
                print(f'{bcolors["HEADER"]}Reason:{bcolors["ENDC"]} {error}')
                self.closeApplication()
    
    def __connectToServer(self):
        self.client = socket.socket()
        self.client.connect(self.server_addr)
        self.clientIP,self.port1 = self.client.getsockname()
        
        ##Fullfill server's initial needs
        server_request = str(self.client.recv(4096),'utf-8')
        if len(server_request) == 0:
            print(f'{bcolors["FAIL"]}[CLIENT]Server went offline!{bcolors["ENDC"]}')
            self.client.close()
            sys.exit()
        server_request = json.loads(server_request)
        
        if server_request['type'] == 'password_verification':
            self._passwordVerification()
        
        ##Successfully connected to server
        print(f'{bcolors["WARNING"]}[CLIENT]{bcolors["ENDC"]}Connected to the server.')
        print(f'{bcolors["WARNING"]}[CLIENT]{bcolors["ENDC"]}clientIP:{self.clientIP} port1:{self.port1} port2:{self.port2}')
    
    ## Public methods
    def closeClient(self):
        print(f'{bcolors["WARNING"]}[CLIENT]{bcolors["ENDC"]}Closing connection with server...')
        self.client.close()
        print(f'{bcolors["WARNING"]}[CLIENT]{bcolors["ENDC"]}Closing file socket...')
        self.file_socket.close()
        
    def startClient(self,server_addr: tuple,clientCredentials: dict,server_password: str = None):
        ##Setting all intial login variables
        self.server_addr = server_addr
        self.server_password = server_password
        self.clientCredentials = clientCredentials
        try:
            self.__openFileSharingSocket()
            self.__connectToServer()
            self._login()
            server_response = self._giveServerPorts(self.port1,self.port2)
            self.SFL = server_response["fileList"]
            self.clientID = server_response["clientID"]
            
            ##Successfully authenticated
            welcome_response = str(self.client.recv(4096),'utf-8')
            if len(welcome_response) == 0:
                print(f'{bcolors["FAIL"]}[CLIENT]Server went offline!{bcolors["ENDC"]}')
                self.client.close()
                sys.exit()
            welcome_response = json.loads(welcome_response)
            print(f'{bcolors["OKGREEN"]}[SERVER]{bcolors["ENDC"]}{bcolors["OKCYAN"]}{welcome_response["data"]}{bcolors["ENDC"]} {bcolors["UNDERLINE"]}{self.server_addr}{bcolors["ENDC"]}')
            
            ##Thread2:Listen to server in background
            t2 = Thread(target=self.__listenToServer,daemon=True,name=f'_listenToServer')
            t2.start()
        except Exception as error:
            print(f'{bcolors["FAIL"]}[CLIENT]Failed to connect to server{bcolors["ENDC"]}')
            print(f'{bcolors["HEADER"]}Reason:{bcolors["ENDC"]} {error}')
            self.closeClient()
            raise error
    
    def closeApplication(self):
        self.closeClient()
        self._closeEvent.set()
        
    def updateUsername(self,username):
        self.clientCredentials["username"] = username
        try:
            self.client.sendall(encodeJSON({"type":"update_client_username","data":username}))
            ##Waiting for response from server
            server_response = self.SRCRQ.get()
            if server_response["data"]!=None:
                self.clientCredentials["username"] = username
                print(f'{bcolors["OKGREEN"]}[SERVER]{bcolors["ENDC"]} {bcolors["OKCYAN"]}{server_response["data"]}{bcolors["ENDC"]}',end='\n')
            else:
                print(f'{bcolors["OKGREEN"]}[SERVER]{bcolors["ENDC"]} {bcolors["FAIL"]}{server_response["error"]}{bcolors["ENDC"]}',end='\n')
        except socket.error as error:
            print(f'[Username update error]:= {error}')
    
    def sendMessage(self,receiverID,message):
        response = {"type":"send_message","data":{"sender":self.clientID,"receiver":receiverID,"message":message}}
        try:
            self.client.sendall(encodeJSON(response))
            ##Waiting for response from server
            server_response = self.SRCRQ.get()
            if server_response["data"]!=None:
                print(f'<{bcolors["HEADER"]}{self.clientCredentials["username"]}>{bcolors["ENDC"]} {message}',end='\n')
            else:
                print(f'{bcolors["OKGREEN"]}[SERVER]{bcolors["ENDC"]} {bcolors["FAIL"]}{server_response["error"]}{bcolors["ENDC"]}',end='\n')
        except socket.error as error:
            print(f'{bcolors["FAIL"]}[CLIENT]{bcolors["ENDC"]}Error sending message!')
            print(f'{bcolors["HEADER"]}Reason:{bcolors["ENDC"]} {error}')
            
    def getAddrOfClient(self,clientID:int):
        if clientID in self.activeClients.keys():
            if self.activeClients[clientID].clientIP is None:
                request = {"type":"get_addr","data":clientID}
                try:
                    self.client.sendall(encodeJSON(request))
                    
                    ##Waiting for response from server
                    server_response = self.SRCRQ.get()
                    return server_response["data"] if server_response["data"]==None else tuple(server_response["data"])
                except Exception as error:
                    print(f'{bcolors["FAIL"]}[CLIENT]{bcolors["ENDC"]}Error getting address of client!')
                    print(f'{bcolors["HEADER"]}Reason:{bcolors["ENDC"]} {error}')
            else:
                return (self.activeClients[clientID].clientIP,self.activeClients[clientID].port2)

class InteractiveShell(Client):
    def __init__(self):
            Client.__init__(self)
            try:
                USER_CREDENTIALS["username"] = input("USERNAME:")
                self.startClient(server_addr=(SERVER_IP,SERVER_PORT),server_password=SERVER_PASSWORD,clientCredentials=USER_CREDENTIALS)
            except Exception as e:
                sys.exit()
            
            ##Thread3:Start interacting with the application
            t3 = Thread(target=self.__startShell,daemon=True,name=f'__startShell')
            t3.start()
            
            ##Close event
            self._closeEvent.wait()
            sys.exit()
    
    def __displayActiveClients(self):
        if len(self.activeClients) == 0:
            print(f'{bcolors["OKBLUE"]}No other active clients found!{bcolors["ENDC"]}')
        else:
            print(f'{bcolors["OKCYAN"]}<------- Active Clients ------>{bcolors["ENDC"]}')
            print(f'{bcolors["OKGREEN"]}ClientID            username{bcolors["ENDC"]}')
            for clientID,clientOBJ in self.activeClients.items():
                print(f'    {clientID}                {clientOBJ.username}')
    
    def __startSendingMessages(self,clientID: int):
        receiver = self.activeClients[clientID]
        self.activeMessagingClient = receiver
        print(f'{self.clientCredentials["username"]} can now send messages to {receiver.username}')
        ##check for unread messages
        for message in self.activeMessagingClient.unread_messages:
            print(f'<{bcolors["OKCYAN"]}{receiver.username}>{bcolors["ENDC"]} {message}',end='\n')
        with self._lock:
            self.activeMessagingClient.unread_messages.clear()
        while True:
            message = input(f'')
            if message == 'q':
                self.activeMessagingClient = None
                break
            self.sendMessage(clientID, message)
    
    def __startShell(self):
        print('Starting interactive shell...')
        while True:
            command = input('>>')
            if len(command) == 0:
                continue
            if command == "list":
                self.__displayActiveClients()
            elif 'select' in command:
                clientID = command.split(" ")[1]
                if clientID.isdigit():
                    try:
                        self.__startSendingMessages(int(clientID))
                    except Exception as error:
                        print(f'{bcolors["WARNING"]}[CLIENT]{bcolors["ENDC"]}{error}')
                        continue
            elif command == 'q':
                self.closeApplication()
            elif "update username to" in command:
                newUsername = command.split(" ")[3]
                self.updateUsername(newUsername)
            elif "get address" in command:
                try:
                    paclientID = int(command.split(" ")[2])
                    res = self.getAddrOfClient(clientID)
                    print(f'{bcolors["OKGREEN"]}[SERVER]{bcolors["ENDC"]} {res}')
                except Exception as error:
                    print(f'"{command}" is an invalid command.')
                
            else:
                print(f'"{command}" is an invalid command.')


def main():
    InteractiveShell()

if __name__ == "__main__":
    main()