from phone.ent.entUser import eUser
import requests

class mUser:
    
    def __init__(self, token):
        self.urlBase = 'http://localhost:8000'
        self.headers = {
                            "Authorization": "Bearer " + token,
                            "Content-Type": "application/json",
                            "Connection": "close"
                        }
        
    def register_user(self, euser:eUser):
        url = self.urlBase + '/register/'
        json = {
            "username": euser.get_username(),
            "password1": euser.get_password1(),
            "password2": euser.get_password2(),
            "first_name": euser.get_first_name(),
            "last_name": euser.get_last_name(),
            "email": euser.get_email(),
            "is_superuser": euser.get_is_superuser(),
            "is_staff": euser.get_is_staff()
        }
        
        response = requests.post(url=url, json=json, headers=self.headers)
        
        user = eUser()
        if response.status_code == 201:
            user.set_id(response.json()['id'])
            user.set_username(response.json()['username'])
            user.set_email(response.json()['email'])
            user.set_first_name(response.json()['first_name'])
            user.set_last_name(response.json()['last_name'])
            user.set_is_superuser(response.json()['is_superuser'])
            user.set_is_staff(response.json()['is_staff'])
            
            return '', user
        else:
            return response.json(), user
        
    def change_password(self, password1, password2):
        url = self.urlBase + '/change_password/'
        json = {
            "password1": password1,
            "password2": password2
        }
        
        response = requests.put(url=url, json=json, headers=self.headers)
        
        user = eUser()
        
        if response.status_code == 201:
            user.set_id(response.json()['id'])
            user.set_username(response.json()['username'])
            user.set_email(response.json()['email'])
            user.set_first_name(response.json()['first_name'])
            user.set_last_name(response.json()['last_name'])
            user.set_is_superuser(response.json()['is_superuser'])
            user.set_is_staff(response.json()['is_staff'])
            
            return '', user
        else:
            return response.json(), user