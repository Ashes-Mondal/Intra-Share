from database.connection import Database

class Database_Methods(Database):
    def __init__(self):
        Database.__init__(self)
    
    def _checkLoginCredentials(self):
        pass
    
    def _createNewProfile(self):
        pass
    
    def _updateClientUsername(self):
        pass
    
    def _updateClientMetadata(self):
        pass
    
    def _getClientDetails(self,clientID: int):
        pass
    
    def _getClientSharableFilesPath(self,clientID: int):
        pass
    
    def _closeClientConnection(self,clientID: int):
        pass