import sqlite3, matching, categ_list

conn = sqlite3.connect('matching_user.db')
# conn = sqlite3.connect(':memory:')
c = conn.cursor()

# Variables derived from register()
username = "emi"
subject = "Humanities"
category = "English"
language = "English"


def search():
    """
    1. Ask user for conditions of a desired peer
        mandatory: category, language <-- wont be asked
        accept mismatch: age, profession, purpose
    2. Retrieve users from the same table who have match:
        [A] all the conditions
        [B] all the conditions except for one
    3. Show [A] followed by [B] with username, profession, and comment
    """

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

    print("\nMy preferences:")
    print(
        f"Subject: {subject} >> Category: {category},\nLanguage: {language},\n"
        f"Age range: {cond_minage}-{cond_maxage},\nProfession: {cond_pro},\nPurpose: {cond_purpose}\n")

    print("Send a message to your peer!")
    # Show perfect matches followed by partial matches
    preference = (subject, category, language, cond_minage, cond_maxage, cond_pro, cond_purpose)
    matching.find_match(preference)


search()
