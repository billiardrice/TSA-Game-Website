import bcrypt

class Account:
    def __init__(self, email, password, username=None, picture=None):
        self.email = email
        self.password = password
        
        bytes = password.encode('utf-8')
        salt = bcrypt.gensalt()
        hash = bcrypt.hashpw(bytes, salt)
        self.hash = hash

        self.username = username
        self.picture = picture

    def check(self, hash):
        check = bcrypt.checkpw(self.password.encode('utf-8'), hash)
        return check