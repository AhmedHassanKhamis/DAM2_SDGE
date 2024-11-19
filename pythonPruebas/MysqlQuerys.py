import mysql.connector
from tkinter import ttk
import tkinter as tk 



root = tk.Tk()
root.title("Conector Mysql")
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

## SECCION CONECTOR ##
conn = mysql.connector.connect(user="ahmed", password="ahmed", host="localhost")
print(conn)
cursor = conn.cursor()
cursor.execute("use DAM")


def conectar():
    ventanaQuery = tk.Toplevel(root)
    ventanaQuery.geometry("500x400")
    ventanaQuery.title("EJECUTOR DE QUERYS")
    ventanaQuery.resizable(1,1)

    queryLbl = ttk.Label(ventanaQuery, text="QUERY O CONSULTA:")
    queryTxt = ttk.Entry(ventanaQuery,width=55)
    btnExecute = ttk.Button(ventanaQuery,text="Ejecutar")
    textArea = tk.Text(ventanaQuery,height=15,width=60)
    btnCrearAlumno = ttk.Button(ventanaQuery,text="CREAR ALUMNO")


    queryLbl.place(x=10,y=10)
    queryTxt.place(x=135,y=10)
    btnExecute.place(x=200,y=40)
    textArea.place(x=5,y=70)
    btnCrearAlumno.place(x=200, y=350)

    btnExecute.bind("<Button-1>",lambda event: ejecutarQuery())
    btnCrearAlumno.bind("<Button-1>", lambda event:insertarAlumno())

    def insertarAlumno():
        ventanaAlumno = tk.Toplevel(ventanaQuery)
        ventanaAlumno.title("Crear Alumno...")
        dniLbl = ttk.Label(ventanaAlumno, text="Dni:")
        dniTxt = ttk.Entry(ventanaAlumno,width=20)

        nombreLbl = ttk.Label(ventanaAlumno, text="Nombre:")
        nombreTxt = ttk.Entry(ventanaAlumno,width=20)

        apellidosLbl = ttk.Label(ventanaAlumno, text="Apellidos:")
        apellidosTxt = ttk.Entry(ventanaAlumno,width=20)

        gradoLbl = ttk.Label(ventanaAlumno, text="Grado:")
        gradoTxt = ttk.Entry(ventanaAlumno,width=20)
        
        edadLbl = ttk.Label(ventanaAlumno, text="Edad:")
        edadTxt = ttk.Entry(ventanaAlumno,width=20)

        btnInsertar = ttk.Button(ventanaAlumno,text="CREAR")

        dniLbl.grid(column=0,row=0,padx=10,pady=10)
        nombreLbl.grid(column=0,row=1,padx=10,pady=10)
        apellidosLbl.grid(column=0,row=2,padx=10,pady=10)
        gradoLbl.grid(column=0,row=3,padx=10,pady=10)
        edadLbl.grid(column=0,row=4,padx=10,pady=10)
        dniTxt.grid(column=1,row=0,padx=10,pady=10)
        nombreTxt.grid(column=1,row=1,padx=10,pady=10)
        apellidosTxt.grid(column=1,row=2,padx=10,pady=10)
        gradoTxt.grid(column=1,row=3,padx=10,pady=10)
        edadTxt.grid(column=1,row=4,padx=10,pady=10)
        btnInsertar.grid(column=0,columnspan=2,row=5,padx=10,pady=10)


        btnInsertar.bind("<Button-1>", lambda event: crearAlumno())

        def crearAlumno():
            cursor.execute("INSERT INTO Alumnos (dni,nombre,apellidos,grado,edad) values(%s,%s,%s,%s,%s)", (dniTxt.get(), nombreTxt.get(), apellidosTxt.get(), gradoTxt.get(), int(edadTxt.get())))
            conn.commit()
            print(cursor.fetchall())

    def insertarModulo(modulo_id,denominacion,alumno_id):
        cursor.execute("INSERT INTO Modulos values(%s,%s,%s)",(modulo_id,denominacion,alumno_id))

    def buscarAlumno(dni):
        cursor.execute("SELECT * FROM Alumnos where id ='%s'",(dni))
        return cursor.fetchall()

    def buscarModulo(modulo_id):
        cursor.execute("SELECT * FROM Modulos where Modulo_ID = %s",(modulo_id))
        return cursor.fetchall()
    
    def eliminarAlumno(dni):
        cursor.execute("DELETE FROM Alumnos where dni = '%s'",(dni))
    
    def eliminarModulo(modulo_id):
        cursor.execute("DELETE FROM Modulos where Modulo_id = ",(modulo_id))

    def actualizarAlumno(dni,nombre,apellidos,grado,edad):
        cursor.execute("UPDATE Alumnos SET nombre ='%s', apellidos = '%s', grado = '%s', edad = %s WHERE dni = '%s'",(nombre,apellidos,grado,edad,dni))

    def actualizarModulo(denominacion, modulo, dni):
        cursor.execute("UPDATE Modulos SET Denominacion = '%s' where Modulo_id = %s and Alumno_DI = '%s'",(denominacion,modulo,dni))

    def ejecutarQuery():    
        #conn = mysql.connector.connect(user=userTxt.get(), password=passwordTxt.get(), host=hostTxt.get())
        

        cursor.execute(queryTxt.get())
        resultado = cursor.fetchall()

        # seccion donde dejo limpio la parte de el text area y luego introduzco los valores mediante un bucle con el metodo insert y diciendo desde donde empieza y transformando cada linea en string
        textArea.delete(1.0, tk.END)
        for row in resultado:
            textArea.insert(tk.END, str(row) + '\n')
        
        #para imprimir lo que me devuelve por terminal
        # print("\n\n---------resultado---------")
        # print(resultado)

        # PARTE DE QUERYS ########################################################

        #cursor.execute("create database DAM")


        # cursor.execute("CREATE TABLE Alumnos (" + 
        # "dni VARCHAR(8) not null, " +
        # "nombre VARCHAR(10) not null, " +
        # "apellidos VARCHAR(20) not null, " +
        # "grado VARCHAR(5) not null, " +
        # "edad INT not null, PRIMARY KEY(dni)) ENGINE=InnoDB")

        # cursor.execute("CREATE TABLE Modulos ("+
        # "Modulo_ID INT, "+
        # "Denominacion VARCHAR(10) not null, " +
        # "Alumno_DI VARCHAR(8) not null, "+
        # "FOREIGN KEY (Alumno_DI) " +
        # "REFERENCES Alumnos(dni) ON DELETE CASCADE) ENGINE=InnoDB")

        # cursor.execute("INSERT INTO Alumnos (dni, nombre, apellidos, grado, edad) VALUES ('12345678', 'Carlos', 'Gómez Rojo', 'DAM', 23)")
        # cursor.execute("INSERT INTO Alumnos (dni, nombre, apellidos, grado, edad) VALUES ('987654321', 'Ahmed', 'Hassan Khamis', 'DAW', 29)")

        
btnConnect.bind("<Button-1>",lambda event: conectar())



root.mainloop()

conn.close()