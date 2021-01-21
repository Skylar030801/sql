import mysql.connector
from tkinter import *
from tkinter import messagebox
import tkinter as tk

root=tk.Tk()
root.title("My logs")
root.geometry("400x400")
root.configure(bg="red")

lbluser = tk.Label(root, text="Please enter username", )
lbluser.place(x=50, y=20)
Username = tk.Entry(root, width=45)
Username.place(x=250, y=20, width=100)
lblpassword = tk.Label(root, text="Please enter password ")
lblpassword.place(x=50, y=50)
Password = tk.Entry(root, width=35)
Password.place(x=250, y=50, width=100)


root.mainloop()
