class Functionalities:
    def __init__(self, clientIns) -> None:
        self.clientIns = clientIns
    def handleSubmit(self, uid, password, ip, port):
        print(uid, password, ip, port)
        credentials = {"username":uid, "password":password}
        self.clientIns.startClient(server_addr = (ip, port), server_password="qwerty", clientCredentials=credentials)
