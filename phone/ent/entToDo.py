class eToDo:
    def __init__(self):
        self._id = ''
        self._task = ''
        self._description = ''
        
    def set_id(self, id):
        self._id = id
        
    def set_task(self, task):
        self._task = task
        
    def set_description(self, description):
        self._description = description
        
    def get_id(self):
        return self._id
        
    def get_task(self):
        return self._task
        
    def get_description(self):
        return self._description