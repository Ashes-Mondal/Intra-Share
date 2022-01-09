import os,sys,socket,json
from queue import Queue
from threading import Thread,Lock,Event
from dotenv import load_dotenv
load_dotenv()
from database.methods import Database_Methods
from colors import bcolors

def encodeJSON(input: dict):
    return str(json.dumps(input)).encode()

class Functionalities(Database_Methods):
    def __init__(self):
        Database_Methods.__init__(self)
    
    __sendMessageRequestQueue = Queue()
    
    def __authenticateClient(self,client: tuple):
        conn,addr = client
        clientID = None
        username = None
        while True:
            request = json.loads(str(conn.recv(4096),'utf-8'))
            response = {"type":"client_request_response","data":"Success","error":None}
            if len(request) == 0:
                ##client has disconnected from server
                conn.close()
                sys.exit()##exists from the thread
            
            if request["type"] == 'client_login':
                try:
                    clientID,username = self._checkLoginCredentials(request["data"])
                except:
                    error_msg = f'Failed to login!'
                    response = {"type":"client_request_response","data":None,"error":error_msg}
            elif request["type"] == 'client_signup':
                clientID,username = self._createNewProfile(request["data"])
            else:
                error_msg = f'Unauthorised request!'
                response = {"type":"client_request_response","data":None,"error":error_msg}
            conn.sendall(encodeJSON(response))
            if clientID!= None and username!=None:
                return clientID,username
    
    def _listenClientForRequests(self,client: tuple,server_password: str = None):
        conn,addr = client
        clientID = None
        username = None
        ##Initial checks before allowing client to send requests 
        try:
            clientID,username = self.__authenticateClient(client)
            self._getMetadataFromClient(clientID,client)
        except:
            sys.exit()
        
        ##Welcome message send to client
        msg = {"type":"connection_established","data":"Welcome to the server."}
        conn.sendall(encodeJSON(msg))
        
        ##Listening to clients for requests
        while True:
            try:
                request = json.loads(str(conn.recv(4096),'utf-8'))
                
                if len(request) == 0:
                    ##client has disconnected from server
                    self._closeClientConnection(clientID,client)
                    sys.exit()##exists from the thread
                    
                ##Working according to request type
                response = {"type":"client_request_response","data":"Success","error":None}
                if request["type"] == 'send_message':
                    ##request["data"] = {sender:tuple(ip,port),receiver:tuple(ip,port),message:str}
                    self.__sendMessageRequestQueue.put(request["data"])
                elif request["type"] == "update_client_username":
                    ##request["data"] = username:str
                    newUsername = request["data"]
                    try:
                        self._updateClientUsername(clientID,newUsername)
                        username = newUsername
                    except:
                        error_msg = f'Failed to update username!'
                        response = {"type":"client_request_error","data":None,"error":error_msg}
                conn.sendall(encodeJSON(response))
            except socket.error as error:
                print(f'[Listening Error]=>{addr[0]}:{addr[1]}:= {error}')
                self._closeClientConnection(clientID,client)
                sys.exit()##exists from the thread
    
    def _getMetadataFromClient(self,clientID:int,client: tuple):
        conn,addr = client
        while True:
            try:
                request = json.loads(str(conn.recv(4096),'utf-8'))
                
                if len(request) == 0:
                    ##client has disconnected from server
                    self._closeClientConnection(clientID,client)
                    sys.exit()##exists from the thread
                
                response = {"type":"client_request_response","data":"Success","error":None}
                ##if request["type"] == 'client_metadata'
                if request["type"] == 'client_metadata':
                    metadata = request["data"]
                    self._updateClientMetadata(clientID,metadata)
                else:
                    error_msg = f'Unauthorised request!'
                    response = {"type":"client_request_response","data":None,"error":error_msg}
                conn.sendall(encodeJSON(response))
                    
            except Exception as error:
                print(f'{bcolors["FAILED"]}[SERVER]Failed to get metadata from {bcolors["UNDERLINE"]}{addr[0]}:{addr[1]}{bcolors["ENDC"]}')
                raise error
    
    def _closeClientConnection(self,clientID: int,client: tuple):
        conn,addr = client
        conn.close()
    
    def _sendMessage(self):
        while True:
            data = self.__sendMessageRequestQueue.get()
            sender_addr = data['sender'] = tuple(data['sender'])
            receiver_addr = data['receiver'] = tuple(data['receiver'])
            
            try:
                receiver = self._getClientDetails(receiver_addr)
                response = {"type":"got_message","data":data}
                receiver.conn.sendall(encodeJSON(response))
            except socket.error as error:
                sender = self._getClientDetails(sender_addr)
                error_msg = f'Failed to send message,receiver went offline!'
                response = {"type":"send_message_error","error":error_msg}
                sender.conn.sendall(encodeJSON(response))
            self.__sendMessageRequestQueue.task_done()

class Server(Functionalities):
    sendMessageThreadCount = 10
    def __init__(self,host: str = '',port: int = 0,max_listen_limit: int = 10,password: str = None):
        Functionalities.__init__(self)
        try:
            self.host = host
            self.port = port
            self.password = password
            self.max_listen_limit = max_listen_limit
            self.__acceptedConnections = []
            self.__createSocket()
            while self.__bindSocket():continue
            t1 = Thread(target=self.__acceptConnections,daemon=True,name=f'__acceptConnections_{self.port}')
            for i in range(self.sendMessageThreadCount):
                worker_thread = Thread(target=self._sendMessage,daemon=True,name=f'worker_thread{i}')
                worker_thread.start()
            t1.start()        
        except Exception as error:
            raise error
    
    def __createSocket(self):
        try:
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print(f'{bcolors["OKGREEN"]}[SERVER]{bcolors["ENDC"]}TCP socket created successfully.')
        except socket.error as error:
            print(f'{bcolors["FAILED"]}[SERVER]Failed to create TCP socket!{bcolors["ENDC"]}')
            print(f'{bcolors["HEADER"]}Reason:{bcolors["ENDC"]} {error}')
            raise error
    
    def __bindSocket(self):
        try:
            self.server.bind((self.host,self.port))
            self.host,self.port= self.server.getsockname()
            self.server.listen(self.max_listen_limit)
            print(f'{bcolors["OKGREEN"]}[SERVER]{bcolors["ENDC"]}Socket binding at:= {bcolors["UNDERLINE"]}{self.host}:{self.port}{bcolors["ENDC"]}')
        except socket.error as error:
            print(f'{bcolors["FAILED"]}[SERVER] Failed to bind TCP socket to {bcolors["ENDC"]}{bcolors["UNDERLINE"]}{self.host}:{self.port}{bcolors["ENDC"]}')
            print(f'{bcolors["HEADER"]}Reason:{bcolors["ENDC"]} {error}')

    def __acceptConnections(self):
        ## Caches all new established connections
        while True:
            try:
                client = self.server.accept()
                
                #listen to client for requests
                t = Thread(target=self._listenClientForRequests,args=(client,self.password),name=f'_listenClientForRequests_{client[0]}')
                t.start()
            except socket.error as error:
                print(f'{bcolors["FAILED"]}[SERVER]Accepting connection error{bcolors["ENDC"]}')
                print(f'{bcolors["HEADER"]}Reason:{bcolors["ENDC"]} {error}')
                self.closeServer()
    
    def closeServer(self):
        print(f'{bcolors["OKGREEN"]}[SERVER]{bcolors["ENDC"]}Closing server socket...')
        self.server.close()
        sys.exit()##exists from the thread


def main():
    server = Server(host='',port=9999)
    while True:
        k = input()
        if k == 'exit()':
            server.closeServer()

if __name__ == "__main__":
    main()
