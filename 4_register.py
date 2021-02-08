import sqlite3
from user import User_details
import matching
import categ_list

conn = sqlite3.connect('matching_user.db')
# conn = sqlite3.connect(':memory:')
c = conn.cursor()

username = "yuri"

def register():
    '''
    1. Ask user to register detailed userinfo: category, language to use, age, ...
    2. Insert the data into the subject table (selected by user in signup() )
    '''
    print("Tell us about yourself!\n")

    # Assign user's input to each variable
    c.execute("SELECT subject FROM user_general WHERE username=?", (username,))
    subject = c.fetchone()[0]
    if subject == "Language":      # There must be a better way...
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
    category = categ_list.sub_list[x][int(input("What is your category: "))]

    print(categ_list.language)
    language = categ_list.language[int(input("Choose your primary language: "))]

    age = input("What is your age (Press 0 if you don't need to mention): ")

    print(categ_list.profession)
    profession = categ_list.profession[int(input("What are you? "))]

    print(categ_list.purpose)
    purpose = categ_list.purpose[int(input(""))]

    comment = input("Let your peers know about yourself! ")

    # Insert user's input to the subject table
    # UGLY. SHORTEN!!
    user_d = User_details(username, category, language, age = age, profession, purpose, comment)

    query = "INSERT INTO {} VALUES (:username, :category, :subcategory, :language, :age, :profession, :purpose, :comment)".format(subject)
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
    print("Your information has been registered.")

register()




