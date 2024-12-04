import pdfkit
from jinja2 import Environment, FileSystemLoader
import os
import tkinter as tk
from tkinter import ttk
import mysql.connector
from matplotlib import pyplot as plt
import numpy as np

env = Environment(loader=FileSystemLoader(''))


root = tk.Tk()
root.geometry("350x450")
root.title("GENERADOR_BOLETIN")

labels = ["DNI", "Nombre", "Fecha de Nacimiento", "Teléfono", "Nota PSP", "Nota AD", "Nota DI", "Nota PMDM", "Nota ING", "Nota EIE", "Nota SDGE"]
entries = []

for i, label in enumerate(labels):
    tk.Label(root, text=label).grid(row=i, column=0, padx=10, pady=5)
    entry = tk.Entry(root)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries.append(entry)

dni_entry, nombre_entry, fecha_nacimiento_entry, telefono_entry, nota_psp_entry, nota_ad_entry, nota_di_entry, nota_pmdm_entry, nota_ing_entry, nota_eie_entry, nota_sdge_entry = entries


info = {
    "title":"Boletin_Notas_Python",
    "heading":"BOLETIN DE NOTAS", 
    "content":"En el siguiente documento se representan las notas de un alumno cursando en el ciclo formativo de grado superior 'DAM'.",
    "dni": "12345678A",
    "nombre": "Juan Pérez",
    "fecha_nacimiento": "01/01/2000",
    "telefono": "600123456",
    "nota_psp": "8.5",
    "nota_ad": "7.0",
    "nota_di": "9.0",
    "nota_pmdm": "8.0",
    "nota_ing": "7.5",
    "nota_eie": "6.5",
    "nota_sdge": "9.5"
}

def generate_pdf():
    info["dni"] = dni_entry.get()
    info["nombre"] = nombre_entry.get()
    info["fecha_nacimiento"] = fecha_nacimiento_entry.get()
    info["telefono"] = telefono_entry.get()
    info["nota_psp"] = nota_psp_entry.get()
    info["nota_ad"] = nota_ad_entry.get()
    info["nota_di"] = nota_di_entry.get()
    info["nota_pmdm"] = nota_pmdm_entry.get()
    info["nota_ing"] = nota_ing_entry.get()
    info["nota_eie"] = nota_eie_entry.get()
    info["nota_sdge"] = nota_sdge_entry.get()

    template = env.get_template('template.html')
    html_content = template.render(info)
    pdfkit.from_string(html_content, 'Boletin_Notas_Python.pdf', css='style.css')
    print("PDF successfully created!")








def generarGrafica():
    conn = mysql.connector.connect(user='ahmed',password='ahmed',host='localhost')
    cursor = conn.cursor()
    cursor.execute('USE DAM2')

    sql = 'SELECT nombre FROM alumnos'        
    cursor.execute(sql)
    nombres = []
    for n in cursor.fetchall():
        nombres.append(n[0])
        
    sql = 'SELECT nota_psp, nota_ad, nota_di, nota_pmdm, nota_ing, nota_eie, nota_sdge FROM alumnos'    
    mediasPost = []
    cursor.execute(sql)
    for i in cursor.fetchall():
        media = sum(i) / len(i)
        mediasPost.append(media)

    cursor.close()
    conn.close()

    plt.plot(nombres, mediasPost, label="Media")
    
    plt.xlabel("Alumnos")
    plt.ylabel("Notas")
    plt.legend()
    plt.title("Notas Medias de alumnos")

    plt.savefig('MediaClase.png')







def insertarAlumno():
    conn=mysql.connector.connect(user='ahmed',password='ahmed',host='localhost')
    cursor=conn.cursor()
    cursor.execute('USE DAM2')
    sql = '''
    INSERT INTO alumnos (dni, nombre, fecha_nacimiento, telefono, nota_psp, nota_ad, nota_di, nota_pmdm, nota_ing, nota_eie, nota_sdge)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    '''
    values = (
        dni_entry.get(),
        nombre_entry.get(),
        fecha_nacimiento_entry.get(),
        telefono_entry.get(),
        float(nota_psp_entry.get()),
        float(nota_ad_entry.get()),
        float(nota_di_entry.get()),
        float(nota_pmdm_entry.get()),
        float(nota_ing_entry.get()),
        float(nota_eie_entry.get()),
        float(nota_sdge_entry.get())
    )
    cursor.execute(sql, values)
    conn.commit()
    conn.close()

def generarTabla():
    conn=mysql.connector.connect(user='ahmed',password='ahmed',host='localhost')
    cursor=conn.cursor()
    cursor.execute('USE DAM2')
    cursor.execute('DROP TABLE IF EXISTS alumnos')
    query = '''
    CREATE TABLE IF NOT EXISTS alumnos (
        dni VARCHAR(45),
        nombre VARCHAR(45),
        fecha_nacimiento VARCHAR(45),
        telefono VARCHAR(45),
        nota_psp FLOAT,
        nota_ad FLOAT,
        nota_di FLOAT,
        nota_pmdm FLOAT,
        nota_ing FLOAT,
        nota_eie FLOAT,
        nota_sdge FLOAT
    )
    '''
    cursor.execute(query)
    conn.commit()
    conn.close()

generate_button = tk.Button(root, text="Generate PDF", command=generate_pdf)
generate_button.grid(row=len(labels), column=0, pady=10)

grafica_button = tk.Button(root, text="Generar Gráfica", command=generarGrafica)
grafica_button.grid(row=len(labels), column=1, pady=10)

insertar_button = tk.Button(root, text="Insertar Alumno", command=insertarAlumno)
insertar_button.grid(row=len(labels) + 1, column=0, pady=10)

tabla_button = tk.Button(root, text="Generar Tabla", command=generarTabla)
tabla_button.grid(row=len(labels) + 1, column=1, pady=10)









root.mainloop()