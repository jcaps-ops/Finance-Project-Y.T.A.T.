#This will be the set up for the menu using the GUI
import tkinter as tk
from tkinter import *
from Functions_Edited_ForGUI import *
from helper import *
from b_functions import *
from j_functions import *
import os

root = tk.Tk()

root.title("FINANCE PROJECT")
root.configure(background="light grey")
root.minsize(900,300)
root.maxsize(1500,500)
root.geometry("1200x400+100+100")

name_var=tk.StringVar()
passw_var=tk.StringVar()
Entriescatagories=tk.StringVar()


#Here is the concept is to make pre loaded and planed areas where we will load with the diffrent labels and buttons
def submiting_password():
    #Replace this with the sign in system that checks it
    root.bools = 0
    name=name_var.get()
    password=passw_var.get()
    if name == "Test1":
        root.bools += 1
    if password == "Test2":
        root.bools += 1
    if root.bools == 2:
        Doc4()
    else:
        root.wrg_label = tk.Label(root, text = 'Incorrect password or username', font = ('calibre',10,'bold'))
        root.wrg_label.place(relx=0.5, rely=0.2, anchor="n")
def Doc4():
    #Clearing
    root.btn.place_forget()
    #Replacing
    root.wrg_label = tk.Label(root, text = 'Incorrect password or username', font = ('calibre',10,'bold'))
    root.wrg_label.place(relx=0.5, rely=0.2, anchor="n")
    root.vent = tk.Button(root, text="View your entries", command=root.user.view_entries())
    root.vent.place(relx=.35, rely=0.4, anchor="n")
    root.aent = tk.Button(root, text="Add an entry", command=root.user.additem())
    root.aent.place(relx=.45, rely=0.4, anchor="n")
    root.dent = tk.Button(root, text="Delete an entry", command=root.user.removeitem())
    root.dent.place(relx=.55, rely=0.4, anchor="n")
    root.sent = tk.Button(root, text="View a statistics", command=Doc8)
    root.sent.place(relx=.65, rely=0.4, anchor="n")
    root.cent = tk.Button(root, text="Change a currency", command=root.user.currchange())
    root.cent.place(relx=.65, rely=0.4, anchor="n")
    


def Doc8():
    root.vent.place_forget()
    root.aent.place_forget()
    root.dent.place_forget()
    root.sent.place_forget()

    root.barbin = tk.Button(root, text="Bar Graph", command=bargraph(root.user.categories, root.user.expenses))
    root.barbin.place(relx=.35, rely=0.4, anchor="n")
    root.piebin = tk.Button(root, text="Pie-chart graph", command=piegraph(root.user.categories, root.user.expenses))
    root.piebin.place(relx=.45, rely=0.4, anchor="n")
    root.Exitbin = tk.Button(root, text="Go back", command=fixstatistcs)
    root.Exitbin.place(relx=.55, rely=0.4, anchor="n")
def fixstatistcs():
    root.barbin.place_forget()
    root.piebin.place_forget()
    root.Exitbin.place_forget()
    Doc4()
def fixguiaddons():
    root.incomebin.place_forget()
    root.Savbin.place_forget()
    root.extbin.place_forget()
    root.expcesbin.place_forget()

    Doc4()
def Doc6():
    root.vent.place_forget()
    root.aent.place_forget()
    root.dent.place_forget()
    root.sent.place_forget()

    root.incomebin = tk.Button(root, text="Income saving")
    root.incomebin.place(relx=.35, rely=0.4, anchor="n")
    root.Savbin = tk.Button(root, text="Savings")
    root.Savbin.place(relx=.45, rely=0.4, anchor="n")
    root.expcesbin = tk.Button(root, text="Expences")
    root.expcesbin.place(relx=.55, rely=0.4, anchor="n")
    root.extbin = tk.Button(root, text="Go back", command=fixguiaddons)
    root.extbin.place(relx=.45, rely=0.6, anchor="n")

def Doc7():
    root.vent.place_forget()
    root.aent.place_forget()
    root.dent.place_forget()
    root.sent.place_forget()

    root.incomebin = tk.Button(root, text="Income saving")
    root.incomebin.place(relx=.35, rely=0.4, anchor="n")
    root.Savbin = tk.Button(root, text="Savings")
    root.Savbin.place(relx=.45, rely=0.4, anchor="n")
    root.expcesbin = tk.Button(root, text="Expences")
    root.expcesbin.place(relx=.55, rely=0.4, anchor="n")
    root.extbin = tk.Button(root, text="Go back", command=fixguiaddons)
    root.extbin.place(relx=.45, rely=0.6, anchor="n")

def Doc2_1():
    pass

def Doc5():
    root.vent.place_forget()
    root.aent.place_forget()
    root.dent.place_forget()
    root.sent.place_forget()

    root.incomebin = tk.Button(root, text="Income saving")
    root.incomebin.place(relx=.35, rely=0.4, anchor="n")
    root.Savbin = tk.Button(root, text="Savings")
    root.Savbin.place(relx=.45, rely=0.4, anchor="n")
    root.expcesbin = tk.Button(root, text="Expences")
    root.expcesbin.place(relx=.55, rely=0.4, anchor="n")
    root.extbin = tk.Button(root, text="Go back", command=fixguiaddons)
    root.extbin.place(relx=.45, rely=0.6, anchor="n")
    root.VEntLabel = tk.Label(root, text = '', font = ('calibre',10,'bold'))
    #This label is where we will display the diffrent enteries 

    
def end_The_program():
    dict_to_csv(root.user)
    root.destroy

#Here is the starting buttons
root.btn = tk.Button(root, text="Sign up", command=Doc4)
root.btn.place(relx=.5, rely=0.4, anchor="n")
root.exiting = tk.Button(root, text="Exit program", command=end_The_program)
root.exiting.place(relx=.05, rely=0.05, anchor="n")



root.user = csv_to_dictionary()







root.mainloop()