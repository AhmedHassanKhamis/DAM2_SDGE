import tkinter as tk

root = tk.Tk()


entrada = tk.Entry()
label = tk.Label(root, text="Introduce la temperatura en grados Celsius")
var = tk.IntVar()
radio1 = tk.Radiobutton(root, text="Fahrenheit", variable=var, value=1)
radio2 = tk.Radiobutton(root, text="Kelvin", variable=var, value=2)
boton = tk.Button(root, text="Convertir")
resultado = tk.Label(root, text="Resultado")



label.grid(column= 0, row=0)
entrada.grid(column= 0, row=1)
radio1.grid(column= 0, row=2)
radio2.grid(column= 0, row=3)


for widget in root.winfo_children():
    widget.grid_configure(padx=10, pady=10)

boton.grid(column= 0, row=4)
boton.bind("<Button-1>", lambda x: convertir())



def convertir():
    temperatura = float(entrada.get())
    if var.get() == 1:
        resultado["text"] = temperatura * 9/5 + 32
    else:
        resultado["text"] = temperatura + 273.15
    



root.mainloop()