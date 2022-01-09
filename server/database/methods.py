import mysql.connector
from database.connection import Database

class Database_Methods(Database):
    def __init__(self):
        Database.__init__(self)
    
    def _checkLoginCredentials(self,credentials):
        try:
            username = credentials["username"]
            password = credentials["password"]
            operation = f'SELECT clientID,username,password FROM clients WHERE username=%s'
            curr = self.dbConn.cursor()
            curr.execute(operation,(username,password))
            res = curr.fetchone()
            if len(res) == 0:
                err_msg = "No such username found!"
                raise err_msg
            pwd = res[2]
            if pwd == password:
                return (res[0],res[1])
            err_msg = "Password did not match!"
            raise err_msg
        except mysql.connector.Error as error:
            print(f'{bcolors["FAIL"]}[DATABASE] Failed to check login Credentials {bcolors["ENDC"]}')
            print(f'{bcolors["HEADER"]}Reason:{bcolors["ENDC"]} {error}')
            err_msg = f'INTERNAL SERVER ERROR'
            raise err_msg
    
    def _createNewProfile(self,data: dict):
        try:
            username = credentials["username"]
            ##check if username already exists
            operation = f'SELECT clientID FROM clients WHERE username=%s'
            curr = self.dbConn.cursor()
            curr.execute(operation,(username,))
            res = curr.fetchall()
            if len(res) > 0:
                err_msg = f'Username "{username}" already exists.'
                raise err_msg
            password = credentials["password"]
            operation = f'INSERT INTO clients (username, password) VALUES (%s,%s)'
            curr = self.dbConn.cursor()
            curr.execute(operation,(username,password))
            self.dbConn.commit()
            clientID = curr.lastrowid
            return (clientID,username)
        except mysql.connector.Error as error:
            print(f'{bcolors["FAIL"]}[DATABASE] Failed to create profile {bcolors["ENDC"]}')
            print(f'{bcolors["HEADER"]}Reason:{bcolors["ENDC"]} {error}')
            err_msg = f'INTERNAL SERVER ERROR'
            raise err_msg
    
    def _updateClientUsername(self,clientID: int,newUsername:str):
        try:
            operation = """
            UPDATE clients
            SET username=%s
            WHERE clientID=%s
            """
            curr = self.dbConn.cursor()
            curr.execute(operation,(newUsername,clientID))
            self.dbConn.commit()
        except mysql.connector.Error as error:
            print(f'{bcolors["FAIL"]}[DATABASE] Failed to update client username{bcolors["ENDC"]}')
            print(f'{bcolors["HEADER"]}Reason:{bcolors["ENDC"]} {error}')
            err_msg = f'INTERNAL SERVER ERROR'
            raise err_msg
    
    def _updateClientMetadata(self,clientID: int,metadata: dict):
        try:
            operation = """
            UPDATE clients
            SET status=%s,ip=%s, port1=%s, port2=%s
            WHERE clientID=%s
            """
            curr = self.dbConn.cursor()
            curr.execute(operation,(True,metadata["ip"],int(metadata["port1"]),int(metadata["port2"],clientID)))
            self.dbConn.commit()
        except mysql.connector.Error as error:
            print(f'{bcolors["FAIL"]}[DATABASE] Failed to update client metadata{bcolors["ENDC"]}')
            print(f'{bcolors["HEADER"]}Reason:{bcolors["ENDC"]} {error}')
            err_msg = f'INTERNAL SERVER ERROR'
            raise err_msg
        
    def _updateClientSharableFilesPath(self,clientID: int):
        pass
    
    def _getClientDetails(self,clientID: int):
        try:
            operation = f'SELECT * FROM clients WHERE clientID ={clientID}'
            curr = self.dbConn.cursor()
            curr.execute(operation)
            res = curr.fetchone()
            return res
        except mysql.connector.Error as error:
            print(f'{bcolors["FAIL"]}[DATABASE] Failed to get client details {bcolors["ENDC"]}')
            print(f'{bcolors["HEADER"]}Reason:{bcolors["ENDC"]} {error}')
            err_msg = f'INTERNAL SERVER ERROR'
            raise err_msg
        
    
    def _getClientSharableFilesPath(self,clientID: int):
        pass
    
    def _closeClientConnection(self,clientID: int):
        try:
            operation = """
            UPDATE clients
            SET status=%s
            WHERE clientID=%s
            """
            curr = self.dbConn.cursor()
            curr.execute(operation,(False,clientID))
            self.dbConn.commit()
        except mysql.connector.Error as error:
            print(f'{bcolors["FAIL"]}[DATABASE] Failed to close client\'s connection{bcolors["ENDC"]}')
            print(f'{bcolors["HEADER"]}Reason:{bcolors["ENDC"]} {error}')
            err_msg = f'INTERNAL SERVER ERROR'
            raise err_msg