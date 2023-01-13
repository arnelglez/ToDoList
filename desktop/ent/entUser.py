class eUser:
    
    def __init__(self):
        self._id = ''
        self._username = ''
        self._email = ''
        self._first_name = ''
        self._last_name = ''
        self._password1 = ''
        self._password2 = ''
        self._is_superuser = ''
        self._is_staff = ''
        
    def set_id(self, id):
        self._id = id
    
    def set_username(self, username):
        self._username = username
    
    def set_email(self, email):
        self._email = email
    
    def set_first_name(self, first_name):
        self._first_name = first_name
    
    def set_last_name(self, last_name):
        self._last_name = last_name
        
    def set_password1(self, password1):
        self._password1 = password1
        
    def set_password2(self, password2):
        self._password2 = password2
        
    def set_is_superuser(self, is_superuser):
        self._is_superuser = is_superuser
        
    def set_is_staff(self, is_staff):
        self._is_staff = is_staff
        
    def get_id(self):
        return self._id
    
    def get_username(self):
        return self._username
    
    def get_email(self):
        return self._email
    
    def get_first_name(self):
        return self._first_name
    
    def get_last_name(self):
        return self._last_name
        
    def get_password1(self):
        return self._password1 
        
    def get_password2(self):
        return self._password2 
        
    def get_is_superuser(self):
        return self._is_superuser
        
    def get_is_staff(self):
        return self._is_staff