import sys, sqlite3, matching, categ_list
from user import User

# import sqlite3
# import user_general
# import matching
# import categ_list

conn = sqlite3.connect('matching_user.db')
# conn = sqlite3.connect(':memory:')
c = conn.cursor()


def mainmenu():
    while True:
        print("""
            MAIN MENU
            1. Register
            2. Log in
        """)

        x = input("Enter choice: ")
        try:
            if int(x) == 1:
                signup()
            elif int(x) == 2:
                login()
        except:
            print("Choose either 1 or 2.")
        else:
            sys.exit()


subject_num = {
    1: "Language",
    2: "Maths",
    3: "Computing",
    4: "Humanities",  # "Arts'&'Humanities" would cause an error when making table..
    5: "Business",
}


def signup():
    global username
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
    print(">>> Current database: ")
    matching.show_all()


# search function called inside register()
def search():
    '''
    1. Ask user for conditions of a desired peer
        mandatory: category, language <-- wont be asked
        accept mismatch: age, profession, purpose
    2. Retrieve users from the same table who have match:
        [A] all the conditions
        [B] all the conditions except for one
    3. Show [A] followed by [B] with username, profession, and comment
    '''

    print("What will your peer be like?\n")
    print("Age preference:")
    while True:
        try:
            cond_minage = int(input("Minimum age (10 or upper): "))
            cond_maxage = int(input("Maximum age: "))
        except ValueError:
            print("Invalid input")
        else:
            if cond_minage < 10:
                print("Minimum age must be 10 or upper")
            elif cond_minage > cond_maxage:
                print("Enter a number {} or upper".format(cond_minage))
            else:
                # Not useful for matching so can be removed
                cond_agerange = range(cond_minage, cond_maxage)
                break

    print("Profession:")
    print(categ_list.profession)
    while True:  # Allow multiple choices!
        try:
            cond_pro = categ_list.profession[int(input("Choose one: "))]
            break
        except (KeyError, ValueError):
            print("Invalid input")

    print("Purpose of learning:")
    print(categ_list.purpose)
    while True:  # Allow multiple choices!
        try:
            cond_purpose = categ_list.purpose[int(input("Choose one: "))]
            break
        except (KeyError, ValueError):
            print("Invalid input")

    print("My preferences:\n")
    print('''
            "Subject: {}> Category: {},"
            "Language: {},"
            "Age range: {}-{},"
            "Profession: {},"
            "Purpose: {}"
            .format(subject, category, language, cond_age_min, cond_age_max)
        ''')

    print("Send a message to your peer!")
    preference = (subject, category, language, cond_minage, cond_maxage, cond_pro, cond_purpose)
    matching.find_match(preference)


# register function called inside login()
def register():
    '''
    1. Ask user to register detailed userinfo: category, language to use, age, ...
    2. Insert the data into the subject table (selected by user in signup() )
    '''
    print("Tell us about yourself :)")

    # Assign user's input to each variable
    print("\n>> Categories of your subject")
    c.execute("SELECT subject FROM user_general WHERE username=?", (username,))
    global subject
    subject = c.fetchone()[0]
    if subject == "Language":  # There must be a better way...
        print(categ_list.lang_categ)
        x = 1
    elif subject == "Maths":
        print(categ_list.maths_categ)
        x = 2
    elif subject == "Computing":
        print(categ_list.comp_categ)
        x = 3
    elif subject == "Humanities":
        print(categ_list.arthuman_categ)
        x = 4
    elif subject == "Business":
        print(categ_list.business_categ)
        x = 5
    global category
    while True:
        try:
            category = categ_list.sub_list[x][int(input("\tChoose one: "))]
            break
        except:
            print("Invalid Input")

    print("\n>> Language you want to use for this program")
    print(categ_list.language)
    global language
    while True:
        try:
            language = categ_list.language[int(input("\tChoose one: "))]
            break
        except:
            print("Invalid Input")

    while True:
        try:
            age = int(input("\n>> What is your age (\"No need to mention\": Press 0): "))
            break
        except:
            print("Invalid Input")

    print("\n>> I am ...")
    print(categ_list.profession)
    while True:
        try:
            profession = categ_list.profession[int(input("\tChoose one: "))]
            break
        except:
            print("Invalid Input")

    print("\n>> I learn ...")
    print(categ_list.purpose)
    while True:
        try:
            purpose = categ_list.purpose[int(input("\tChoose one: "))]
            break
        except:
            print("Invalid Input")

    comment = input("\n>> Let your peers know about yourself! ")

    # UGLY. SHORTEN!!
    # user_d = User_details(username, category, language, age, profession, purpose, comment)
    query = "INSERT INTO {} VALUES (:username, :category, :subcategory, :language, :age, :profession, :purpose, :comment)".format(
        subject)
    with conn:
        c.execute(query, {
            'username': username,
            'category': category,
            'subcategory': None,
            'language': language,
            'age': age,
            'profession': profession,
            'purpose': purpose,
            'comment': comment})

    # Insert '1' to the column "registered" in Table "user_general"
    matching.flag_registered(username)
    print("\nYour information has been registered.")

    go_to_search = int(input("Are you looking for a learning peer? (YES: 1 / NO: 2) "))
    if go_to_search == 1:
        search()
    elif go_to_search == 2:
        pass
    else:
        print("Choose either 1 or 2.")


def login():
    print("WELCOME BACK")
    notloggedin = True  # set a boolean flag to True if the user is NOT logged in

    while notloggedin:
        global username
        username = input("Username: ")
        pwd = input("Login password: ")

        c.execute("SELECT * FROM user_general WHERE username=? AND pwd=?", (username, pwd))
        id_match = c.fetchall()
        if id_match:
            notloggedin = False
            print("Successfully logged in!\n")
            break
        else:
            print("Wrong username or password (Case sensitive!)")

    # If there is no registered record in the subject table, ask for registration
    if not matching.if_registered(username):
        print("You haven't been registered your profile yet.")
        register()  # defined in 4_register.py
    else:
        go_to_search = int(input("Are you looking for a learning peer? (YES: 1 / NO: 2) "))
        if go_to_search == 1:
            search()  # defined in 3_search.py
        elif go_to_search == 2:
            pass
        else:
            print("Choose either 1 or 2.")


mainmenu()
