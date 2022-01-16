import os

import mysql.connector as connector
from colors import bcolors

from .model.main import Tables

dbConfig = {"host":"localhost","user":os.getenv("DB_USER"),"password":os.getenv("DB_PASSWORD")}

class Database:
    def __init__(self):
        self.dbName = os.getenv("DB_NAME")
        try:
            self.dbConfig = dbConfig
            self.__initiateConnection(self.dbConfig)
            self.__initiateTables()
        except Exception as error:
            exit(0)
    
    def __initiateConnection(self,dbConfig):
        try:
            self.dbConn = connector.connect(**dbConfig)
            ##Creating Database if not exists
            curr = self.dbConn.cursor()
            operation = f'CREATE DATABASE IF NOT EXISTS {self.dbName}'
            curr.execute(operation)
            curr.execute(f'USE {self.dbName}')
            print(f'{bcolors["OKCYAN"]}[DATABASE]{bcolors["ENDC"]}Connection initiated.')
        except Exception as error:
            print(f'{bcolors["FAIL"]}[DATABASE] Failed to initiate connection! {bcolors["ENDC"]}')
            print(f'{bcolors["HEADER"]}Reason:{bcolors["ENDC"]} {error}')
            raise error
    
    def __initiateTables(self):
        curr = self.dbConn.cursor()
        for (name,model) in Tables:
            try:
                operation = f'CREATE TABLE IF NOT EXISTS {name} ({model})'
                curr.execute(operation)
            except Exception as error:
                print(f'{bcolors["FAIL"]}[DATABASE]Failed to create "{name}"{bcolors["ENDC"]}')
                print(f'{bcolors["HEADER"]}Reason:{bcolors["ENDC"]}{error}')
