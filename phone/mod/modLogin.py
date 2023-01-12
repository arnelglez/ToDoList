from ent.entLogin import eLogin
import requests

class mLogin:
    
    def __init__(self):
        self.urlBase = 'http://localhost:8000'
        
    
    def login(self, username , password):
        url = self.urlBase + '/login/'
        data = {
            "username" : username,
            "password" : password
        }
        
        response = requests.post(url=url, data=data)
        
        elogin = eLogin()
        if response.status_code == 200:
            elogin.set_token(response.json()['token'])
            elogin.set_refresh(response.json()['refresh'])
            elogin.euser.set_id(response.json()['user'].get('id'))
            elogin.euser.set_username(response.json()['user'].get('username'))
            elogin.euser.set_email(response.json()['user'].get('email'))
            elogin.euser.set_first_name(response.json()['user'].get('first_name'))
            elogin.euser.set_last_name(response.json()['user'].get('last_name'))
            elogin.euser.set_is_superuser(response.json()['user'].get('is_superuser'))
            elogin.euser.set_is_staff(response.json()['user'].get('is_staff'))
           
            return '', elogin
        else:
            return response.json(), elogin
        
    def refresh_token(self, elogin:eLogin):
        
        url = self.urlBase + '/token/refresh/'
        data = {
            "refresh" : elogin.get_refresh()
        }
        
        response = requests(url=url, data=data)
        elogin.get_token(response.json()['access'])
        elogin.get_refresh(response.json()['refresh'])
        
        return elogin
        
        
    def logout(self, token):
        
        url = self.urlBase + '/logout/'
        headers = {
                        "Authorization": "Bearer " + token,
                        "Content-Type": "application/json",
                        "Connection": "close"
                    }
        response = requests.post(ur=url, headers=headers)
        
        if response.status_code == 200:
            return  '' , response.json()
        else:
            return 'No', response.json()