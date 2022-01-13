import socket,sys,json
from colors import bcolors

def encodeJSON(input: dict):
    return str(json.dumps(input)).encode()


class FileSharingFunctionalities:
    def __init__(self):
        self.port2 = None##File sharing port
        self.FTCU = []##File Taking Clients from User
        
    def _connectToClient(self,clientID:int,addr: tuple):
        if addr == None:
            raise Exception("Client went offline,failed to connect")
        self.client = socket.socket()
        self.client.connect(self.server_addr)
        self.clientIP,self.port1 = self.client.getsockname()
        pass
    
    
    def _listenClientForRequests(self):
        pass
    
    def _closeFileClient(self,client: tuple):
        conn,addr = client
        conn.close()
        sys.exit()
    
    def _closeFileSocket(self):
        print(f'{bcolors["WARNING"]}[CLIENT]{bcolors["ENDC"]}Closing file socket...')
        self.file_socket.close()
        sys.exit()