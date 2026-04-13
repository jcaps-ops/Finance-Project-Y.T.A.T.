from helper import *
from F_M_functions import *
import bcrypt # pyright: ignore[reportMissingImports]
import pandas as pd # pyright: ignore[reportMissingModuleSource, ModuleNotFoundError]

def csv_to_dictionary(path):
    dictionary = csv_to_dict(path)
    return Budget(dictionary[0], dictionary[1], dictionary[2], dictionary[3])

def dict_to_csv(budget, path):
    df = pd.DataFrame({"income": budget.income, "expenses": budget.expenses, "savings": budget.savings, "currency": budget.current_currencies})
    df.to_csv(path, sheet_name="", index=False)

def pass_encoder(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def pass_checker(password, hashed):
    return bcrypt.checkpw(password.encode(), hashed.encode())

def password():
    passwords = ["1234", "password", "qwerty", "123456", "123456789", "123467890", "0987654321", "111111", "p@ssw0rd", "123123", "p@$$w0rd", "5678", "abcdefghijklmnopqrstuvwxyz", "aBcDeFgHiJkLmNoPqRsTuVwXyZ", "AbCdEfGhIjKlMnOpQrStUvWxYz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "qwertyuiop", "asdfghjkl", "asdfghjkl;'", "zxcvbnm,./", "/.,mnbvcxz", "';lkjhgfdsa", "lkjhgfdsa", "poiuytrewq"]
    #loop
    while True:
        #reset the strength to 0
        strength = 0
        #reset all the variables to false
        up = False
        low = False
        num = False
        #Ask the user for the password
        password = input("Please write your prospective password.\n> \033[34m ")
        print('\033[0m')
        #if it is longer than 7 letters
        if len(password) > 7:
            #add 1 to the password strength
            strength += 1
        #otherwise
        else:
            #say that they need to make their password longer
            print("You need to make your password longer. ")
        #looping through every single letter
        for letter in password:
            #check if that letter is uppercase
            if letter.isupper():
                #make it so that the information that it is uppercase is true
                up = True
            #if it is true
        if up:
                #add 1 to the password strength
            strength += 1
            #otherwise
        else:
                #say that they have to add an uppercase letter
            print("You need to add an uppercase letter. ")
        #looping through every single letter
        for letter in password:
        #check if that letter is lowercase
            if letter.islower():
                #make it so that the information that it is lowercase is true
                low = True
        #if it is true
        if low:
            #add 1 to the password strength
            strength += 1
        #otherwise
        else:
            #say that they have to add an lowercase letter
            print("You need to add a lowercase letter. ")
        #check if the string is not alpha numeric (isalnum)
        if not password.isalnum() and password:
            #add 1 to the password strength
            strength += 1
        #otherwise
        else:
            #say that they need to add a special character
            print("You need to add a special character. ")
        #looping through every single letter
        for letter in password:
            #check if that letter is numeric
            if letter.isdigit():
                #if it is, make it so that the information that there is a number is true
                num = True
        #if it is true
        if num:
            #add 1 to the password strength
            strength += 1
        #otherwise
        else:
            #say that they have to add an number
            print("You need to add a number. ")
        #display the password strength
        print(f"Your password strength is {strength}/5. ")
        if strength == 5:
            print("That is very strong. Good job! ")
        elif strength == 4:
            print("This is strong but you can do better. ")
        elif strength == 3:
            print("Your password is moderate. You have room to improve. ")
        elif strength == 1 or strength == 2:
            print("Your password is weak. Do better. ")
        elif strength == 0:
            print("You and your password are a failure. ")
        else:
            print("You found the easter egg! Don't use it again. ")
        if password in passwords:
            print("That is so boring and typical. Why did you choose this password? Get more creative. I don't really like that you did this. ")
        check = choice_input(['yes','y','no','n'],"Are you satisfied with your password? ")
        if check in ["yes",'y']:
            return password

def user_creator(path):
    try:
        dictionary = csv_to_dictionary(path)
    except:
        dictionary = []

    while True:
        created = False
        name = input("What will your username be? ")
        if dictionary:
            for i in dictionary:
                if name == i["username"]:
                    created = True
        else:
            created = False
        if created == False:
            break
        print("That username is already being used. ")
    user_password = password()
    user_password = pass_encoder(user_password)
    dictionary.append({'username': name, 'password': user_password, 'logged in': 'True'})
    save_csv(dictionary, path)
    return name

def user_sign_in(path):
    dictionary = csv_to_dictionary(path)
    while True:
        username = input("Enter Username: ")
        for i in dictionary:
            if i["username"] == username:
                save_csv(dictionary, path)
                check = False
                while not check:
                    password = input("Enter Password: \033[34m")
                    print('\033[0m')
                    check = pass_checker(password, i["password"])
                return username
