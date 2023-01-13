from ent.entUser import eUser

class eLogin:
    
    def __init__(self):
        self._token = ''
        self._refresh = ''
        self.euser = eUser()
        
    def set_token(self, token):
        self._token = token
        
    def set_refresh(self, refresh):
        self._refresh = refresh
        
    
    def get_token(self):
        return self._token
    
    def get_refresh(self):
        return self._refresh