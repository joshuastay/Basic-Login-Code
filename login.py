import re


class LoginCredentials:
    """
    Simple login authentication program
    includes a method to create a new user
    stores values in a dictionary
    """

    def __init__(self):
        self.login_dict = dict()
        self.status = 1

    # method to check if the password meets parameters
    def check_pass(self, entry):
        check_upper = False
        check_lower = False
        check_length = False
        check_int = False
        check_spec = False
        for each in entry:
            if each.islower() is True:
                check_lower = True
            else:
                continue
        for each in entry:
            if each.isupper() is True:
                check_upper = True
            else:
                continue
        if re.search("\d", entry):
            check_int = True
        if len(entry) >= 8 and len(entry) <= 20:
            check_length = True
        if re.search("[!, @, #, $, %]", entry):
            check_spec = True
        if check_spec and check_length and check_int and check_upper and check_lower:
            return True
        else:
            return False

    # new_login prompts user for a new username and password and stores values in the dictionary
    def new_login(self):
        make_user = True
        make_pass = True
        while make_user is True:
            print("Enter a new username (limit 25 characters, no spaces) ")
            username = input("Username: ")
            if len(username) > 25 or username.count(" ") > 0:
                print("Invalid Username!")
                continue
            elif username in self.login_dict.keys():
                print('Username in use!')
                continue
            make_user = False
        while make_pass is True:
            print("Enter a new password (atleast 8 characters, limit 20. Must include lowercase, uppercase, numbers and"
                  " a special character !, @, #, $, %")
            password = input("Enter new password: ")
            passvalid = self.check_pass(password)
            if passvalid:
                self.login_dict[username] = password
                break
            else:
                print("Password Invalid!")
                continue

    # login method checks the dictionary for a matching username and password
    def login(self):
        username = input("Username: ")
        if self.login_dict.get(username) is not None:
            attempts = 3
            while attempts > 0:
                password = input("Password: ")
                if self.login_dict[username] == password:
                    print("Login Successful!")
                    break
                else:
                    attempts -= 1
                    print("Login Failed! attempts remaining: ", attempts)
        else:
            print("Unrecognized Username!")
