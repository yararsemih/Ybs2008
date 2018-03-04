from tkinter import *
from tkinter import ttk

def hesapla(*args):
    try:
        ciro = int(satisMiktar.get()) * int(bSatisFiyat.get())
        abc  = int(ciro) / int(calisanSayisi.get())
        state = round(float(abc),2)," Tl/Kişi "
        durum.set(state)
        
    except ValueError:
        pass
        
def main():
    
        global satisMiktar
        global bSatisFiyat
        global calisanSayisi 
        
        global durum
        
        root = Tk()
        root.title("İşletme Adam Başı Ciro Takip Programı")

        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)

        satisMiktar = StringVar()
        bSatisFiyat = StringVar()
        calisanSayisi = StringVar()
        
        durum = StringVar()

        satisMiktar_entry = ttk.Entry(mainframe, width=15, textvariable=satisMiktar)
        bSatisFiyat_entry = ttk.Entry(mainframe, width=10, textvariable=bSatisFiyat)
        calisanSayisi_entry = ttk.Entry(mainframe, width=10, textvariable=calisanSayisi)
        

        ttk.Label(mainframe, text="Satış Miktarı (adet/kutu) :").grid(column=1, row=1, sticky=W)
        satisMiktar_entry.grid(column=2, row=1, sticky=(W, E))

        ttk.Label(mainframe, text="Birim Satış Fiyatı (Tl): ").grid(column=1, row=2, sticky=W)
        bSatisFiyat_entry.grid(column=2, row=2, sticky=(W, E))

        
        ttk.Label(mainframe, text="İşletmede Çalışan Sayısı :").grid(column=1, row=3, sticky=W)
        calisanSayisi_entry.grid(column=2, row=3, sticky=(W, E))

       

        ttk.Button(mainframe, text="Hesapla", command=hesapla).grid(column=3, row=4, sticky=W)



        ttk.Label(mainframe, text="Sonuç :").grid(column=1, row=4, sticky=E)
        ttk.Label(mainframe, textvariable=durum).grid(column=2, row=4, sticky=(W, E))


        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        #gelir_entry.focus()
        #gider_entry.focus()
        root.bind('<Return>', hesapla)
        root.mainloop()
main()
