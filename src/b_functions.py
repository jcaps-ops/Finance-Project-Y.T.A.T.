from helper import *
from F_M_functions import *

def csv_to_dictionary():
    savings_dict, income_dict, expenses_dict, budget_dict = {}, {}, {}, {}#Create the dictionaries
    #Get all the information from the CSV files
    savings = csv_to_dict("docs/savings.csv")
    incomes = csv_to_dict("docs/income.csv")
    currencies = csv_to_dict("docs/currency.csv")
    expenses = csv_to_dict("docs/expenses.csv")
    budget = csv_to_dict("docs/budget.csv")
    #Change all of the information into the correct format (Put it in a dictionary, with the name as the key and the rest of the imformation as an object as the value)
    for i in incomes:
        income_dict[i["name"]] = (Income(amount=i["amount"], category=i["category"], date=i["date"], currency=i["currency"], name=i["name"]))
    for i in savings:
        savings_dict[i["name"]] = (Saving(amount=i["amount"], amount_saved=i["amount_saved"], name=i["name"], currency=i["currency"], category=i["category"], date=i["date"]))
    for i in expenses:
        expenses_dict[i["name"]] = (Expense(amount=i["amount"], category=i["category"], date=i["date"], currency=i["currency"], name=i["name"]))
    for i in budget:
        budget_dict[i["name"]] = (BudgetEntry(amount=i["amount"], category=i["category"], date=i["date"], currency=i["currency"], name=i["name"]))
    return Budget(savings=savings_dict, income=income_dict, expenses=expenses_dict, budgets=budget_dict, current_currencies=currencies)#Return the information that we got from the CSV files in a budget object, which will be used in the program

def dict_to_csv(budget):#Save it to the respective CSV files
    save_csv("docs/income.csv", budget.incomes)#Saving the information to the income file
    save_csv("docs/savings.csv", budget.savings)#Saving the information to the savings file
    save_csv("docs/expenses.csv", budget.expenses)#Saving the information to the expenses file
    save_csv("docs/budget.csv", budget.budgets)#Saving the information to the budget file