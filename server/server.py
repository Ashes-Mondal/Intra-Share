import os,sys,socket,json,time
from queue import Queue
from threading import Thread,Lock,current_thread
from dotenv import load_dotenv
load_dotenv()
from colors import bcolors
from functionalities import Functionalities,encodeJSON

class client_struct:
        def __init__(self,clientID:int,client:tuple,username:str,port2: int):
            self.client = client
            self.username = username
            self.clientID = clientID
            self.clientIP,self.port1 = client[1]
            self.port2 = port2
            self.sendQueue = Queue()

class Server(Functionalities):
    __sendMessageThreadCount = 10
    __maxListenLimit = 10
    def __init__(self,host: str = '',port: int = 0,limit: int = 10,password: str = None):
        Functionalities.__init__(self)
        self.__lock = Lock()
        try:
            self.host = host
            self.port = port
            self._server_password = password
            self.__maxListenLimit = limit
            self.__acceptedConnections = []
            
            ##creating and binding socket
            self.__createSocket()
            while self.__bindSocket():continue
            
            #Thread1:Accepts connections
            t1 = Thread(target=self.__acceptConnections,daemon=True,name=f'__acceptConnections{self.port}')
            t1.start()    
            
            #Thread2:Send updated self.allclient to all active clients
            t2 = Thread(target=self._sendUpdatedClientList,args=(5,),daemon=True,name='_sendUpdatedClientList')
            t2.start()    
        except Exception as error:
            sys.exit()
    
    def __createSocket(self):
        try:
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print(f'{bcolors["OKGREEN"]}[SERVER]{bcolors["ENDC"]}TCP socket created successfully.')
        except socket.error as error:
            print(f'{bcolors["FAIL"]}[SERVER]Failed to create TCP socket!{bcolors["ENDC"]}')
            print(f'{bcolors["HEADER"]}Reason:{bcolors["ENDC"]} {error}')
            sys.exit()
    
    def __bindSocket(self):
        try:
            self.server.bind((self.host,self.port))
            self.host,self.port= self.server.getsockname()
            self.server.listen(self.__maxListenLimit)
            print(f'{bcolors["OKGREEN"]}[SERVER]{bcolors["ENDC"]}Socket binding at:= {bcolors["UNDERLINE"]}{self.host}:{self.port}{bcolors["ENDC"]}')
        except socket.error as error:
            print(f'{bcolors["FAIL"]}[SERVER] Failed to bind TCP socket to {bcolors["ENDC"]}{bcolors["UNDERLINE"]}{self.host}:{self.port}{bcolors["ENDC"]}')
            print(f'{bcolors["HEADER"]}Reason:{bcolors["ENDC"]} {error}')
            sys.exit()

    def __acceptConnections(self):
        ## Caches all new established connections
        print(f'{bcolors["OKGREEN"]}[SERVER]{bcolors["ENDC"]}Caching all new established connections...')
        while True:
            try:
                client = self.server.accept()
                conn,addr = client
                
                ##Initial checks before allowing client to send requests 
                try:
                    if self._server_password != None:
                        ##Sending password request to the client
                        pwd_request = {"type":"password_verification"}
                        conn.sendall(encodeJSON(pwd_request))
                        self._checkForServerPassword(client)
                    else:
                        ##Sending client_authentication request to the client
                        auth_request = {"type":"client_authentication"}
                        conn.sendall(encodeJSON(auth_request))
                    clientID,username = self._authenticateClient(client)
                    ports = self._getPortsFromClient(clientID,client)
                except Exception as error:
                    response = {"type":"client_request_response","data":None,"error":str(error)}
                    conn.sendall(encodeJSON(response))
                    conn.close()##closing connection with the client
                    continue
                
                ##Client authenticated adding to allclients dictionary
                newClient = client_struct(clientID=clientID,client=client,username=username,port2=ports["port2"])
                with self.__lock:
                    self.allClients[clientID] = newClient
                
                ##Sending welcome message
                print(f'{bcolors["OKGREEN"]}[SERVER]{bcolors["ENDC"]}New connection "{username}":={bcolors["UNDERLINE"]}{addr[0]}:{addr[1]}{bcolors["ENDC"]}')
                server_response = {"type":"welcome_message","data":f'Hi {username},welcome to the server.'}
                conn.sendall(encodeJSON(server_response))
                
                #Start server-client interactions
                worker_thread1 = Thread(target=self._listenClientForRequests,args=(clientID,),name=f'_listenClientForRequests{clientID}')
                worker_thread1.start()
                
                worker_thread2 = Thread(target=self._sendResponseToClients,args=(clientID,),name=f'_sendResponseToClients{clientID}')
                worker_thread2.start()
                
            except socket.error as error:
                print(f'{bcolors["FAIL"]}[SERVER]Accepting connection error{bcolors["ENDC"]}')
                print(f'{bcolors["HEADER"]}Reason:{bcolors["ENDC"]} {error}')
                self.closeServer()
    
    ##public methods
    def closeServer(self):
        print(f'{bcolors["OKGREEN"]}[SERVER]{bcolors["ENDC"]}Closing server socket...')
        self.server.close()
        sys.exit()##exists from the thread
    
    def changeServerPassword(self,newPassword: str):
        self._server_password
        print(f'{bcolors["OKGREEN"]}[SERVER]{bcolors["ENDC"]}Server password has been changed.')

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def main():
    try:
        server = Server(host=get_ip(),port=9999,password=None)
        while True:
            k = input()
            if k == 'q':
                server.closeServer()
            elif 'change pwd to' in k:
                newPassword = (k.split(" "))[3]
                server.changeServerPassword(newPassword)
            else:
                print(f'{bcolors["WARNING"]}[SERVER]{bcolors["ENDC"]}Invalid command!')
    except Exception as e:
        sys.exit()
    

if __name__ == "__main__":
    main()
