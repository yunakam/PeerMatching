import sqlite3
from user import User
import matching

conn = sqlite3.connect('matching_user.db')
# conn = sqlite3.connect(':memory:')
c = conn.cursor()

def login():
    print("WELCOME BACK")
    notloggedin = True   # set a boolean flag to True if the user is NOT logged in

    while notloggedin:
        username = input("Username: ")
        pwd = input("Login password: ")

        c.execute("SELECT * FROM user_general WHERE username=? AND pwd=?", (username, pwd))
        id_match = c.fetchall()
        if id_match:
            notloggedin = False
            print("Successfully logged in!")
            break
        else:
            print("Wrong username or password (Case sensitive!)")

    # If there is no registered record in the subject table, ask for registration
    if not matching.if_registered(username):
        print("You haven't been registered your profile yet.")
        register()   # defined in 4_register.py
    else:
        go_to_search = int(input("Are you looking for a learning peer? (YES: 1 / NO: 2) "))
        if go_to_search == 1:
            search()   # defined in 3_search.py
        elif go_to_search == 2:
            pass
        else:
            print("Choose either 1 or 2.")

login()


