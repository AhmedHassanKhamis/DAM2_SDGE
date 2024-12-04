import mysql.connector
import tkinter as tk
from tkinter import ttk
from click.decorators import command
from matplotlib import pyplot as plt
import numpy as np
import jinja2
import pdfkit

root=tk.Tk()
root.geometry("400x400")


#FUNCIONES

def crear_grafica():
        conn=mysql.connector.connect(user='root',password='1234',host='localhost')
        cursor=conn.cursor()
        cursor.execute('USE alumnos')

        sql='SELECT nombre FROM alu'        
        cursor.execute(sql)
        nombres=list()
        print(nombres)
        for n in cursor.fetchall():
            nombres=np.append(nombres,n)
         
        
        sql='SELECT nota1,nota2,nota3,nota4 FROM alu'    
        mediasPost=list()
        cursor.execute(sql)
        media=float()
        print(media)
        for i in cursor.fetchall():
           media=(i[0]+i[1]+i[2]+i[3])/4
           mediasPost=np.append(mediasPost,media)

        print(nombres)
        print(mediasPost)

        plt.plot(nombres,mediasPost, label="Media")
        
        plt.xlabel("Notas")
        plt.ylabel("Alumnos")
        plt.legend()
        plt.title("Notas Medias de alumnos")

        plt.savefig('MediaClase.png')
 


def crear_archivo(ruta_template,info,rutacss=''):
    
    nombre_template=ruta_template.split('/')[-1]
    ruta_template=ruta_template.replace(nombre_template,"")

    env= jinja2.Environment(loader=jinja2.FileSystemLoader(ruta_template))
    template= env.get_template(nombre_template)
    html= template.render(info)
    print(html)

    options ={
        'page-size' :'letter',
        'margin-top' : '0.05in',
        'margin-bottom':'0.05in',
        'margin-left': '0.05in',
        'margin-right': '0.05in',
        'encoding':'UTF-8'
        
    }

    config= pdfkit.configuration(wkhtmltopdf= '/usr/bin/wkhtmltopdf')
    ruta_salida= '/media/usertar/PuntiDiscoExtraible/2DAM/SGE/Python/EjercicioPDf/EjercicioPDFs/fichero.pdf'

    pdfkit.from_string(html, ruta_salida, css=rutacss, options=options, configuration=config)

    



def crearPDF():
    global dni

    query='SELECT * FROM alu WHERE dni="'+ dni.get() +'"'
    conn=mysql.connector.connect(user='root',password='1234',host='localhost')
    cursor=conn.cursor()
    cursor.execute('USE alumnos')
    cursor.execute(query)
    usuario = cursor.fetchone()
    conn.close()

    nameEx=usuario[0]
    apeEx=usuario[1]
    dniEx=usuario[2]
    n1Ex=usuario[4]
    n2Ex=usuario[6]
    n3Ex=usuario[8]
    n4Ex=usuario[10]


    for n in usuario:
        print(n)
    
    if __name__ == '__main__':
        media=(usuario[4]+usuario[6]+usuario[8]+usuario[10])/4
        ruta_template='/media/usertar/PuntiDiscoExtraible/2DAM/SGE/Python/EjercicioPDf/EjercicioPDFs/template.html'
        info= {
            'nombre':nameEx,
            'apellido':apeEx,
            'curso':"DAM",
            'dni': dniEx,
            'modulo1':'SGE',
            'nota1':n1Ex,
            'modulo2':'DI',
            'nota2':n2Ex,
            'modulo3':'AD',
            'nota3':n3Ex,
            'modulo4':'PSP',
            'nota4':n4Ex,
            'tutor':'Mario',
            'media':media,
            'fecha':'27-11-2024'}
        rutacss= '/media/usertar/PuntiDiscoExtraible/2DAM/SGE/Python/EjercicioPDf/EjercicioPDFs/estilos.css'
        
        crear_archivo(ruta_template,info,rutacss)


def insertar(nombre,apellidos,dni,nota1,nota2,nota3,nota4):
    
    conn=mysql.connector.connect(user='root',password='1234',host='localhost')
    cursor=conn.cursor()
    cursor.execute('USE alumnos')
    sql='INSERT INTO alu (nombre,apellidos,dni,modulo1,nota1,modulo2,nota2,modulo3,nota3,modulo4,nota4,tutor,fecha) VALUES  ("'+nombre+'","'+apellidos+'","'+dni+'","SGE",'+nota1+',"DI",'+nota2+',"AD",'+nota3+',"PSP",'+nota4+',"Mario","27/11/2024")'
    cursor.execute(sql)
    conn.commit()
    conn.close()
    
    crearPDF()
    
    





#VARIABLES DE DATOS
nombre=tk.StringVar();
apellidos=tk.StringVar();
dni=tk.StringVar();
nota1=tk.StringVar();
nota2=tk.StringVar();
nota3=tk.StringVar();
nota4=tk.StringVar();





#GADGETS
lblNombre=tk.Label(root,text="Nombre:").place(x=20,y=30)

etNombre=tk.Entry(root,textvariable=nombre).place(x=125,y=30)

lblApellido=tk.Label(root,text="Apellidos:").place(x=20,y=60)
etApellidos=tk.Entry(root,textvariable=apellidos).place(x=125,y=60)

lblDni=tk.Label(root,text="DNI:").place(x=20,y=90)
etDni=tk.Entry(root,textvariable=dni).place(x=125,y=90)

lblNota1=tk.Label(root,text="Nota en SGE:").place(x=20,y=150)
etNota1=tk.Entry(root,textvariable=nota1).place(x=125,y=150)

lblNota2=tk.Label(root,text="Nota en DI:").place(x=20,y=180)
etNota2=tk.Entry(root,textvariable=nota2).place(x=125,y=180)

lblNota3=tk.Label(root,text="Nota en AD:").place(x=20,y=210)
etNota3=tk.Entry(root,textvariable=nota3).place(x=125,y=210)

lblNota4=tk.Label(root,text="Nota en PSP:").place(x=20,y=240)
etNota4=tk.Entry(root,textvariable=nota4).place(x=125,y=240)


btnInsertar=tk.Button(root,text="Insertar",command=lambda:insertar(nombre.get(),apellidos.get(),dni.get(),nota1.get(),nota2.get(),nota3.get(),nota4.get())).place(x=150,y=270)
btnGrafica=tk.Button(root,text="Crear Gráfica",command=crear_grafica).place(x=150,y=325)

etNota4=tk.Entry(root,textvariable=dni).place(x=125,y=375)
btnPDF=tk.Button(root,text="Crear PDF de alumno",command=lambda:crearPDF()).place(x=175,y=375)


root.mainloop()