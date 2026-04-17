import csv

#For changing CSV files to lists of dictionaries. 
def csv_to_dict(path):
    try:#Attempted to 
        with open(path, mode = 'r') as file:#Open the file
            reader = csv.reader(file)
            header = next(reader)
            finished = []
            for line in reader:
                i = 0
                current_line = {}
                for column in header:
                    if "[" in line[i] and "]" in line[i]: line[i] = strlistconvert(line[i])
                    if "{" in line[i] and "}" in line[i]: line[i] = strlistconvert(listdictconvert(line[i]))
                    current_line[column] = line[i]
                    if line[i].isdigit(): current_line[column] = int(line[i])
                    i += 1
                finished.append(current_line)#And get all the info in it
    except FileNotFoundError: print("The file was not found. ")
    except Exception as e: print(f"You had a(n) {e} error. ")
    else: return finished
    return []

#For saving lists with dictionaries to CSV files. 
def save_csv(path, data):
    try:# attempt to 
        if not data: return
        with open(path, mode="w", newline="") as file:#open the file
            cleaned_data = []
            for row in data:
                new_row = {}
                for key, value in row.items():
                    if isinstance(value, (list, dict)): new_row[key] = str(value)
                    else: new_row[key] = value
                cleaned_data.append(new_row)
            header = cleaned_data[0].keys()
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writeheader()# and write it into the csv
            writer.writerows(cleaned_data)
    except FileNotFoundError: print("The file was not found. ")
    except Exception as e: print(f"You had a(n) {e} error. ")

#Used to convert a string to a list, mostly for CSV files. 
def strlistconvert(string):
    string = string.strip("[]")  # remove brackets
    if not string:
        return []
    strlist = []
    temp = ""
    for char in string:
        if char != ",":
            temp += char
        else:
            strlist.append(int(temp.strip()))
            temp = ""
    if temp:
        strlist.append(int(temp.strip()))
    return strlist

#Same thing as strlistconvert, but for dictionaries.
def listdictconvert(listitem):
    dictversion = {}
    for item in listitem:
        keypair = item.split(":")
        dictversion[keypair[0]] = keypair[1]
    return dictversion

def csv_to_dictionary():
    #Get all the information from the CSV files
    savings = csv_to_dict("docs/savings.csv")
    incomes = csv_to_dict("docs/income.csv")
    expenses = csv_to_dict("docs/expenses.csv")
    budget = csv_to_dict("docs/budget.csv")
    #Change all of the information into the correct format (Put it in a dictionary, with the name as the key and the rest of the imformation as an object as the value)
    return savings, incomes, expenses, budget

def dict_to_csv(budget):#Save it to the respective CSV files
    save_csv("docs/income.csv", budget.incomes)#Saving the information to the income file
    save_csv("docs/savings.csv", budget.savings)#Saving the information to the savings file
    save_csv("docs/expenses.csv", budget.expenses)#Saving the information to the expenses file
    save_csv("docs/budget.csv", budget.budgets)#Saving the information to the budget file