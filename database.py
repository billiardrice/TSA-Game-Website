import sqlite3
from auth import Account

class Database:
    def connect(self):
        self.conn = sqlite3.connect('users.db')
        return self.conn.cursor()
    
    def disconnect(self):
        self.conn.commit()
        self.conn.close()

    def __init__ (self):
        c = self.connect()

        try:
            c.execute("""
            CREATE TABLE users (
                name text,
                email text,
                password text,
                picture blob
            )""")
        except sqlite3.OperationalError:
            print("Table already exists")

        self.disconnect()

    def addUser(self, user: Account):
        c = self.connect()

        if user.username == None:
            raise AccountError("Missing Username")
        if user.picture == None:
            raise AccountError("Missing User Picture")

        c.execute("SELECT * FROM users WHERE name=:name", {'name':user.username})
        if len(c.fetchall()) > 0:
            self.disconnect()
            raise AccountError("Username Taken")
        
        c.execute("SELECT * FROM users WHERE email=:email", {'email':user.email})
        if len(c.fetchall()) > 0:
            self.disconnect()
            raise AccountError("Email Taken")
        
        c.execute("INSERT INTO users VALUES (:name, :email, :password, :picture)",
           {'name':user.username,
            'email':user.email,
            'password':user.hash,
            'picture':user.picture
            })    
        
        self.disconnect()
    
    def clean(self):
        c = self.connect()

        c.execute("DROP TABLE users")

        self.disconnect()

    def login(self, user: Account):
        c = self.connect()

        c.execute("SELECT * FROM users WHERE email=:email", {'email':user.email})
        userdb = c.fetchone()
        if userdb == None:
            raise AccountNotFound

        if not user.check(userdb[2]):
            raise PasswordIncorrect
        
        user.username = userdb[0]
        user.picture = userdb[3]

class AccountError(Exception):
    def __init__(self, value): 
        self.value = value
    def __str__(self): 
        return f"Account Error: {self.value}"

class AccountNotFound(Exception):
    def __str__(self): 
        return f"Account Not Found"

class PasswordIncorrect(Exception):
    def __str__(self): 
        return f"Incorrect Password"