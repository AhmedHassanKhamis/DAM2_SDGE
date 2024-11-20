import tkinter as tk
from tkinter import ttk
import mysql.connector



root = tk.Tk()
root.title("Conexion BBDD")
root.geometry("200x220")

 



userLbl = tk.Label(root,text="Usuario:")
userTxt = tk.Entry(root, width=15) 

passwordLbl = tk.Label(root,text="Password:")
passwordTxt = tk.Entry(root, width=15) 

hostLbl = tk.Label(root,text="Host:")
hostTxt = tk.Entry(root, width=15) 

databaseLbl = tk.Label(root,text="Database:")
databaseTxt = tk.Entry(root, width=15) 

btnConn = tk.Button(root, text="Conectar")


userLbl.grid(column=0,row=0,padx=10,pady=10)
userTxt.grid(column=1,row=0,padx=10,pady=10)
passwordLbl.grid(column=0,row=1,padx=10,pady=10)
passwordTxt.grid(column=1,row=1,padx=10,pady=10)
hostLbl.grid(column=0,row=2,padx=10,pady=10)
hostTxt.grid(column=1,row=2,padx=10,pady=10)
databaseLbl.grid(column=0,row=3,padx=10,pady=10)
databaseTxt.grid(column=1,row=3,padx=10,pady=10)
btnConn.grid(column=0,columnspan=2,row=4,padx=10,pady=10)


def conectar():
    conn = mysql.connector.connect(user=userTxt.get(),password=passwordTxt.get(),host=hostTxt.get(),database=databaseTxt.get())
    #conn = mysql.connector.connect(user="ahmed",password="ahmed",host="localhost",database="")
    print(conn)
    conn.close()
    ventanaQuery = tk.Toplevel(root)
    ventanaQuery.title("Querys")
    ventanaQuery.geometry("500x400")

    consultaLbl = tk.Label(ventanaQuery, text="Query:")
    consultaTxt = tk.Entry(ventanaQuery, width=70)
    btnQuery = tk.Button(ventanaQuery, text="Ejecutar")
    resultadoTxtA = tk.Text(ventanaQuery,height=15,width=60)

    consultaLbl.place(x=10,y=10)
    consultaTxt.place(x=55,y=10)
    btnQuery.grid(column=0,row=2,columnspan=2,pady=40)
    resultadoTxtA.grid(column=0,row=3,columnspan=2)

    def ejecutar():
        conn = mysql.connector.connect(user=userTxt.get(),password=passwordTxt.get(),host=hostTxt.get(),database=databaseTxt.get())
        cursor = conn.cursor()
        cursor.execute(consultaTxt.get())
        resultado = cursor.fetchall()
        resultadoTxtA.delete(1.0,tk.END)
        for row in resultado:
            resultadoTxtA.insert(tk.END,str(row) + "\n")
        if(len(resultado) == 0):
            resultadoTxtA.insert(tk.END,"NO HAY RESULTADOS O LA QUERY NO DEVUELVE NADA")
        conn.commit()
        conn.close()
        print("\n\n-------------Resultado-------------")
        print(resultado)
        

    btnQuery.bind("<Button-1>", lambda event: ejecutar())


# create table bibliotecas(nombre VARCHAR(45) primary key, direccion VARCHAR(500) DEFAULT "SIN ESPECIFICAR",telefono int);
# create table libros(titulo varchar(100),autor varchar(45),biblioteca varchar(45),foreign key (biblioteca) references bibliotecas(nombre))

# insert into bibliotecas values('casalibro','vallecas',777)
# insert into libros values('Geronimo Stilton','',777)


btnConn.bind("<Button-1>", lambda event: conectar())
root.mainloop()
