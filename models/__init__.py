

class User:

    def __init__(self, username,email,password):
        self.username = username
        self.email = email
        self.password = password
        self.details = {}

    def save_user(self):
        self.details[self.email] = self.username, self.password

