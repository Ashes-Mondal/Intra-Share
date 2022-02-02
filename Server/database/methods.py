import os
import sys

import bcrypt
import mysql.connector
from colors import bcolors

from .connection import Database


class Database_Methods:
    def startDB(self):
        self.db = Database()
        self.dbConn = self.db.dbConn
        self.dbConfig = self.db.dbConfig
        self.dbName = self.db.dbName

    def _checkLoginCredentials(self, addr: tuple, credentials: dict):
        try:
            username = credentials["username"]
            password = credentials["password"]
            operation = f'SELECT clientID,password FROM clients WHERE BINARY username=%s'
            curr = self.dbConn.cursor()
            curr.execute(operation, (username,))
            res = curr.fetchone()
            if res == None:
                # creating new profile
                return self._createNewProfile(addr, credentials)
            # checking if passwords matches
            (clientID, hashed_password) = res
            if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')) == False:
                err_msg = "User password did not match!"
                raise Exception(err_msg)
            operation = """
            UPDATE clients
            SET ip=%s,port1=%s
            WHERE clientID=%s"""
            curr.execute(operation, (addr[0], addr[1], clientID))
            return (clientID, username)
        except mysql.connector.Error as error:
            print(
                f'{bcolors["FAIL"]}[DATABASE] Failed to check login Credentials {bcolors["ENDC"]}')
            print(f'{bcolors["HEADER"]}Reason:{bcolors["ENDC"]} {error}')
            err_msg = f'INTERNAL SERVER ERROR'
            raise Exception(err_msg)

    def _createNewProfile(self, addr: tuple, credentials: dict):
        try:
            username = credentials["username"]
            password = bcrypt.hashpw(
                credentials["password"].encode('utf-8'), bcrypt.gensalt())
            IP, port1 = addr
            operation = f'INSERT INTO clients (username, password, ip, port1) VALUES (%s,%s,%s,%s)'
            curr = self.dbConn.cursor()
            curr.execute(operation, (username, password, IP, port1))
            self.dbConn.commit()
            clientID = curr.lastrowid
            return (clientID, username)
        except mysql.connector.Error as error:
            print(
                f'{bcolors["FAIL"]}[DATABASE] Failed to create profile {bcolors["ENDC"]}')
            print(f'{bcolors["HEADER"]}Reason:{bcolors["ENDC"]} {error}')
            err_msg = f'INTERNAL SERVER ERROR'
            raise Exception(err_msg)

    def _updateClientUsername(self, clientID: int, newUsername: str):
        try:
            operation = "SELECT clientID FROM clients WHERE BINARY username=%s"
            curr = self.dbConn.cursor()
            curr.execute(operation, (newUsername,))
            res = curr.fetchone()
            if res != None:
                raise Exception(
                    f'Failed to update username, "{newUsername}" already taken!')
            operation = """
            UPDATE clients
            SET username=%s
            WHERE clientID=%s
            """
            curr.execute(operation, (newUsername, clientID))
            self.dbConn.commit()
        except mysql.connector.Error as error:
            print(
                f'{bcolors["FAIL"]}[DATABASE] Failed to update client username{bcolors["ENDC"]}')
            print(f'{bcolors["HEADER"]}Reason:{bcolors["ENDC"]} {error}')
            err_msg = f'INTERNAL SERVER ERROR'
            raise Exception(err_msg)

    def _updateClientMetadata(self, clientID: int, metadata: dict):
        try:
            operation = """
            UPDATE clients
            SET status=%s, port1=%s, port2=%s, pubkey=%s
            WHERE clientID=%s
            """
            curr = self.dbConn.cursor()
            curr.execute(
                operation, (True, metadata["port1"], metadata["port2"],metadata["pubkey"], clientID))
            self.dbConn.commit()
        except mysql.connector.Error as error:
            print(
                f'{bcolors["FAIL"]}[DATABASE] Failed to update client metadata{bcolors["ENDC"]}')
            print(f'{bcolors["HEADER"]}Reason:{bcolors["ENDC"]} {error}')
            err_msg = f'INTERNAL SERVER ERROR'
            raise Exception(err_msg)

    def _getClientDetails(self, clientID: int):
        try:
            operation = f'SELECT * FROM clients WHERE clientID ={clientID}'
            curr = self.dbConn.cursor()
            curr.execute(operation)
            res = curr.fetchone()
            return res[0]
        except mysql.connector.Error as error:
            print(
                f'{bcolors["FAIL"]}[DATABASE] Failed to get client details {bcolors["ENDC"]}')
            print(f'{bcolors["HEADER"]}Reason:{bcolors["ENDC"]} {error}')
            err_msg = f'INTERNAL SERVER ERROR'
            raise Exception(err_msg)
    
    def _getClientPubkey(self, clientID: int):
        try:
            operation = f'SELECT pubkey FROM clients WHERE clientID =%s'
            curr = self.dbConn.cursor()
            curr.execute(operation,(clientID,))
            res = curr.fetchone()
            return res[0]
        except mysql.connector.Error as error:
            print(
                f'{bcolors["FAIL"]}[DATABASE] Failed to get client public key {bcolors["ENDC"]}')
            print(f'{bcolors["HEADER"]}Reason:{bcolors["ENDC"]} {error}')
            err_msg = f'INTERNAL SERVER ERROR'
            raise Exception(err_msg)

    def _getClientFiles(self, clientID: int):
        try:
            operation = """SELECT files.fileID, files.filename, files.filesize, files.path, clients.clientID, clients.username,clients.status 
            FROM files INNER JOIN clients 
            ON (clients.clientID = files.clientID) 
            WHERE clients.clientID = %s"""
            curr = self.dbConn.cursor()
            curr.execute(operation, (clientID,))
            res = curr.fetchall()
            return res or []
        except mysql.connector.Error as error:
            print(
                f'{bcolors["FAIL"]}[DATABASE] Failed to get client\'s shared filelist {bcolors["ENDC"]}')
            print(f'{bcolors["HEADER"]}Reason:{bcolors["ENDC"]} {error}')
            err_msg = f'INTERNAL SERVER ERROR'
            raise Exception(err_msg)

    def _inserFilesToClientSharedFilelist(self, clientID: int, files: list):
        try:
            operation = f'INSERT INTO files (filename, filesize, path, clientID) VALUES (%s,%s,%s,%s)'
            curr = self.dbConn.cursor()
            fileIDs = []
            for file in files:
                filename, filesize, path = file
                try:
                    curr.execute(
                        operation, (filename, filesize, path, clientID))
                    fileID = curr.lastrowid
                    fileIDs.append(fileID)
                except Exception as error:
                    print(
                        f'{bcolors["FAIL"]}[DATABASE] Failed to insert client\'s file{bcolors["ENDC"]}')
                    print(
                        f'{bcolors["HEADER"]}Reason:{bcolors["ENDC"]} {error}')
                    fileIDs.append(None)
            self.dbConn.commit()
            return fileIDs
        except mysql.connector.Error as error:
            print(
                f'{bcolors["FAIL"]}[DATABASE] Failed to insert files {bcolors["ENDC"]}')
            print(f'{bcolors["HEADER"]}Reason:{bcolors["ENDC"]} {error}')
            err_msg = f'INTERNAL SERVER ERROR'
            raise Exception(err_msg)

    def _deleteFile(self, fileID: int):
        try:
            operation = f'DELETE FROM files WHERE fileID = %s'
            curr = self.dbConn.cursor()
            curr.execute(operation, (fileID,))
            self.dbConn.commit()
        except mysql.connector.Error as error:
            print(
                f'{bcolors["FAIL"]}[DATABASE] Failed to insert files {bcolors["ENDC"]}')
            print(f'{bcolors["HEADER"]}Reason:{bcolors["ENDC"]} {error}')
            err_msg = f'INTERNAL SERVER ERROR'
            raise Exception(err_msg)

    def _searchFile(self, clientID: int, filename: str):
        try:
            search = f'%{filename}%'
            operation = """SELECT files.fileID, files.filename, files.filesize, clients.clientID, clients.username,clients.status  
                FROM files INNER JOIN clients 
                ON (files.clientID = clients.clientID)
                WHERE (clients.clientID != %s AND files.filename LIKE %s);"""
            curr = self.dbConn.cursor()
            curr.execute(operation, (clientID, search))
            res = curr.fetchall()
            return res
        except mysql.connector.Error as error:
            print(
                f'{bcolors["FAIL"]}[DATABASE] Failed to search files {bcolors["ENDC"]}')
            print(f'{bcolors["HEADER"]}Reason:{bcolors["ENDC"]} {error}')
            err_msg = f'INTERNAL SERVER ERROR'
            raise Exception(err_msg)

    def _getAllMembers(self):
        try:
            operation = """SELECT clientID,username FROM clients"""
            curr = self.dbConn.cursor()
            curr.execute(operation)
            members = curr.fetchall()
            return members
        except mysql.connector.Error as error:
            print(
                f'{bcolors["FAIL"]}[DATABASE] Failed to close client\'s connection{bcolors["ENDC"]}')
            print(f'{bcolors["HEADER"]}Reason:{bcolors["ENDC"]} {error}')
            err_msg = f'INTERNAL SERVER ERROR'
            raise Exception(err_msg)

    def _closeClientStatus(self, clientID: int):
        try:
            operation = """
            UPDATE clients
            SET status=%s
            WHERE clientID=%s
            """
            curr = self.dbConn.cursor()
            curr.execute(operation, (False, clientID))
            self.dbConn.commit()
        except mysql.connector.Error as error:
            print(
                f'{bcolors["FAIL"]}[DATABASE] Failed to close client\'s connection{bcolors["ENDC"]}')
            print(f'{bcolors["HEADER"]}Reason:{bcolors["ENDC"]} {error}')
            err_msg = f'INTERNAL SERVER ERROR'
            raise Exception(err_msg)
