import socket,sys,json
from colors import bcolors

def encodeJSON(input: dict):
    return str(json.dumps(input)).encode()

class FTC_struct:##File Taking Client
    clientID = None
    username = None
    files = []
    def __init__(self,clientID: int,username: str):
        self.clientID = clientID
        self.username = username

class FileSharingFunctionalities:
    def __init__(self):
        self.port2 = None##File sharing port
        self.FTCU = []##File Taking Clients from User
        
    
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