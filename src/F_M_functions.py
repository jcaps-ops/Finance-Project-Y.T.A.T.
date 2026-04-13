#MW_CP2 classes
import pandas as pd
from helper import *
import datetime

##Class Budget: (aggregate with currency, income, expenses, savings)
class Budget:
#init there will 
    ###explanation: this class is an aggregate class, that holds all possible currencies the player can use, as well as all of their budgeting choices. (this includes income, savings, and expenses)
	#1: income
	#2: expenses
	#3: Savings
	#4: current currency
    def __init__(self):
        self.incomes = {}
        self.expenses = {}
        self.savings = {}

	#addItem(self)
    def additem(self):
        print("Is this an:\n1. Income\n2. Saving\n3. Expense")
        choice = inputchecker(3)
        match choice:
            case 1:
                entrytype = "income"
            case 2:
                entrytype = "saving"
            case 3: 
                entrytype = "expense"

        itemname = input("What is the name of this item:\n")
        print("1. USD\n2. IRR\n3. EUR\n4. JPY\n5. GBP\n6. CHF\n7. CAD\n8. AUD\n9. SEK")
        curr = inputchecker(9)

        match curr:
            case 1:
                currency = "USD"
            case 2:
                currency = "IRR"
            case 3:
                currency = "EUR"
            case 4:
                currency = "JPY"
            case 5:
                currency = "GBP"
            case 6:
                currency = "CHF"
            case 7:
                currency = "CAD"
            case 8:
                currency = "AUD"
            case 9:
                currency = "SEK"

        itemscost = input("How much money was this item (in the currency you inputted earlier)? (if it's an expense, put a negative number):\n")
        itemscost = gummysint(itemscost)

        category = input("What is the category (ex: transport, entertainment, etc) of this item?:\n")

        if entrytype == "saving":
            saveamount = input("How much do you need to save?\n")
            saveamount = gummysint(saveamount)
        
        todaysday = datetime.datetime.now()

        if entrytype == "income":
            self.incomes[itemname] = Income(itemname, itemscost, currency, category, todaysday)
        elif entrytype == "saving":
            self.savings[itemname] = Saving(itemname, saveamount , currency, category, todaysday, itemscost)
        elif entrytype == "expense":
            self.expenses[itemname] = Expense(itemname, itemscost, currency, category, todaysday)
	
    def removeitem(self):
        print("Is this an:\n1. Income\n2. Saving\n3. Expense")
        choice = inputchecker(3)
        match choice:
            case 1:
                entrytype = "income"
            case 2:
                entrytype = "saving"
            case 3: 
                entrytype = "expense"

        itemname = input("What is the name of this item:\n")

        if entrytype == "income":
            self.incomes.pop(itemname)
        elif entrytype == "saving":
            self.savings.pop(itemname)
        elif entrytype == "expense":
            self.expenses.pop(itemname)
        else:
            print("That item likely does not exist :(")
    
    def view_entries(self):
        print("What kind of entry would you like to view?\n")
        print("1. Income\n2. Expenses\n3. Savings\n4. All Entries")

        choice = inputchecker(4)

        if choice == 1:
            incomeskeys = self.incomes.keys()
            for income in incomeskeys:
                print(self.incomes[income])
        elif choice == 2:
            expenses = self.expenses.keys()
            for expense in expenses:
                print(self.expenses[expense])
        elif choice == 3:
            savings = self.savings.keys()
            for saving in savings:
                print(self.savings[saving])
        elif choice == 4:
            entries = self.incomes.keys() + self.expenses.keys() + self.savings.keys()
            for entry in entries:
                print(self.entries[entry])
        else:
            print("Invalid choice. Please try again.")

		

#class MoneyItem: (parent of income, expenses, saving, composition of currency)
class MoneyItem:
    ###explanation: this is a parent class to expenses, income, and savings
        ###it will take in 4 amounts name, amount held, currency it is in, and category.
#init there will be a couple of pieces of information.
    #1: Name
	#2: Amount
	#3: Currency
    #4: category
    def __init__(self, name, amount, currency, category, date):
        self.name = name
        self.amount = amount
        self.currency = currency
        self.category = category
        self.date = date
    
    def currchange(self):
        print("What currency would you like to change to?\n1. USD\n2. IRR\n3. EUR\n4. JPY\n5. GBP\n6. CHF\n7. CAD\n8. AUD\n9. SEK")
        curr = inputchecker(9)

        match curr:
            case 1:
                currency = "USD"
            case 2:
                currency = "IRR"
            case 3:
                currency = "EUR"
            case 4:
                currency = "JPY"
            case 5:
                currency = "GBP"
            case 6:
                currency = "CHF"
            case 7:
                currency = "CAD"
            case 8:
                currency = "AUD"
            case 9:
                currency = "SEK"

        print("Is the entry an:\n1. Income\n2. Saving\n3. Expense")

        entrytype = inputchecker(3)

        match entrytype:
            case 1:
                entrytype = "income"
            case 2:
                entrytype = "saving"
            case 3: 
                entrytype = "expense"

        while True:
            entry = input("What is the name of the entry you want to change?(Enter 'EXIT' to go back)\n")

            entries = self.income.keys()+self.expense.keys()+self.saving.keys()

            if entry == "EXIT" or entry == "exit":
                return
            elif entry in entries:
                break
            else:
                print("Looks like that entry doesn't exist! Maybe you made a typo? Try again!")
        
        if entrytype == "income":
            self.income[entry].convert()
        elif entrytype == "saving":
            self.saving[entry].convert()
        elif entrytype == "expense":
            self.expense[entry].convert()

    def convert(self, new_currency):
        if self.currency != "USD":
            df = pd.read_csv("docs/currency.csv", skipinitialspace=True)
            rate = df.loc[df["currency"] == self.currency, "conversion to USD"].iat[0]
            self.amount *= rate
            print(df.loc[df["currency"] == self.currency, "conversion to USD"].iat[0])
            print(self.amount)
        
        df = pd.read_csv("docs/currency.csv", skipinitialspace=True)
        rate = df.loc[df["currency"] == new_currency, "conversion from USD"].iat[0]
        self.amount *= rate
        print(df.loc[df["currency"] == new_currency, "conversion from USD"].iat[0])
        print(self.amount)
        self.currency = new_currency


                

	

"""#class Currency: (aggregate of budget, child of money item)
class Currency: 
#init there will be the values name, conversion to USD, and the Conversion From USD
    def __init__(self, name, abreviation, conversion_to_USD, conversion_from_USD):
        self.name = name
        self.abreviation = abreviation
        self.conversion_to_USD = conversion_to_USD
        self.conversion_from_USD = conversion_from_USD

#def convert to usd(self, conversion_factor):
    def convertToUSD(self, conversion_factor):
	#Converted = Self.conversion to USD * conversion factor
        converted = self.conversion_to_USD * conversion_factor
	#return converted
        return converted

# def convert from usd(self, conversion_factor)
    def convertFromUSD(self, conversion_factor):
        #converted = self.conversion from USD *conversion_factor
        converted = self.conversion_from_USD * conversion_factor
    #return converted
        return converted"""


#class Income(MoneyItem):(aggregate of budget, child of money item)
class Income(MoneyItem):
#init will be the amount and name, use the super init function to get those.
#__str__:
    def __str__(self):
# f“Income: {self.name} made you {self.amount}” 
        return f"Income: {self.name} made you {self.amount}" 

#class Expense(MoneyItem)
class Expense(MoneyItem):
#init will be the amount and name, use the super init function to get those.
#__str__:
    def __str__(self):
# f“Expense: {self.name} cost you {self.amount}”
        return f"Expense: {self.name} cost you {self.amount}"


#class Saving(MoneyItem)(aggregate of budget, child of money item)
class Saving(MoneyItem):
#init will be the amount and name, use the super init function to get those, but this will have another variable called amount saved.
    def __init__(self, name, amount, currency, category, date, amount_saved):
        super().__init__(name, amount, currency, category, date)
        self.amount_saved = amount_saved
        self.amount_left = amount - amount_saved
        self.last_date_payed = ""

#pay:
    def pay(self):
        payment = floatInput(min=0.00, max = self.amount_left, prompt = f"\nEnter the amount you are paying, this should be a number from 0, to {self.amount_left}")
        self.amount_saved += payment
        self.amount_left -= payment
        print(self.__str__())
	#Self.amount_paid += amount_paid

#__str__: 
    def __str__(self):
        
        return f"{self.name} : Goal : {self.amount} | Amount Saved : {self.amount_saved} | Amount left to save : {self.amount_left} "
# f“Saving: You have saved {self.amount_saved} for Your goal,{self.name}, to raise {self.amount}” 
