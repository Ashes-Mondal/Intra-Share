import sys,os
import mysql.connector
import bcrypt
from colors import bcolors
from connection import Database

class Database_Methods: 
    def startDB(self):
        self.db = Database()
        self.dbConn = self.db.dbConn
        self.dbConfig = self.db.dbConfig
        self.dbName = self.db.dbName
    
    def _checkLoginCredentials(self,addr: tuple,credentials: dict):
        try:
            username = credentials["username"]
            password = credentials["password"]
            operation = f'SELECT clientID,password FROM clients WHERE BINARY username=%s'
            curr = self.dbConn.cursor()
            curr.execute(operation,(username,))
            res = curr.fetchone()
            if res == None:
                ##creating new profile
                return self._createNewProfile(addr,credentials)
            ##checking if passwords matches
            (clientID,hashed_password) = res
            if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')) == False:
                err_msg = "User password did not match!"
                raise Exception(err_msg)
            operation = """
            UPDATE clients
            SET ip=%s,port1=%s
            WHERE clientID=%s"""
            curr.execute(operation,(addr[0],addr[1],clientID))
            return (clientID,username)
        except mysql.connector.Error as error:
            print(f'{bcolors["FAIL"]}[DATABASE] Failed to check login Credentials {bcolors["ENDC"]}')
            print(f'{bcolors["HEADER"]}Reason:{bcolors["ENDC"]} {error}')
            err_msg = f'INTERNAL SERVER ERROR'
            raise Exception(err_msg)
    
    def _createNewProfile(self,addr: tuple,credentials: dict):
        try:
            username = credentials["username"]
            password = bcrypt.hashpw(credentials["password"].encode('utf-8'), bcrypt.gensalt()) 
            IP,port1 = addr
            operation = f'INSERT INTO clients (username, password, ip, port1) VALUES (%s,%s,%s,%s)'
            curr = self.dbConn.cursor()
            curr.execute(operation,(username,password,IP,port1))
            self.dbConn.commit()
            clientID = curr.lastrowid
            return (clientID,username)
        except mysql.connector.Error as error:
            print(f'{bcolors["FAIL"]}[DATABASE] Failed to create profile {bcolors["ENDC"]}')
            print(f'{bcolors["HEADER"]}Reason:{bcolors["ENDC"]} {error}')
            err_msg = f'INTERNAL SERVER ERROR'
            raise Exception(err_msg)
    
    def _updateClientUsername(self,clientID: int,newUsername:str):
        try:
            operation = "SELECT clientID FROM clients WHERE BINARY username=%s"
            curr = self.dbConn.cursor()
            curr.execute(operation,(newUsername,))
            res = curr.fetchone()
            if res != None:
                raise Exception(f'Failed to update username, "{newUsername}" already taken!')
            operation = """
            UPDATE clients
            SET username=%s
            WHERE clientID=%s
            """
            curr.execute(operation,(newUsername,clientID))
            self.dbConn.commit()
        except mysql.connector.Error as error:
            print(f'{bcolors["FAIL"]}[DATABASE] Failed to update client username{bcolors["ENDC"]}')
            print(f'{bcolors["HEADER"]}Reason:{bcolors["ENDC"]} {error}')
            err_msg = f'INTERNAL SERVER ERROR'
            raise Exception(err_msg)
    
    def _updateClientPorts(self,clientID: int,ports: dict):
        try:
            operation = """
            UPDATE clients
            SET status=%s, port1=%s, port2=%s
            WHERE clientID=%s
            """
            curr = self.dbConn.cursor()
            curr.execute(operation,(True,ports["port1"],ports["port2"],clientID))
            self.dbConn.commit()
        except mysql.connector.Error as error:
            print(f'{bcolors["FAIL"]}[DATABASE] Failed to update client metadata{bcolors["ENDC"]}')
            print(f'{bcolors["HEADER"]}Reason:{bcolors["ENDC"]} {error}')
            err_msg = f'INTERNAL SERVER ERROR'
            raise Exception(err_msg)
        
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
            raise Exception(err_msg)
        
    
    def _getClientSharedFilelist(self,clientID: int):
        return None
    
    def _getAllMembers(self):
        try:
            operation = """SELECT clientID,username FROM clients"""
            curr = self.dbConn.cursor()
            curr.execute(operation)
            members = curr.fetchall()
            return members
        except mysql.connector.Error as error:
            print(f'{bcolors["FAIL"]}[DATABASE] Failed to close client\'s connection{bcolors["ENDC"]}')
            print(f'{bcolors["HEADER"]}Reason:{bcolors["ENDC"]} {error}')
            err_msg = f'INTERNAL SERVER ERROR'
            raise Exception(err_msg)
    
    def _closeClientStatus(self,clientID: int):
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
            raise Exception(err_msg)