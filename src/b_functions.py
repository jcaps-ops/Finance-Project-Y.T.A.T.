from helper import *
from F_M_functions import *

def csv_to_dictionary():
    savings_list, income_list, expenses_list, budget_list = [], [], [], []#Create the lists
    savings = csv_to_dict("docs/saving.csv")#Get all the information
    income = csv_to_dict("docs/income.csv")
    currencies = csv_to_dict("docs/currency.csv")
    expenses = csv_to_dict("docs/expenses.csv")
    budget = csv_to_dict("docs/budget.csv")
    for i in income:#Change all of the information into the correct format
        income_list.append(Income(amount=i["amount"], category=i["category"], date=i["date"], currency=i["currency"], name=i["name"]))
    for i in savings:
        savings_list.append(Saving(amount=i["amount"], amount_saved=i["amount_saved"], name=i["name"], currency=i["currency"], category=i["category"], date=i["date"]))
    for i in expenses:
        expenses_list.append(Expense(amount=i["amount"], category=i["category"], date=i["date"], currency=i["currency"], name=i["name"]))
    for i in budget:
        budget_list.append(BudgetEntry(amount=i["amount"], category=i["category"], date=i["date"], currency=i["currency"], name=i["name"]))
    return Budget(savings=savings_list, income=income_list, expenses=expenses_list, budgets=budget_list, current_currencies=currencies)#Return the information

def dict_to_csv(budget):#Save it. 
    save_csv("docs/income.csv", budget.income)
    save_csv("docs/savings.csv", budget.savings)
    save_csv("docs/expenses.csv", budget.expenses)
