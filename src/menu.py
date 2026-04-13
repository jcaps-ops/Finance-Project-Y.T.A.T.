from helper import *
from b_functions import *
from j_functions import *
import os

def main():
    print("Welcome to the Y. T. A. T. Finance Tracker! ")
    accounts = csv_to_dict("docs/accounts.csv")
    while True:
        check = choice_input(["1", "2", "3"], "Would you like to: \n1. Sign up\n2. Log in\n3. Exit\n> ")
        if check == "1":
            name = user_creator("docs/accounts.csv")
        elif check == "2":
            name = user_sign_in("docs/accounts.csv")
        elif check == "3":
            break
        path = f"docs/{name}.csv"
        if not os.path.exists(path):
            with open(path, mode = 'w') as file:
                writer = csv.writer(file)
                writer.writerow(["name", "amount", "currency", "category"])
                writer.writerow([{}, {}, {}, {}])
        try:
            user = csv_to_dictionary(path)
        except:
            user = Budget()
        while True:
            check = choice_input(["1", "2", "3", "4", "5", "6"], "Would you like to: \n1. View your entries \n2. Add an entry \n3. Delete an entry\n4. View statistics \n5. Change your currency \n6. Log out \n> ")
            if check == "1":
                user.view_entries()
            elif check == "2":
                user.additem()
            elif check == "3":
                user.removeitem()
            elif check == "4":
                choice = choice_input(["1", "2"], "Would you like to \n1. View a bar chart \n2. View a pie chart \n> ")
                if choice == "1":
                    bargraph(user.categories, user.expenses)
                elif choice == "2":
                    piegraph(user.categories, user.expenses)
            elif check == "5":
                user.currchange()
            else:
                break
