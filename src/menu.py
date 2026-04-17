from helper import *
from CSV_Management import *
from Primary_Classes import *
from graphs import *
import sys

def main():#Define the main function, which will be the main menu of the program
    print("Welcome to the Y. T. A. T. Finance Tracker! ")#Give a short welcome to the user
    savings, incomes, expenses, budget = csv_to_dictionary()#Get the information from the CSV files, and put it in a budget object
    user = classetup(incomes, savings, expenses, budget)
    
    while True:#Start the main menu loop
        check = choice_input(["1", "2", "3", "4", "5", "6", "7"], "Would you like to: \n1. View your entries \n2. Add an entry \n3. Delete an entry\n4. View statistics \n5. Change your currency\n6. View Totals \n7. Log out \n> ")#Give the user a choice of what they would like to do
        #Call the respective function based on the user's choice
            #Try and except blocks are used to catch any errors that may occur, and print them to the user instead of crashing the program
        if check == "1":
            try:
                user.view_entries()
            except Exception as e:
                pass
        elif check == "2":
            try:
                user.additem()
            except Exception as e:
                pass
        elif check == "3":
            try:
                user.removeitem()
            except Exception as e:
                pass
        elif check == "4":
            choice = choice_input(["1", "2"], "Would you like to \n1. View a bar chart \n2. View a pie chart \n> ")#Let the user choose what type of graph they would like to see
            #Give the user the graph based on their choice
            if choice == "1":
                try:
                    bargraph(user.categories, user.expenses)
                except Exception as e:
                    pass
            elif choice == "2":
                try:
                    piegraph(user.categories, user.expenses)
                except Exception as e:
                    pass
        elif check == "5":
            try:
                entry = user.selectentry()
                entry.currchange()
            except Exception as e:
                pass
        elif check == "6":
            try:
                print("\n\nView Totals:\n1.Incomes\n2.Expenses\n3. All")
                choice = inputchecker(3)

                if choice == 1:
                    print(user.viewincomes())
                elif choice == 2:
                    print(user.viewexpenses())
                elif choice == 3:
                    print(user.viewall())

            except Exception as e:
                pass
        else:
            break
        try:
            dict_to_csv(user)#Save the information to the CSV files after every change
        except Exception as e:
            pass
    try:
        sys.exit()#Close the program when the user logs out
    except Exception as e:
        pass
