try:
    from tkinter import *
    from tkinter import ttk
    
except ImportError: 
    #for python 2.7+
    
    from Tkinter import *
    import ttk

import subprocess
import sys



class mainCont:
    def KDC(self):
         subprocess.check_call([sys.executable, 'sub_programs/KDC.py'])
         
    def CalismaSuresi(self):
        subprocess.check_call([sys.executable, 'sub_programs/MSC.py'])

    def ik(self):
        subprocess.check_call([sys.executable, 'sub_programs/ik.py'])

    def StokTakip(self):
        subprocess.check_call([sys.executable, 'sub_programs/stok.py'])

    def __init__(self):
        root = Tk()
        root.title("İşletme Takip Programı")

        mainframe = ttk.Frame(root, padding="3 3 120 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        
        ttk.Button(mainframe, text="Katma Değer Ciro Hesapla", command=self.KDC).grid(column=2, row=2, sticky=W)
        ttk.Button(mainframe, text="Yıllara Göre Çalışma Süresi Karşılaştır", command=self.CalismaSuresi).grid(column=2, row=3, sticky=W)
        ttk.Button(mainframe, text="İşletme Kar Hesap&Karşılaştırma", command=self.ik).grid(column=2, row=4, sticky=W)
        ttk.Button(mainframe, text="Stok Takip", command=self.StokTakip).grid(column=2, row=5, sticky=W)

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        root.mainloop()

mainCont()
