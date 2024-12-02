import pdfkit
from jinja2 import Environment, FileSystemLoader
import os
import tkinter as tk
from tkinter import ttk

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






generate_button = tk.Button(root, text="Generate PDF", command=generate_pdf)
generate_button.grid(row=len(labels), columnspan=2, pady=10)









root.mainloop()