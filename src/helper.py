import random as rand
import csv

#explanation: used by other input functions
def userInput(prompt = '> '):
    return input(prompt).lower().strip()

#We do not use this. I don't want to delete it, as it is not mine, but we already have another one of these functions that does the same thing, and this one is not used anywhere in the program. 
"""#explanation: allows user to input a number of their choice, you can set the max and min, the number they type will have to be between those [the max and min are INCLUDED!]
def intInput(max = 100000,prompt='> ',min = 0):
    while True:
        num = userInput(prompt)
        try:
            num = int(num)
        except:
            print('\nInput is not a number!')
            continue
        if num <= max and num >= min:
            return num
        else:
            print('\nInput is out of range!')"""


#Explanation: same as int input but with a float!
def floatInput(max = 100000.00,prompt='> ',min = 0.00):
    while True:
        num = userInput(prompt)
        try:
            num = float(num)
        except:
            print('\nInput is not a number!')
            continue
        if num <= max and num >= min:
            return num
        else:
            print('\nInput is out of range!')

#We do not use this. I don't want to delete it, as it is not mine, but we already have another one of these functions that does the same thing, and this one is not used anywhere in the program. 
"""#explanation: choice input allows tyou to select a choice. choices should be equal to a list... IE: bats = choiceInput(['big','small','medium'], "What size bat would you like?") the user will then be asked what bat they like till they enter one of the things in that list
def choiceInput(choices,prompt = '> '):
    while True:
        choice = userInput(prompt)
        if choice in choices:
            return choice
        else:
            print('\nPlease select a valid choice!')"""

#Foe changing CSV files to lists of dictionaries. 
def csv_to_dict(path):
    try:
        with open(path, mode = 'r') as file:
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
                finished.append(current_line)
    except FileNotFoundError: print("The file was not found. ")
    except Exception as e: print(f"You had a(n) {e} error. ")
    else: return finished
    return []

#For saving lists with dictionaries to CSV files. 
def save_csv(path, data):
    try:
        if not data: return
        with open(path, mode="w", newline="") as file:
            cleaned_data = []
            for row in data:
                new_row = {}
                for key, value in row.items():
                    if isinstance(value, (list, dict)): new_row[key] = str(value)
                    else: new_row[key] = value
                cleaned_data.append(new_row)
            header = cleaned_data[0].keys()
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writeheader()
            writer.writerows(cleaned_data)
    except FileNotFoundError: print("The file was not found. ")
    except Exception as e: print(f"You had a(n) {e} error. ")

#The same exact function as choiceInput, but it is being used, as opposed to its opposite. 
def choice_input(choices, prompt = ">"):
    while True:
        choice = input(prompt)
        if choice in choices:
            return choice
        elif choice in ["idk", "i don't know", "i dont know"]:
            return rand.choice(choices)
        else:
            print("That was an invalid input. Please try again. ")

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

#A variant of the int input function, but it has a simpler system doesn't need to take in a min. 
def inputchecker(rangeofchoices):
    while True:
            choicevar = input(f"Which one would you like to choose?(1~{rangeofchoices}):\n")
            try:
                choicevar = int(choicevar)
                if choicevar in range(1, rangeofchoices+1):
                    break
                else:
                    print("That's not an option :(")
                    continue
            except:
                    continue
           
    return choicevar

#Another variant of the int input function, but it takes in any number, and it doesn't have a max or min. 
def gummysint(usernum):
    while True:
        if usernum.isdigit():
            return int(usernum)
        else:
            usernum = input("Please enter a valid number:\n")