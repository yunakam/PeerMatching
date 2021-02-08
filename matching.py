import sqlite3
from user import User

conn = sqlite3.connect('matching_user.db')
# conn = sqlite3.connect(':memory:')   # It makes the code start from scratch and overwrite the data
c = conn.cursor()


### Inserting data
# Insert a user's basic data into Table "user_general"
def insert_one(user):  # Method using dictionary
    with conn:
        c.execute("INSERT INTO user_general VALUES (:username, :pwd, :subject, :registered)",
                  {'username': user.username, 'pwd': user.pwd, 'subject': user.subject, 'registered': 0})

    # user = User(username, pwd, subject_num[subject])
    # matching.insert_one(user)


def insert_one2(user):  # Method using tuple
    with conn:
        c.execute("INSERT INTO user_general VALUES (?, ?, ?)", (user.username, user.pwd, user.subject))


# Insert a user's detailed data into the corresponding sublist table
# NOT COMPLETE
# def insert_to_sublist(user_d):
#     c.execute("SELECT subject FROM user_general WHERE username=?", (username,))
#     subject = c.fetchone()[0]
#
#     # query = "INSERT INTO {} VALUES (:username, :category, :subcategory, :language, :age, :profession, :purpose, :comment)".format(subject)
#     query = "INSERT INTO {} VALUES (?, ?, ?, ?, ?, ?, ?, ?)".format(subject)
#     with conn:
#         c.execute(query, {
#                 'username': user_d.username,
#                 'category': user_d.category,
#                 'subcateg': user_d.subcateg,
#                 'language': user_d.language,
#                 'age': user_d.age,
#                 'profession': user_d.profession,
#                 'purpose': user_d.purpose,
#                 'comment': user_d.comment})

# query = "INSERT INTO {} VALUES (:username, :category, :subcategory, :language, :age, :profession, :purpose, :comment)".format("Computing")
# with conn:
#     c.execute(query, {
#         'username': username,
#         'category': category,
#         'subcategory': None,
#         'language': language,
#         'age': age,
#         'profession': profession,
#         'purpose': purpose,
#         'comment': comment})

### Show the entire data of table
# Show user_general
def show_all():
    c.execute("SELECT rowid, * FROM user_general")
    items = (c.fetchall())
    for item in items:
        print(item)


# Show a given table
def show_all_in_table(table):
    c.execute("SELECT rowid, * FROM {}".format(table))
    print(table + ": ")
    print("ID\tUsername Category\t\tLanguage  Age\tProfession\t\t\t\t\t\t\t\tPurpose\t\t\tComment")
    items = (c.fetchall())
    for item in items:
        print(item)


### Column "registered" in user_general
# Flag '1' to the column "registered"
def flag_registered(username):
    with conn:
        c.execute("UPDATE user_general SET registered = 1 WHERE username=:username", {'username': username})


# Check if the use already exists in a subject table
def if_registered(username):
    c.execute("SELECT registered FROM user_general WHERE username=:username", {'username': username})
    return c.fetchone()[0] == 1


### Getting data
# Get a certain user's info by username
def get_matching_user_by_name(username):
    c.execute("SELECT rowid, * FROM user_general WHERE username=:username", {'username': username})
    print(c.fetchone())


# Get the subject of the given user by username
def get_subject(username):
    c.execute("SELECT subject FROM user_general WHERE username=:username", {'username': username})
    # print(c.fetchone())
    # print(type(c.fetchone()))   # tuple
    print(c.fetchone()[0])


# Get a certain user's rowID by username in integer
def get_id_by_name(username):
    c.execute("SELECT rowid, * FROM user_general WHERE username=:username", {'username': username})
    print(int(c.fetchone()[0]))
    # print(type(c.fetchone()[0]))


# # Get all the usernames in TABLE user_general
# def get_username():
#     c.execute("SELECT username FROM user_general")
#     print(c.fetchall())
#
# # Get all IDs and usernames in TABLE user_general
# def get_id_username():
#     c.execute("SELECT rowid, username FROM user_general")
#     print(c.fetchall())


### Find matches according to user's preference
def find_match(pref):
    subject, categ, lang, minage, maxage, pro, purpose = pref

    # Get all the users that matches all the conditions from the given table
    def perfect_match():
        c.execute("SELECT username, comment FROM {} WHERE category=? AND language=? AND "
                  "age >= ? AND age <= ? AND profession = ? AND purpose = ?".format(subject),
                  [categ, lang, minage, maxage, pro, purpose])
        items = (c.fetchall())
        for item in items:
            print(item)

    # Get all the users that matches most conditions from the given table
    def partial_match():
        c.execute("SELECT username, comment FROM {} WHERE category=? AND language=? AND "
                  "age >= ? AND age <= ? AND profession = ? OR purpose = ?".format(subject),
                  [categ, lang, minage - 5, maxage + 5, pro, purpose])
        items = (c.fetchall())
        for item in items:
            print(item)

    perfect_match()
    partial_match()


### Delete data in a table or the entire table
# Delete a user by id
def delete_from_id(id):
    with conn:
        c.execute("DELETE from user_general WHERE rowid = (?)", (id,))


# Delete a given user from the given table
def delete_one(table, username):
    with conn:
        c.execute("DELETE FROM {} WHERE username = :username".format(table),
                  {'username': username, })


# Clear the content of Table user_general (but keep the table itself)
def delete_table(table):
    with conn:
        c.execute("DELETE FROM {}".format(table))


# SQLite allows you to drop only one table at a time
def drop_table(table):
    with conn:
        c.execute("DROP TABLE IF EXISTS {}".format(table))

# # Look up using LIKE
# def email_lookup(email):
#     with conn:
#         c.execute("SELECT * from user_general WHERE email LIKE (?)", ('%' + email,))
#         items = c.fetchall()
#         for item in items:
#             print(item)
