'''
Basic login script, lets you create a username and password, and test the login
'''

import re
logindict = dict()
status = 1

# this function checks the parameters of the password
# if all are true it returns True
def checkpass(entry):
    checkupper = False
    checklower = False
    checklen = False
    checkint = False
    checkspec = False
    for each in entry:
        if each.islower() is True:
            checklower = True
        else:
            continue
    for each in entry:
        if each.isupper() is True:
            checkupper = True
        else:
            continue
    if re.search("\d", entry):
        checkint = True
    if len(entry) >= 8 and len(entry) <= 20:
        checklen = True
    if re.search("[!, @, #, $, %]", entry):
        checkspec = True
    if checkspec and checklen and checkint and checkupper and checklower:
        return True
    else:
        return False

# this function is used to create a new username and password
# user is held in loop until parameters of username and password are met
def newlogin():
    makeuser = True
    makepass = True
    while makeuser is True:
        print("Enter a new username (limit 25 characters, no spaces) ")
        username = input("Username: ")
        if len(username) > 25 or username.count(" ") > 0:
            print("Invalid Username!")
            continue
        makeuser = False
    while makepass is True:
        print("Enter a new password (atleast 8 characters, limit 20. Must include lowercase, uppercase, numbers and"
              " a special character !, @, #, $, %")
        password = input("Enter new password: ")
        passvalid = checkpass(password)
        if passvalid:
            logindict[username] = password
            break
        else:
            print("Password Invalid!")
            continue

# this function validates credentials, it checks the dictionary for a username then checks the password for a match
# it gives the user 3 attempts to log in
def login():
    username = input("Username: ")
    if logindict.get(username) is not None:
        attempts = 3
        while attempts > 0:
            password = input("Password: ")
            if logindict[username] == password:
                print("Login Successful!")
                break
            else:
                attempts -= 1
                print("Login Failed! attempts remaining: " , attempts)
    else:
        print("Unrecognized Username!")

# main line of code calling for a command to either login, make a new login or end the program
# matches the command with the desired function
while status > 0:
    command = input("New, Login or Done?: ")

    if command == "New":
        newlogin()
        continue

    elif command == "Login":
        login()
        continue

    elif command == "Done":
        break

    else:
        print("Invalid Command!")

