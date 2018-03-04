from tkinter import *
from tkinter import ttk

global karEsigi
karEsigi = 1000

def hesapla(*args):
    try:
        gelir = int(fGelir.get()) + int(pGelir.get())+ int(kGelir.get())
        gider = int(uGider.get()) + int(fGider.get())+ int(pGider.get()) + int(kGider.get()) + int(mGider.get())

        calculate = gelir-gider

        if (calculate > karEsigi):
            state = calculate," Karlı"
            durum.set(state)
        elif (calculate == karEsigi):
            state = calculate," Başabaş"
            durum.set(state)
        else:
            state = calculate,"Zarar ziyansınız vallahi"
            durum.set(state)
        
    except ValueError:
        pass
        
def main():
        global fGelir
        global pGelir
        global kGelir

        global uGider 
        global fGider 
        global pGider 
        global kGider 
        global mGider 

        global durum
        
        root = Tk()
        root.title("İşletme Kar Takip Programı")

        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)

        fGelir = StringVar()
        pGelir = StringVar()
        kGelir = StringVar()

        uGider = StringVar()
        fGider = StringVar()
        pGider = StringVar()
        kGider = StringVar()
        mGider = StringVar()

        durum = StringVar()

        fGelir_entry = ttk.Entry(mainframe, width=10, textvariable=fGelir)
        pGelir_entry = ttk.Entry(mainframe, width=10, textvariable=pGelir)
        kGelir_entry = ttk.Entry(mainframe, width=10, textvariable=kGelir)

        #Giderler

        uGider_entry = ttk.Entry(mainframe, width=10, textvariable=uGider)
        fGider_entry = ttk.Entry(mainframe, width=10, textvariable=fGider)
        pGider_entry = ttk.Entry(mainframe, width=10, textvariable=pGider)
        kGider_entry = ttk.Entry(mainframe, width=10, textvariable=kGider)
        mGider_entry = ttk.Entry(mainframe, width=10, textvariable=mGider)

        ttk.Label(mainframe, text="Finansman Geliri ").grid(column=1, row=1, sticky=W)
        fGelir_entry.grid(column=2, row=1, sticky=(W, E))

        ttk.Label(mainframe, text="Pazar Geliri ").grid(column=1, row=2, sticky=W)
        pGelir_entry.grid(column=2, row=2, sticky=(W, E))

        ttk.Label(mainframe, text="Kira Geliri ").grid(column=1, row=3, sticky=W)
        kGelir_entry.grid(column=2, row=3, sticky=(W, E))

        ttk.Label(mainframe, text="--------------------Giderler---------------").grid(column=2, row=4, sticky=W)

        #Giderler
        ttk.Label(mainframe, text="Ücret Gideri ").grid(column=1, row=5, sticky=W)
        uGider_entry.grid(column=2, row=5, sticky=(W, E))

        ttk.Label(mainframe, text="Finansman Gideri ").grid(column=1, row=6, sticky=W)
        fGider_entry.grid(column=2, row=6, sticky=(W, E))

        ttk.Label(mainframe, text="Pazar Gideri ").grid(column=1, row=7, sticky=W)
        pGider_entry.grid(column=2, row=7, sticky=(W, E))

        ttk.Label(mainframe, text="Kira Gideri ").grid(column=1, row=8, sticky=W)
        kGider_entry.grid(column=2, row=8, sticky=(W, E))

        ttk.Label(mainframe, text="Muhasebe Gideri ").grid(column=1, row=9, sticky=W)
        mGider_entry.grid(column=2, row=9, sticky=(W, E))


       


        ttk.Button(mainframe, text="Hesapla", command=hesapla).grid(column=3, row=12, sticky=W)



        ttk.Label(mainframe, text="Durum :").grid(column=1, row=12, sticky=E)
        ttk.Label(mainframe, textvariable=durum).grid(column=2, row=12, sticky=(W, E))


        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        #gelir_entry.focus()
        #gider_entry.focus()
        root.bind('<Return>', hesapla)
        root.mainloop()
main()
