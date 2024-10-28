import tkinter as tk
from tkinter import ttk,messagebox

root = tk.Tk()


entrada = tk.Entry()
entrada.grid(row=0, column=1 )


def chkBox_Click():
    if opt1.get() == 1:
        messagebox.showinfo(message="Esta activo", title="2DAM")
    else:
        messagebox.showinfo(message="Esta desactivado", title="3DAM")

opt1 = tk.IntVar()
opt2 = tk.IntVar()
opt3 = tk.IntVar()



chkopt1 = ttk.Checkbutton(root, text="Opcion 1", variable=opt1, state="enable", command=chkBox_Click)
chkopt2 = ttk.Checkbutton(root, text="Opcion 2", variable=opt2, state="disable")
chkopt3 = ttk.Checkbutton(root, text="Opcion 3", variable=opt3, state="checked")
chkopt1.grid(column= 1, row=1, sticky=tk.W)
chkopt2.grid(column= 1, row=2)
chkopt3.grid(column= 1, row=3)



root.mainloop()