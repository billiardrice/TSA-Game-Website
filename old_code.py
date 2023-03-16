import database
from auth import Account

db = database.Database()
db.clean()
db = database.Database()
db.addUser(Account("email@email", "password", "name", "picture"))
db.login(Account("email@email", "password"))

while True:
    action = input("(R)egister or (L)ogin:\n")
    if action.strip().lower() == 'r':
        acc = Account(input("Enter email: ").strip().lower(),
                input("Enter password: ").strip().lower(),
                input("Enter username: ").strip().lower(),
                input("Upload Photo: ").strip().lower())
        try:
            db.addUser(acc)
        except database.AccountError as e:
            print(e)

    elif action.strip().lower() == 'l':
        acc = Account(input("Enter email: ").strip().lower(),
                input("Enter password: ").strip().lower())
        try:
            db.login(acc)
            print(acc.username)
        except database.AccountNotFound as e:
            print(e)