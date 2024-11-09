import mysql.connector
import tkinter
from tkinter import Tk, ttk


root = Tk()
root.title="Conector Mysql"
root.geometry("300x200")
welcomeLbl = ttk.Label(root,text="Rellena los campos para realizar una conexion:")
userLbl = ttk.Label(root, text="Usuario:")
userTxt = ttk.Entry(root)
passwordLbl = ttk.Label(root, text="Password:")
passwordTxt = ttk.Entry(root)
hostLbl = ttk.Label(root, text="Host:")
hostTxt = ttk.Entry(root)
btnConnect = ttk.Button(root, text="Conectar")


welcomeLbl.place(x=10,y=10)
userLbl.place(x=10,y=40)
userTxt.place(x=80,y=40)
passwordLbl.place(x=10,y=70)
passwordTxt.place(x=80,y=70)
hostLbl.place(x=10,y=100)
hostTxt.place(x=80,y=100)
btnConnect.place(x=90,y=140)

def conectar():
    conn = mysql.connector.connect(user=userTxt.get(), password=passwordTxt.get(), host=hostTxt.get())
    print(conn)
    conn.close()



btnConnect.bind("<Button-1>",lambda x: conectar())




root.mainloop()