import mysql.connector
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from datetime import *

mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234',
                               host='127.0.0.1', database='Lifechoicesonline',
                               auth_plugin='mysql_native_password')
mycursor = mydb.cursor()

root=tk.Tk()
root.title("My logs")
root.geometry("400x400")
root.configure(bg="red")

lblName = tk.Label(root, text="Please enter Name", )
lblName.place(x=50, y=20)
Name = tk.Entry(root, width=45)
Name.place(x=250, y=20, width=100)
lblSurname = tk.Label(root, text="Please enter Surname ")
lblSurname.place(x=50, y=50)
Surname = tk.Entry(root, width=35)
Surname.place(x=250, y=50, width=100)
lblphone_number = tk.Label(root, text="Please enter phone number ")
lblphone_number.place(x=50, y=80)
phone_number = tk.Entry(root, width=35)
phone_number.place(x=250, y=80, width=100)


def usertable():
    user_info = (Name.get() , Surname.get() , phone_number.get() )
    fmsw = "INSERT INTO register (Name , Surname , Phone_Number) VALUES(%s ,%s ,%s)"
    mycursor.execute(fmsw, user_info)
    mydb.commit()
    result = mycursor
    if result:
        messagebox.showinfo("info","You have successfully registered")

    else:
        failed()

#if login details are incorrect
def failed():
    messagebox.showinfo("Error", "Please try again")






Registerbtn = tk.Button(root, text="Register new user", bg='Magenta', command=usertable)
Registerbtn.place(x=250, y=135, width=150)



root.mainloop()
