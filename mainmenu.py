import mysql.connector
from tkinter import *
from tkinter import messagebox
import tkinter as tk


root=tk.Tk()
root.title("My logs")
root.geometry("400x400")
root.configure(bg="red")

def stud():
    import students
    students.mainloop()

def admin():
    import admin
    admin.mainloop()

def staff():
    import staff
    staff.mainloop()

def register():
    import register
    register.mainloop()

def visitors():
    import visitors
    visitors.mainloop()


adminButton = Button(root)
adminButton.configure(text = "ADMIN", command=admin, fg = 'white', bg = 'purple')
adminButton.place(y = 100, x = 10)

staffButton = Button(root)
staffButton.configure(text = "STAFF", command=staff, fg = 'white', bg = 'purple')
staffButton.place(y = 150, x = 10)

visitorsButton = Button(root)
visitorsButton.configure(text = "VISITORS", command=visitors, fg = 'white', bg = 'purple')
visitorsButton.place(y = 200, x = 10)

studentsButton = Button(root)
studentsButton.configure(text = "STUDENTS", command=stud ,fg = 'white', bg = 'purple')
studentsButton.place(y = 250, x = 10)

registerButton = Button(root)
registerButton.configure(text = "REGISTER", command=register,fg = 'white', bg = 'purple')
registerButton.place(y = 300, x = 10)



closeButton = Button(root)
closeButton.configure(text = "CLOSE", fg = 'white', bg = 'purple')
closeButton.place(y = 350, x = 10)



#close funtion
def close():
    quit()



#attaching the "close" function to the "close" button
closeButton.configure(command = close)

root.mainloop()
