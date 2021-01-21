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

lbluser = tk.Label(root, text="Please enter Name", )
lbluser.place(x=50, y=20)
Username = tk.Entry(root, width=45)
Username.place(x=250, y=20, width=100)
lblpassword = tk.Label(root, text="Please enter Surname ")
lblpassword.place(x=50, y=50)
Password = tk.Entry(root, width=35)
Password.place(x=250, y=50, width=100)
lblphone_number = tk.Label(root, text="Please enter phone number ")
lblphone_number.place(x=50, y=80)
phone_number = tk.Entry(root, width=35)
phone_number.place(x=250, y=80, width=100)

def logged():
    d = datetime.now()
    t = d.strftime("%H:%M")
    dt = d.strftime("%d/%m/%y")
    messagebox.showinfo('info', "You have successfully logged in")
    outW = Tk()
    def out():
        d2 = datetime.now()
        t2 = d2.strftime("%H:%M")
        u = Username.get()
        infoU2 = u, t, t2, dt
        uCom2 = "INSERT INTO register(Name, Time, Time_out, Date) VALUES(%s,%s,%s,%s)"

        mycursor.execute(uCom2, infoU2)
        mydb.commit()
        messagebox.showinfo()
    btnOut = Button(outW, text="Out", command=out)
    btnOut.pack()

logbtn = tk.Button(root, text="login", bg='Magenta', command=logged)
logbtn.place(x=250, y=135, width=150)



root.mainloop()
