import sqlite3
import matching

conn = sqlite3.connect('matching_user.db')
# conn = sqlite3.connect(':memory:')
c = conn.cursor()


matching.show_all()
# matching.delete_from_id(ID)
# matching.get_subject("USERNAME")
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
# matching.get_matching_user_by_name("USERNAME")
# matching.get_id_by_name("USERNAME")
# matching.show_username()
# matching.show_id_username()
# matching.show_rowID()
# matching.show_all_business()

# matching.if_registered("USERNAME")

