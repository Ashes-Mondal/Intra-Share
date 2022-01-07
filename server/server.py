import os,sys,socket
from queue import Queue
from threading import Thread,Lock
from dotenv import load_dotenv
load_dotenv()
from dbConnection import DB
from colors import bcolors

class TCP:
    LISTEN_UPPER_LIMIT = 10
    def __init__(self,host: str = '',port: int = 0,listen: int = 10):
        try:
            self.host = host
            self.port = port
            self.connections = Queue()
            self.LISTEN_UPPER_LIMIT = listen
            self.__createSocket()
            self.__bindSocket()
            t1 = Thread(target=self.__acceptConnections,daemon=True,name=f'__acceptConnections_{self.port}')
            t1.start()
        except Exception as error:
            raise error
    
    def __createSocket(self):
        try:
            self.socket = socket.socket()
            print(f'{bcolors["OKGREEN"]}TCP socket created successfully.{bcolors["ENDC"]}')
        except socket.error as error:
            print(f'{bcolors["FAILED"]}Failed to create TCP socket!{bcolors["ENDC"]}')
            print(f'{bcolors["HEADER"]}Reason:{bcolors["ENDC"]} {error}')
            raise error
    
    def __bindSocket(self):
        try:
            self.socket.bind((self.host,self.port))
            self.host,self.port= self.socket.getsockname()
            self.socket.listen(self.LISTEN_UPPER_LIMIT)
            print(f'{bcolors["OKGREEN"]}Binding socket successfull := {self.host}:{self.port} ')
        except socket.error as error:
            print(f'{bcolors["FAILED"]}Failed to bind TCP socket to {bcolors["ENDC"]}{bcolors["UNDERLINE"]}{self.host}:{self.port}{bcolors["ENDC"]}')
            print(f'{bcolors["HEADER"]}Reason:{bcolors["ENDC"]} {error}')
    
    def __acceptConnections(self):
        ## Caches all new established connections
        while True:
            try:
                client = self.socket.accept()
                self.connections.put(client)
            except socket.error as error:
                print(f'{bcolors["FAILED"]}Failed to accept TCP connection{bcolors["ENDC"]}')
                print(f'{bcolors["HEADER"]}Reason:{bcolors["ENDC"]} {error}')
    
    def __del__(self):
        pass

def main():
    dbConfig = {
        "host":"localhost",
        "user":os.getenv("DB_USER"),
        "password":os.getenv("DB_PASSWORD"),
    }
    DB(dbConfig)

if __name__ == "__main__":
    main()
