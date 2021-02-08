import sqlite3
from user import User
import matching

conn = sqlite3.connect('matching_user.db')
# conn = sqlite3.connect(':memory:')
c = conn.cursor()

subject_num = {
        1: "Language",
        2: "Maths",
        3: "Computing",
        4: "Humanities",
        5: "Business",
    }

def signup():
    print("WELCOME")

    # Ask user for details
    # If the username is already in the database, cause an error
    unique_name = False
    while not unique_name:
        username = input("Username: ")
        c.execute("SELECT username FROM user_general WHERE username=?", (username,))
        same_name = c.fetchone()
        if same_name:
            print("This username is taken.")
        else:
            unique_name = True
            break

    pwd = input("Password: ")
    print(subject_num)
    subject = int(input("What do you want to learn?  Enter the number: "))

    user = User(username, pwd, subject_num[subject])
    matching.insert_one(user)

    print("Account created!")


signup()
