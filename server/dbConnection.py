import os,mysql.connector as connector
from colors import bcolors
from model.main import Tables

class DB:
    DB_NAME = os.getenv("DB_NAME")
    def __init__(self,config):
        try:
            self.config = config
            self.__initiateConnection(self.config)
            self.__initiateTables()
        except Exception as error:
            exit(0)
    
    def __initiateConnection(self,config):
        try:
            self.dbConn = connector.connect(**config)
            ##Creating Database if not exists
            curr = self.dbConn.cursor()
            operation = f'CREATE DATABASE IF NOT EXISTS {self.DB_NAME}'
            curr.execute(operation)
            curr.execute(f'USE {self.DB_NAME}')
            print(f'{bcolors["OKGREEN"]}Database connection initiated successfully.{bcolors["ENDC"]}')
        except Exception as error:
            print(f'{bcolors["FAIL"]} Failed to initiate connection! {bcolors["ENDC"]}')
            print(f'{bcolors["HEADER"]}Reason:{bcolors["ENDC"]} {error}')
            raise error
    
    def __initiateTables(self):
        curr = self.dbConn.cursor()
        for (name,model) in Tables:
            try:
                operation = f'CREATE TABLE IF NOT EXISTS {name} ({model})'
                curr.execute(operation)
            except Exception as error:
                print(f'{bcolors["FAIL"]}Failed to create "{name}"{bcolors["ENDC"]}')
                print(f'{bcolors["HEADER"]}Reason:{bcolors["ENDC"]}{error}')