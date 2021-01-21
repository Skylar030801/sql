import mysql.connector
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from datetime import *
mydb = mysql.connector.connect(user='lifechoices', password='@Lifechoices1234',
                               host='127.0.0.1', database='Lifechoicesonline',
                               auth_plugin='mysql_native_password')
mycursor = mydb.cursor()
def verify():
    users = Username.get()
    passs = Password.get()
    sql = "select * from Login where username = %s and password = %s"
    mycursor.execute(sql, [(users), (passs)])
    results = mycursor.fetchall()
    if results:
        for i in results:
            logged()
            break
    else:
        failed()

def logged():
    messagebox.showinfo("You have successfully logged")
    import mainmenu
    root.destroy()


def failed():
    messagebox.showinfo("Error, try again")
    Username.delete(0, END)
    Password.delete(0, END)

#Design the login form
root = tk.Tk()
root.geometry("400x400")
root.title("Login Page")
lbluser = tk.Label(root, text="Please enter username", )
lbluser.place(x=50, y=20)
Username = tk.Entry(root, width=45)
Username.place(x=250, y=20, width=100)
lblpassword = tk.Label(root, text="Please enter password ")
lblpassword.place(x=50, y=50)
Password = tk.Entry(root, width=35)
Password.place(x=250, y=50, width=100)

Loginbtn = tk.Button(root, text="Login", bg='Magenta', command=verify)
Loginbtn.place(x=150, y=135, width=55)


root.mainloop()
