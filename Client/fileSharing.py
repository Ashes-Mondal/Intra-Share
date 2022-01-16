import socket,sys,json
from colors import bcolors
from .utils import encodeJSON

class FileSharingFunctionalities:
    def __init__(self):
        self.port2 = None##File sharing port
        self.FileTakingclients = []
        
    def _connectToClient(self,clientID:int,addr: tuple):
        if addr == None:
            raise Exception("Client went offline,failed to connect")
        self.client = socket.socket()
        self.client.connect(self.server_addr)
        self.clientIP,self.port1 = self.client.getsockname()
    
    
    def _listenClientForRequests(self,client):
        conn,addr = client

    
    def _closeFileClient(self,client: tuple):
        conn,addr = client
        conn.close()
        sys.exit()
    
    def _closeFileSocket(self):
        print(f'{bcolors["WARNING"]}[CLIENT]{bcolors["ENDC"]}Closing file socket...')
        self.file_socket.close()
        sys.exit()