#MW_CP2 classes
import csv
from helper import choiceInput, floatInput

##Class Budget: (aggregate with currency, income, expenses, savings)
class Budget:
#init there will 
    ###explanation: this class is an aggregate class, that holds all possible currencies the player can use, as well as all of their budgeting choices. (this includes income, savings, and expenses)
	#1: income
	#2: expenses
	#3: Savings
	#4: current currency
    def __init__(self):
        self.income = {}
        self.expenses = {"example" : Expense("pets_food", 50, "USD", "pets")}
        self.savings = {"example" : Saving("cat", 100, 'USD','pets', 20), "example2" : Saving("dog", 1000, 'USD','pets', 80)}
        self.current_currencies = {"U.S. Dollar" : Currency("US-Dollar", "USD", 1,1), "British Pound" : Currency("British Pound", "GBP",1.32, .75)}

	#addItem(self)
    def addItem(self):
		#Type = enter item
        type = choiceInput(['income', 'expense', 'saving'], "\nChoose\n\tIf you made money, and would like to add a new income, type 'income'\n\tIf you spent money, and would like to add a new expense, type 'expense'\n\tIf you have a new savings goal, and would like to add one of them, type 'saving'")
		#Name = enter item
        name = input
        #Amount = enter amount
		#Currency = enter currency
		#If type == ‘income’:
			#Self.income[name] = income(name, amount, currency)
		#elIf type == ‘expenses’:
			#Self.expenses[name] =expenses(name, amount, currency)
		#elIf type == ‘savings’:
			#Amount paid = “How much have you paid off for this item?”
			#Self.savings[name] =saving(name, amount, currency, amount paid off)
	#remove item(self)
		#what type is this?
		#while true show all of type, ask what they would like to remove
		#remove item from self.type

	#convertCurrency(self)
	

		

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

    def convert(self, new_currency):
        try:
            with open('docs/currency.csv', 'r') as currency_csv:
                

	

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
        if
        return f"{self.name} : Goal : {self.amount} | Amount Saved : {self.amount_saved} | Amount left to save : {self.amount_left} "
# f“Saving: You have saved {self.amount_saved} for Your goal,{self.name}, to raise {self.amount}” 
