import sys

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

mainmenu()
