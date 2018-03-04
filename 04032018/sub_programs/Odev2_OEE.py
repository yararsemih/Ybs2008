from tkinter import *
from tkinter import ttk

def hesapla(*args):
    try:
        usability = (float(puSuresi.get()) - float(upDurus.get()) ) / float(puSuresi.get())
        performans = ( float(scSuresi.get()) * int(uMiktar.get()) ) / ( float(puSuresi.get()) - float(upDurus.get()) )
        kalite = int(suMiktar.get()) / int(uMiktar.get())

        OEE = usability * performans * kalite
        oee = round(OEE,2)                           
        state = "Ekipman Etkinlik Oranı : %",oee
        durum.set(state)
        
    except ValueError:
        pass
        
def main():
    
        global puSuresi
        global upDurus
        global scSuresi
        global uMiktar 
        global suMiktar 
        
        global durum
        
        root = Tk()
        root.title("İşletme OEE Takip Programı")

        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)

        puSuresi = StringVar()
        upDurus = StringVar()
        scSuresi = StringVar()
        uMiktar = StringVar()
        suMiktar = StringVar()
        
        durum = StringVar()

        puSuresi_entry = ttk.Entry(mainframe, width=10, textvariable=puSuresi)
        upDurus_entry = ttk.Entry(mainframe, width=10, textvariable=upDurus)
        scSuresi_entry = ttk.Entry(mainframe, width=10, textvariable=scSuresi)
        uMiktar_entry = ttk.Entry(mainframe, width=10, textvariable=uMiktar)
        suMiktar_entry = ttk.Entry(mainframe, width=10, textvariable=suMiktar)

        #durum_entry = ttk.Entry(mainframe, width=10, textvariable=durum)

        ttk.Label(mainframe, text="Planlanmış Üretim Süresi ").grid(column=1, row=1, sticky=W)
        puSuresi_entry.grid(column=2, row=1, sticky=(W, E))

        ttk.Label(mainframe, text="Planlanmamış Durma Süresi ").grid(column=1, row=2, sticky=W)
        upDurus_entry.grid(column=2, row=2, sticky=(W, E))

        ttk.Label(mainframe, text="Standart Çevrim Süresi ").grid(column=1, row=3, sticky=W)
        scSuresi_entry.grid(column=2, row=3, sticky=(W, E))

        ttk.Label(mainframe, text="Ürün Miktarı ").grid(column=1, row=4, sticky=W)
        uMiktar_entry.grid(column=2, row=4, sticky=(W, E))

        ttk.Label(mainframe, text="Sağlam Ürün Miktarı ").grid(column=1, row=5, sticky=W)
        suMiktar_entry.grid(column=2, row=5, sticky=(W, E))
       


        ttk.Button(mainframe, text="Hesapla", command=hesapla).grid(column=3, row=6, sticky=W)



        ttk.Label(mainframe, text="Sonuç :").grid(column=1, row=6, sticky=E)
        ttk.Label(mainframe, textvariable=durum).grid(column=2, row=6, sticky=(W, E))


        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        #gelir_entry.focus()
        #gider_entry.focus()
        root.bind('<Return>', hesapla)
        root.mainloop()
main()
