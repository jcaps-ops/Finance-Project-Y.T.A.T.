#This will be the set up for the menu using the GUI
import tkinter as tk
from tkinter import *
from Functions_Edited_ForGUI import *
import time

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
def Doc2():
    btn.place_forget()
    sign.place_forget()
    root.singuplabel = tk.Label(root, text=f"This is where you would have signed up but that has not been added yet", bg="Light grey", font=("Times new roman", 14, "bold"))
    root.singuplabel.place(relx=.5, rely=0, anchor="n")

    root.name_entry = tk.Entry(root,textvariable = name_var, font=('calibre',10,'normal'))
    root.name_entry.place(relx=0.55, rely=0.3, anchor="n")

    root.name_label = tk.Label(root, text = 'Username', font=('calibre',10, 'bold'))
    root.name_label.place(relx=0.45, rely=0.3, anchor="n")

    root.passw_entry=tk.Entry(root, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*')
    root.passw_entry.place(relx=0.55, rely=0.4, anchor="n")

    root.passw_label = tk.Label(root, text = 'Password', font = ('calibre',10,'bold'))
    root.passw_label.place(relx=0.45, rely=0.4, anchor="n")

    root.btn1 = tk.Button(root, text="Enter",command=signingup)
    root.btn1.place(relx=.5, rely=0.7, anchor="n")
def signingup():
    root.singuplabel.place_forget()
    root.SgUpLabel = tk.Label(root, text=f"", bg="Light grey", font=("Times new roman", 14, "bold"))
    root.SgUpLabel.place(relx=.5, rely=0, anchor="n")

    name=name_var.get()
    password=passw_var.get()
    GuiEdt_user_creator("docs/accounts.csv",name,password,root.SgUpLabel)
    #What ever do to the document
    Doc4()
def Doc3():
    
    btn.place_forget()
    sign.place_forget()
    root.singuplabel = tk.Label(root, text=f"This is tempory text while we add the sign in function\n To go passed the username is Test1 and password is Test2", bg="Light grey", font=("Times new roman", 14, "bold"))
    root.singuplabel.place(relx=.5, rely=0, anchor="n")

    

    root.name_entry = tk.Entry(root,textvariable = name_var, font=('calibre',10,'normal'))
    root.name_entry.place(relx=0.55, rely=0.3, anchor="n")

    root.name_label = tk.Label(root, text = 'Username', font=('calibre',10, 'bold'))
    root.name_label.place(relx=0.45, rely=0.3, anchor="n")

    root.passw_entry=tk.Entry(root, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*')
    root.passw_entry.place(relx=0.55, rely=0.4, anchor="n")

    root.passw_label = tk.Label(root, text = 'Password', font = ('calibre',10,'bold'))
    root.passw_label.place(relx=0.45, rely=0.4, anchor="n")

    root.btn1 = tk.Button(root, text="Enter",command=submiting_password)
    root.btn1.place(relx=.5, rely=0.7, anchor="n")
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
    root.singuplabel.place_forget()
    root.btn1.place_forget()
    root.name_entry.place_forget()
    root.name_label.place_forget()
    root.passw_entry.place_forget()
    root.passw_label.place_forget()
    root.singuplabel.place_forget()
    root.wrg_label.place_forget()

    #Replacing
    root.vent = tk.Button(root, text="View your entries", command=Doc5)
    root.vent.place(relx=.35, rely=0.4, anchor="n")
    root.aent = tk.Button(root, text="Add an entry", command=Doc6)
    root.aent.place(relx=.45, rely=0.4, anchor="n")
    root.dent = tk.Button(root, text="Delete an entry", command=Doc7)
    root.dent.place(relx=.55, rely=0.4, anchor="n")
    root.sent = tk.Button(root, text="View a statistics", command=Doc8)
    root.sent.place(relx=.65, rely=0.4, anchor="n")
    


def Doc8():
    root.vent.place_forget()
    root.aent.place_forget()
    root.dent.place_forget()
    root.sent.place_forget()

    root.barbin = tk.Button(root, text="Bar Graph")
    root.barbin.place(relx=.35, rely=0.4, anchor="n")
    root.piebin = tk.Button(root, text="Pie-chart graph")
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

    


#Here is the starting buttons
btn = tk.Button(root, text="Sign up", command=Doc2)
btn.place(relx=.53, rely=0.4, anchor="n")
root.wrg_label = tk.Label(root, text = '', font = ('calibre',10,'bold'))
sign = tk.Button(root, text="Sign in", command=Doc3)
sign.place(relx=.47, rely=0.4, anchor="n")
root.exiting = tk.Button(root, text="Exit program", command=root.destroy)
root.exiting.place(relx=.05, rely=0.05, anchor="n")








root.mainloop()