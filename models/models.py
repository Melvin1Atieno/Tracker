
class User:
    
    def __init__(self, username,email,password, admin=False):
        self.username = username
        self.email = email
        self.password = password
        self.admin = admin
              