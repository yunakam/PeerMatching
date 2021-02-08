# PeerMatching

*This is going to be the assignment for Digital Expertise.*

------------------------------------

## **Overview**

It is an educational program that finds a matching user to learn with (peer learner) according to the registered info and preferences of users.

#### Procedure
The file with a number at the beginning stores the code snippet for each stage.

1. `1_mainmenu.py` User is asked whether to sign up for the first time or log in if already signed up

1. `2_signup.py` User signs up with username, password, and the subject they want to learn. Create a table `user_general` to store data.
    username | pwd | subject | registered
    -------- | --- | ------- | ------------
    yuri | yurispwd | Language | 0 *(default value)*
    fabi | fabispwd | Language | 0
    dani | danispwd | Computing | 0

1. `3_login.py` User logs in with username & password

1. `4_register.py` Once login is successful and if not registered yet, they will be asked for some more info about themselves:
    * a category of the subject (e.g., category "French" for subject "Language")
    * language to use in the program
    * age
    * profession
    * purpose of learning (how serious you are)
    * comment
    
   These information will be stored in the table of each subject.
   #### e.g. Language
    username | category | subcategory | language | age ...
    -------- | -------- | ----------- | -------- | ---
    yuri | French | None | English | 34
    fabi | English | French | 50
    
   The column `registered` in the table `user_general` flags 1.
  
1. `5_register.py` If user wants, they enter some conditions for possible peer learners. Matches will be displayed with their username and profile comment

------------------------------------

## Requirements

* No external modules required
* Run `set_up.py` in order to create tables anew


--- end of README.md ---
