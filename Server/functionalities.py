import os
import sys
import socket
import json
import time
from threading import Thread, Lock, current_thread
from queue import Queue

from colors import bcolors
from .database.methods import Database_Methods


def encodeJSON(input: dict):
    return str(json.dumps(input)).encode()


class Functionalities(Database_Methods):
    def __init__(self):
        self.__lock = Lock()
        self._server_password = None
        self.allClients = {}

    def _checkForServerPassword(self, client: tuple):
        conn, addr = client
        # receiving password from the client
        client_response = str(conn.recv(4096), 'utf-8')
        if len(client_response) == 0:
            # client has disconnected from server
            conn.close()
            sys.exit()  # exists from the thread
        client_response = json.loads(client_response)

        if client_response['type'] == 'server_password':
            pwd = client_response["data"]
            if pwd != self._server_password:
                raise Exception("Server password did not match!")
        else:
            raise Exception("You are not authenticated, request dropped.")
        response = {"type": "client_request_response",
                    "data": "Server password check successfull.", "error": None}
        conn.sendall(encodeJSON(response))

        # print("PASSED _checkForServerPassword")

        time.sleep(0.1)

    def _authenticateClient(self, client: tuple):
        conn, addr = client
        # receiving credentials from the client
        client_response = str(conn.recv(4096), 'utf-8')
        if len(client_response) == 0:
            # client has disconnected from server
            conn.close()
            sys.exit()  # exists from the thread
        client_response = json.loads(client_response)

        if client_response["type"] == 'client_authentication':
            clientID, username = self._checkLoginCredentials(
                addr, client_response["data"])
        else:
            raise Exception("You are not authenticated, request dropped.")

        if clientID in self.allClients.keys():
            raise Exception(
                f'You are already logged with other address {self.allClients[clientID].clientIP}:{self.allClients[clientID].port1}')
        response = {"type": "client_request_response",
                    "data": f'Authenticated successfully', "error": None}

        conn.sendall(encodeJSON(response))

        # print("PASSED _authenticateClient")

        time.sleep(0.1)
        return clientID, username

    def _getMetadataFromClient(self, clientID: int, client: tuple):
        conn, addr = client

        # receiving metadata from the client
        client_response = str(conn.recv(4096), 'utf-8')
        if len(client_response) == 0:
            # client has disconnected from server
            self._closeClientConnection(clientID)
            sys.exit()  # exists from the thread
        client_response = json.loads(client_response)

        if client_response["type"] == 'client_ports':
            metadata = client_response["data"]
            self._updateClientMetadata(clientID, metadata)
            fileList = self._getClientFiles(clientID)
            members = self._getAllMembers()
        else:
            self._closeClientStatus(clientID)
            raise Exception("You are not authenticated, request dropped.")
        server_response = {"type": "client_request_response", "data": {
            "fileList": fileList, "clientID": clientID, "members": members}, "error": None}
        conn.sendall(encodeJSON(server_response))

        # print("PASSED _getMetadataFromClient")

        time.sleep(0.1)
        return metadata

    def _heatbeatCheck(self, clientID: int):
        conn, addr = self.allClients[clientID].client
        while True:
            ipList = []
            for ID, clientOBJ in self.allClients.items():
                ipList.append((clientOBJ.username, ID))
            update = {"type": "server_update", "data": ipList}
            if clientID in self.allClients.keys():
                self.allClients[clientID].sendQueue.put(update)
            else:
                sys.exit()
            time.sleep(5)

    def _listenClientForRequests(self, clientID: int):
        conn, addr = self.allClients[clientID].client
        # Listening to clients for requests
        while True:
            try:
                client_request = str(conn.recv(4096), 'utf-8')
                if len(client_request) == 0:
                    # client has disconnected from server
                    self._closeClientConnection(clientID)
                    sys.exit()  # exists from the thread
                client_request = json.loads(client_request)

                # send_message
                if client_request["type"] == 'send_message':
                    ##request["data"] = {sender:senderID,receiver:receiverID,message:str}
                    data = client_request["data"]
                    if data["receiver"] in self.allClients.keys():
                        self.allClients[data["receiver"]
                                        ].sendQueue.put(client_request)
                    else:
                        server_response = {"type": "client_request_response_SM", "data": None,
                                           "error": "Failed to send message,client went offline!"}
                        self.allClients[data["sender"]
                                        ].sendQueue.put(server_response)

                # update_client_username
                elif client_request["type"] == "update_client_username":
                    server_response = {"type": "client_request_response_UU",
                                       "data": "Successfully updated your username.", "error": None}
                    # request["data"] = username:str
                    newUsername = client_request["data"]
                    try:
                        self._updateClientUsername(clientID, newUsername)
                        with self.__lock:
                            self.allClients[clientID].username = newUsername
                    except Exception as error:
                        server_response = {
                            "type": "client_request_response_UU", "data": None, "error": str(error)}
                    self.allClients[clientID].sendQueue.put(server_response)

                # get client's file sharing address
                elif client_request["type"] == "get_addr":
                    ID = client_request["data"]
                    if ID in self.allClients.keys():
                        IP = self.allClients[ID].clientIP
                        port2 = self.allClients[ID].port2
                        server_response = {"type": "client_request_response_GP", "data": (
                            IP, port2), "error": None}
                    else:
                        server_response = {"type": "client_request_response_GP",
                                           "data": None, "error": "Failed client went offline!"}
                    self.allClients[clientID].sendQueue.put(server_response)

                # get client's files sharing list
                elif client_request["type"] == "get_file_list":
                    ID = client_request["data"]
                    try:
                        fileList = self._getClientFiles(clientID=ID)
                        server_response = {
                            "type": "client_request_response_GF", "data": fileList, "error": None}
                    except Exception as e:
                        server_response = {
                            "type": "client_request_response_GF", "data": None, "error": str(error)}
                    self.allClients[clientID].sendQueue.put(server_response)

                # insert new files to  client's sharing list
                elif client_request["type"] == "insert_new_files":
                    files = client_request["data"]
                    try:
                        fileIDs = self._inserFilesToClientSharedFilelist(
                            clientID=clientID, files=files)
                        server_response = {
                            "type": "client_request_response_INF", "data": fileIDs, "error": None}
                    except Exception as error:
                        server_response = {
                            "type": "client_request_response_INF", "data": None, "error": str(error)}
                    self.allClients[clientID].sendQueue.put(server_response)

                # delete listed file of client
                elif client_request["type"] == "delete_file":
                    fileID = client_request["data"]
                    try:
                        self._deleteFile(fileID)
                        server_response = {
                            "type": "client_request_response_DF", "data": "Success", "error": None}
                    except Exception as error:
                        server_response = {
                            "type": "client_request_response_DF", "data": None, "error": str(error)}
                    self.allClients[clientID].sendQueue.put(server_response)

                # Search files
                elif client_request["type"] == "search_file":
                    filename = client_request["data"]
                    try:
                        res = self._searchFile(clientID, filename)
                        server_response = {
                            "type": "client_request_response_SF", "data": res, "error": None}
                    except Exception as error:
                        server_response = {
                            "type": "client_request_response_SF", "data": None, "error": str(error)}
                    self.allClients[clientID].sendQueue.put(server_response)
                
                # get public key
                elif client_request["type"] == "get_pubkey":
                    ID = client_request["data"]
                    try:
                        res = self._getClientPubkey(ID)
                        server_response = {
                            "type": "client_request_response_CPK", "data": res, "error": None}
                    except Exception as error:
                        server_response = {
                            "type": "client_request_response_CPK", "data": None, "error": str(error)}
                    self.allClients[clientID].sendQueue.put(server_response)
            except socket.error as error:
                print(f'{bcolors["FAIL"]}[SERVER]Failed to keep listening to the client!{bcolors["ENDC"]}{bcolors["UNDERLINE"]}{self.allClients[clientID].clientIP}{bcolors["ENDC"]}')
                print(f'{bcolors["HEADER"]}Reason:{bcolors["ENDC"]} {error}')
                self._closeClientConnection(clientID)
                sys.exit()  # exists from the thread

    def _sendResponseToClients(self, clientID: int):
        conn, addr = self.allClients[clientID].client
        while True:
            request = self.allClients[clientID].sendQueue.get()
            try:
                if request["type"] == "close_thread":
                    sys.exit()
                # server_update
                if request["type"] == "server_update" or "client_request_response" in request["type"]:
                    conn.sendall(encodeJSON(request))
                elif request["type"] == "send_message":
                    data = request["data"]
                    sendMsg = {"type": "got_message", "data": data}
                    conn.sendall(encodeJSON(sendMsg))
                    # Send success message to sender
                    if data["sender"] in self.allClients.keys():
                        res = {"type": "client_request_response_SM",
                               "data": "Message delivered", "error": None}
                        self.allClients[data["sender"]].sendQueue.put(res)
            except Exception as e:
                if request["type"] == "send_message":
                    # Send Failed message to sender
                    data = request["data"]
                    if data["sender"] in self.allClients.keys():
                        res = {"type": "client_request_response_SM", "data": None,
                               "error": f'Failed to send "{data["message"]}"'}
                        self.allClients[data["sender"]].sendQueue.put(res)
                sys.exit()
            self.allClients[clientID].sendQueue.task_done()

    def _closeClientConnection(self, clientID: int):
        print(f'{bcolors["OKGREEN"]}[SERVER]{bcolors["ENDC"]}Closing connection with {self.allClients[clientID].username} := {bcolors["UNDERLINE"]}{self.allClients[clientID].clientIP}{bcolors["ENDC"]}')
        conn, addr = self.allClients[clientID].client
        conn.close()
        try:
            self._closeClientStatus(clientID)
            self.allClients[clientID].sendQueue.put({"type": "close_thread"})
        except:
            pass
        with self.__lock:
            del self.allClients[clientID]

    def _getClient(self, clientID: int):
        for client in self.allClients:
            if clientID == client["clientID"]:
                return client
        raise Exception("Client went offline!message dropped")
