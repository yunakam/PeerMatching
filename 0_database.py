import sqlite3
import matching

conn = sqlite3.connect('matching_user.db')
# conn = sqlite3.connect(':memory:')
c = conn.cursor()

# Create an table "user_general" with columns: pwd(name) / username(name) / subject
c.execute("""CREATE TABLE IF NOT EXISTS user_general (
            username text,
            pwd text,
            subject text,
            registered integer
            )""")

# Create an table for each subject with columns: username / category / subcategory...
c.execute("""CREATE TABLE IF NOT EXISTS Language (
            username text,
            category text,
            subcategory integer,
            language text,
            age integer,
            profession text,
            purpose text,
            comment text              
            )""")

c.execute("""CREATE TABLE IF NOT EXISTS Maths (
            username text,
            category text,
            subcategory integer,
            language text,
            age integer,
            profession text,
            purpose text,
            comment text              
            )""")

c.execute("""CREATE TABLE IF NOT EXISTS Computing (
            username text,
            category text,
            subcategory integer,
            language text,
            age integer,
            profession text,
            purpose text,
            comment text             
            )""")

c.execute("""CREATE TABLE IF NOT EXISTS Humanities (
            username text,
            category text,
            subcategory integer,
            language text,
            age integer,
            profession text,
            purpose text,
            comment text            
            )""")

c.execute("""CREATE TABLE IF NOT EXISTS Business (
            username text,
            category text,
            subcategory integer,
            language text,
            age integer,
            profession text,
            purpose text,
            comment text             
            )""")


matching.show_all()
# matching.delete_from_id(7)
# matching.get_subject("yuri")
# matching.delete_table("Language")
# matching.delete_table("Computing")
# matching.delete_table("Humanities")
# matching.drop_table("Language")
# matching.drop_table("Computing")
# matching.drop_table("Maths")
# matching.drop_table("Humanities")
# matching.drop_table("Business")

matching.show_all_in_table("Language")
matching.show_all_in_table("Computing")
matching.show_all_in_table("Humanities")
# matching.get_matching_user_by_name("emi")
# matching.get_id_by_name("emi")
# matching.show_username()
# matching.show_id_username()
# matching.show_rowID()
# matching.show_all_business()

# matching.drop_table("Computing")

matching.if_registered("yuri")

