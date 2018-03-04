from tkinter import *
from tkinter import ttk

import subprocess
import sys

def isletmekar():
    subprocess.check_call([sys.executable, 'sub_programs/Odev1_isletmeKar.py'])

def OEE():
    subprocess.check_call([sys.executable, 'sub_programs/Odev2_OEE.py'])

def ABC():
    subprocess.check_call([sys.executable, 'sub_programs/Odev3_AdambasiCiro.py'])


root = Tk()
root.title("İşletme Takip Programı")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
        
ttk.Button(mainframe, text="İşletme Karı Hesapla", command=isletmekar).grid(column=2, row=2, sticky=W)
ttk.Button(mainframe, text="İşletme OEE Hesapla", command=OEE).grid(column=2, row=3, sticky=W)
ttk.Button(mainframe, text="İşletme Adam Başı Ciro Hesapla", command=ABC).grid(column=2, row=4, sticky=W)

for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

#root.bind('<Return>', hesapla)
root.mainloop()
