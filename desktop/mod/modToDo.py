from ent.entToDo import eToDo
import requests

class mToDo:
    
    def __init__(self, token):
        self.urlBase = 'http://localhost:8000/api/todo/'
        self.headers = {
                            "Authorization": "Bearer " + token,
                            "Content-Type": "application/json",
                            "Connection": "close"
                        }
        
    def list_toDo(self):
        url = self.urlBase         
        response = requests.get(url=url,headers=self.headers)
        
        result = list()
        if response.status_code == 200:
            for item in response.json():
                etodo = eToDo()
                etodo.set_id(item['id'])
                etodo.set_task(item['task']) 
                etodo.set_description(item['description'])            
                
                result.append(etodo)
                
            return '', result
        else:
            return response.json(), result
        
    def create_toDo(self, toDo:eToDo):
        url = self.urlBase 
        json = {
            "task" : toDo.get_task(),
            "description" : toDo.get_description()
        }
        
        response = requests.post(url=url, json=json, headers=self.headers)
        
        etodo = eToDo()
        if response.status_code == 201:
            etodo.set_id(response.json()['id'])
            etodo.set_task(response.json()['task']) 
            etodo.set_description(response.json()['description'])            
            
            return '', etodo
        else:
            return response.json(), etodo
            
    
    def update_toDo(self, toDo:eToDo):
        url = self.urlBase + str(toDo.get_id())  + '/'
        json = {
            "task" : toDo.get_task(),
            "description" : toDo.get_description()
        }
        
        response = requests.put(url=url, json=json, headers=self.headers)
        
        etodo = eToDo()
        if response.status_code == 202:
            etodo.set_id(response.json()['id'])
            etodo.set_task(response.json()['task']) 
            etodo.set_description(response.json()['description'])            
            
            return '' ,etodo
        else:
            return response.json(), etodo
    
    def delete_toDo(self, id):
        url = self.urlBase + str(id) + '/'  
        json = {
            "id" : id,
        }
        
        response = requests.delete(url=url, json=json, headers=self.headers)
        
        if response.status_code == 204:
            return  ''
        else:
            return response.json()