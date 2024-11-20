import tkinter as tk
from tkinter import ttk
import mysql.connector

titulo = "Examen 2DAM"

root = tk.Tk()
root.title(titulo)
root.geometry("230x320+500+200")
root.resizable(0,0)




userLbl = tk.Label(root,text="Usuario:")
userTxt = tk.Entry(root)

passwordLbl = tk.Label(root,text="Password:")
passwordTxt = tk.Entry(root,show="*")

hostLbl = tk.Label(root,text="Host:")
hostTxt = tk.Entry(root)

databaseLbl = tk.Label(root,text="Base de datos:")
databaseTxt = tk.Entry(root)


btnConexion = tk.Button(root, text="Conectar")


userLbl.grid(column=0,row=0,padx=30,pady=5,sticky=tk.W)
userTxt.grid(column=0,row=1,padx=30,pady=5)
passwordLbl.grid(column=0,row=2,padx=30,pady=5,sticky=tk.W)
passwordTxt.grid(column=0,row=3,padx=30,pady=5)
hostLbl.grid(column=0,row=4,padx=30,pady=5,sticky=tk.W)
hostTxt.grid(column=0,row=5,padx=30,pady=5)
databaseLbl.grid(column=0,row=6,padx=30,pady=5,sticky=tk.W)
databaseTxt.grid(column=0,row=7,padx=30,pady=5)
btnConexion.grid(column=0,row=8,columnspan=2,padx=30,pady=5)

def conectar():
    
    conn = mysql.connector.connect(user=userTxt.get(),password=passwordTxt.get(),host=hostTxt.get(),database=databaseTxt.get())
    #conn = mysql.connector.connect(user="ahmed",password="ahmed",host="localhost",database="")
    cursor = conn.cursor()

    if(conn):
        print("###CONEXION CORRECTA A LA BASE DE DATOS###")
    
            
    if(btnConexion["text"] == "Conectar"):
        btnConexion.config(text="Desconectar")
    else:
        btnConexion.config(text="Conectar")
        conn.close()
        exit()
   
    ventanaSeleccion = tk.Toplevel(root)
    ventanaSeleccion.title(titulo)
    ventanaSeleccion.geometry("250x260")
    
    variableRadio = tk.StringVar()
    radio1 = tk.Radiobutton(ventanaSeleccion,variable=variableRadio, value=1,text="Creacion Base de datos")
    radio2 = tk.Radiobutton(ventanaSeleccion,variable=variableRadio, value=2,text="Creacion de Tablas")
    radio3 = tk.Radiobutton(ventanaSeleccion,variable=variableRadio, value=3,text="Insertar registro")
    radio4 = tk.Radiobutton(ventanaSeleccion,variable=variableRadio, value=4,text="Actualizacion de registros")
    radio5 = tk.Radiobutton(ventanaSeleccion,variable=variableRadio, value=5,text="Eliminacion de registros")
    radio6 = tk.Radiobutton(ventanaSeleccion,variable=variableRadio, value=6,text="Consulta de seleccion")

    btnAbrir = tk.Button(ventanaSeleccion,text="Abrir")
    
    radio1.grid(column=0,row=0,padx=20,pady=5,sticky=tk.W)
    radio2.grid(column=0,row=1,padx=20,pady=5,sticky=tk.W)
    radio3.grid(column=0,row=2,padx=20,pady=5,sticky=tk.W)
    radio4.grid(column=0,row=3,padx=20,pady=5,sticky=tk.W)
    radio5.grid(column=0,row=4,padx=20,pady=5,sticky=tk.W)
    radio6.grid(column=0,row=5,padx=20,pady=5,sticky=tk.W)

    btnAbrir.grid(column=0,row=6,padx=20,pady=10)
    
    def crearBbdd():
        ventanaQuery = tk.Toplevel(ventanaSeleccion)
        ventanaQuery.title(titulo)
        ventanaQuery.geometry("250x250")
        
        bbddLbl = tk.Label(ventanaQuery,text="Nombre de la bbdd:")
        bbddTxt = tk.Entry(ventanaQuery)
        btnEjecutar = tk.Button(ventanaQuery,text="Ejecutar")

        
        bbddLbl.grid(column=0,row=0,padx=30,pady=5,sticky=tk.W)
        bbddTxt.grid(column=0,row=1,padx=30,pady=5)
        btnEjecutar.grid(column=0,row=3,padx=30,pady=5)
        
        def crearbase():
            cursor.execute("CREATE DATABASE "+ str(bbddTxt.get()))
            
        btnEjecutar.bind("<Button-1>",lambda event: crearbase())
        
    def Query():
        ventanaQuery = tk.Toplevel(ventanaSeleccion)
        ventanaQuery.title(titulo)
        ventanaQuery.geometry("620x550")
        
        bbddLbl = tk.Label(ventanaQuery,text="Query:")
        bbddTxt = tk.Entry(ventanaQuery, width=70)
        btnEjecutar = tk.Button(ventanaQuery,text="Ejecutar")
        resultadoLbl = tk.Label(ventanaQuery,text="Resultado:")
        resultadoTxtArea = tk.Text(ventanaQuery,height=15,width=70)

        
        
        bbddLbl.grid(column=0,row=0,padx=30,pady=5,sticky=tk.W)
        bbddTxt.grid(column=0,row=1,padx=30,pady=5)
        btnEjecutar.grid(column=0,row=3,padx=30,pady=5)
        resultadoLbl.place(x=30,y=150)
        resultadoTxtArea.place(x=30,y=170)
        
        def ejecutarQuery():
            cursor.execute(bbddTxt.get())
            resultados = cursor.fetchall()
            
            resultadoTxtArea.delete(1.0,tk.END)
            for row in resultados:
                resultadoTxtArea.insert(tk.END,str(row) + "\n")
                
            if(len(resultados) == 0):
                resultadoTxtArea.insert(tk.END,"La sentencia ha sido ejecutada.\n ADVERTENCIA:PUEDE QUE NO DEVUELVA NADA EN CASO DE NO SER UN SELECT")
                
            conn.commit()
        
        btnEjecutar.bind("<Button-1>", lambda event: ejecutarQuery())
    
    def ejecutar():
        if(int(variableRadio.get()) == 1):
            crearBbdd()
        elif(int(variableRadio.get()) > 1 and int(variableRadio.get()) < 7):
            Query()
       
    btnAbrir.bind("<Button-1>",lambda event: ejecutar())        
    
    





btnConexion.bind("<Button-1>", lambda event: conectar())

root.mainloop()