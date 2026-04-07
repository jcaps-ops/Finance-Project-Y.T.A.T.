
#explanation: used by other input functions
def userInput(prompt = '> '):
    return input(prompt).lower().strip()


#explanation: allows user to input a number of their choice, you can set the max and min, the number they type will have to be between those [the max and min are INCLUDED!]
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
            print('\nInput is out of range!')


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

#explanation: choice input allows tyou to select a choice. choices should be equal to a list... IE: bats = choiceInput(['big','small','medium'], "What size bat would you like?") the user will then be asked what bat they like till they enter one of the things in that list
def choiceInput(choices,prompt = '> '):
    while True:
        choice = userInput(prompt)
        if choice in choices:
            return choice
        else:
            print('\nPlease select a valid choice!')
import random as rand
import csv

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

def choice_input(choices, prompt = ">"):
    while True:
        choice = input(prompt)
        if choice in choices:
            return choice
        elif choice in ["idk", "i don't know", "i dont know"]:
            return rand.choice(choices)
        else:
            print("That was an invalid input. Please try again. ")

def int_input(prompt = ">"):
    while True:
        choice = input(prompt).lower().strip()
        if choice.isdigit():
            return int(choice)
        elif choice in ["idk", "i don't know", "i dont know"]:
            return rand.randint(0, 10000000)
        print("That was an invalid input. Please try again. ")

def txt_reader(path):
    try:
        with open(path) as file:
            return file.read()
    except FileNotFoundError:
        print("The file was not found. ")
    except Exception as e:
        print(f"You had an {e}. ")
        return ""

def txt_saver(path, content):
    try:
        with open(path, "w") as document:
            document.write(content)
    except FileNotFoundError:
        print("The file was not found. ")
    except Exception as e:
        print(f"You had an {e}. ")

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

def listdictconvert(listitem):
    dictversion = {}
    for item in listitem:
        keypair = item.split(":")
        dictversion[keypair[0]] = keypair[1]
    return dictversion

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
