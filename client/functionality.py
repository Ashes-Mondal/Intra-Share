class Functionalities:
    def __init__(self, clientIns) -> None:
        self.clientIns = clientIns
    def handleSubmit(self, userid, password, serverip, port, serverPassword):
        print(userid, password, serverip, port, serverPassword)
        credentials = {"username": userid, "password": password}
        self.clientIns.startClient(
            server_addr = (serverip, port),
            server_password=serverPassword,
            clientCredentials=credentials
        )
