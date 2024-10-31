import tkinter as tk
from tkinter import ttk, Toplevel

root = tk.Tk()
altopantalla = root.winfo_screenheight()
anchopantalla = root.winfo_screenwidth()
# root.geometry("150x100+%d+%d" % (anchopantalla,altopantalla))
root.geometry("150x100")
etiqueta = tk.Label(root, text="selecciona tu genero...")
etiqueta.grid(column=0, row=0)
combo = ttk.Combobox(state="readonly",values=["hombre","mujer","helicoptero","otro"])
combo.grid(column=0,row=1,padx=5,pady=2)
boton = tk.Button(text="pulsame!")
boton.grid(column=0,row=2,padx=5,pady=2)





def decirGenero():
    ventana = Toplevel(root)
    ventana.resizable(1,1)
    ventana.geometry("150x50")
    genero = combo.get()
    label = tk.Label(ventana,text="TU GENERO ES ->"+genero)
    label.grid(row=0,column=0,padx=10,pady=10)


boton.bind('<Button-1>',lambda event: decirGenero())


root.mainloop()