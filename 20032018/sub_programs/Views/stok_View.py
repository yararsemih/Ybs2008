#################################
#       İsletme Stok view       #
#################################

try:
    from tkinter import *
    from tkinter import ttk
    
except ImportError: 
    #for python 2.7+
    
    from Tkinter import *
    import ttk

    
class stok_View:

    def __init__(self,cal):
        self.status = {0:"Yetersiz Kar",1:"Kar Normal",2:"Kar Yüksek"}
        
        self.cal = cal
        self.main()
        
        
    def stkrequest(self):
        state = self.cal.calculate(db_k.get(), db_y.get(), db_d.get(),dsa_k.get(),dsa_y.get(),dsa_d.get(),dss_k.get(),dss_y.get(),dss_d.get() )

        dss_stok.set(state["dss_stok"])
        ort_stok.set(state["ort_stok"])

       
    def main(self):

        #db stok
        global db_k 
        global db_y
        global db_d

        #ds stok alım
        global dsa_k 
        global dsa_y
        global dsa_d

        #ds stok satım
        global dss_k 
        global dss_y
        global dss_d
       
        
        
        global dss_stok
        global ort_stok
        
        
        root = Tk()
        root.title("İşletme Stok Hesabı")

        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)

        db_k = IntVar()
        db_y = IntVar()
        db_d = IntVar()

        dsa_k = IntVar()
        dsa_y = IntVar()
        dsa_d = IntVar()

        dss_k = IntVar()
        dss_y = IntVar()
        dss_d = IntVar()

        
        dss_stok = StringVar()
        ort_stok = StringVar()
     
       
        db_k_entry = ttk.Entry(mainframe, width=10, textvariable=db_k)
        db_y_entry = ttk.Entry(mainframe, width=10, textvariable=db_y)
        db_d_entry = ttk.Entry(mainframe, width=10, textvariable=db_d)
        
        dsa_k_entry = ttk.Entry(mainframe, width=10, textvariable=dsa_k)
        dsa_y_entry = ttk.Entry(mainframe, width=10, textvariable=dsa_y)
        dsa_d_entry = ttk.Entry(mainframe, width=10, textvariable=dsa_d)

        dss_k_entry = ttk.Entry(mainframe, width=10, textvariable=dss_k)
        dss_y_entry = ttk.Entry(mainframe, width=10, textvariable=dss_y)
        dss_d_entry = ttk.Entry(mainframe, width=10, textvariable=dss_d)
        

        ttk.Label(mainframe, text="------------------------------").grid(column=1, row=1, sticky=(W,E))
        ttk.Label(mainframe, text="Dönem Başı Stok Değerleri").grid(column=2, row=1, sticky=(W,E))
        ttk.Label(mainframe, text="------------------------------").grid(column=3, row=1, sticky=(W,E))

        ttk.Label(mainframe, text="Koltuk Sayısı (Adet) ").grid(column=1, row=2, sticky=W)
        db_k_entry.grid(column=2, row=2, sticky=(W, E))
        
        ttk.Label(mainframe, text="Yatak Sayısı (Adet) ").grid(column=1, row=3, sticky=W)
        db_y_entry.grid(column=2, row=3, sticky=(W, E))

        ttk.Label(mainframe, text="Dolap Sayısı (Adet) ").grid(column=1, row=4, sticky=W)
        db_d_entry.grid(column=2, row=4, sticky=(W, E))

        ttk.Label(mainframe, text="------------------------------").grid(column=1, row=5, sticky=(W,E))
        ttk.Label(mainframe, text="Dönem İçi Stok Alımlar ").grid(column=2, row=5, sticky=(W,E))
        ttk.Label(mainframe, text="------------------------------").grid(column=3, row=5, sticky=(W,E))

        ttk.Label(mainframe, text="Koltuk Sayısı (Adet) ").grid(column=1, row=6, sticky=W)
        dsa_k_entry.grid(column=2, row=6, sticky=(W, E))

        ttk.Label(mainframe, text="Yatak Sayısı (Adet) ").grid(column=1, row=7, sticky=W)
        dsa_y_entry.grid(column=2, row=7, sticky=(W, E))

        ttk.Label(mainframe, text="Dolap Sayısı (Adet)  ").grid(column=1, row=8, sticky=W)
        dsa_d_entry.grid(column=2, row=8, sticky=(W, E))

        ttk.Label(mainframe, text="------------------------------").grid(column=1, row=9, sticky=(W,E))
        ttk.Label(mainframe, text="Dönem İçi Stok Satımlar ").grid(column=2, row=9, sticky=(W,E))
        ttk.Label(mainframe, text="------------------------------").grid(column=3, row=9, sticky=(W,E))

        ttk.Label(mainframe, text="Koltuk Sayısı (Adet) ").grid(column=1, row=10, sticky=W)
        dss_k_entry.grid(column=2, row=10, sticky=(W, E))

        ttk.Label(mainframe, text="Yatak Sayısı (Adet) ").grid(column=1, row=11, sticky=W)
        dss_y_entry.grid(column=2, row=11, sticky=(W, E))

        ttk.Label(mainframe, text="Dolap Sayısı (Adet) ").grid(column=1, row=12, sticky=W)
        dss_d_entry.grid(column=2, row=12, sticky=(W, E))

     
        ttk.Button(mainframe, text="Hesapla", command=self.stkrequest).grid(column=3, row=18, sticky=W)



        ttk.Label(mainframe, text="Dönem Sonu Stok Değerleri:").grid(column=1, row=18, sticky=E)
        ttk.Label(mainframe, textvariable=dss_stok).grid(column=2, row=18, sticky=(W, E))
        
        ttk.Label(mainframe, text="Ortalama Stoklar Değerleri :").grid(column=1, row=19, sticky=E)
        ttk.Label(mainframe, textvariable=ort_stok).grid(column=2, row=19, sticky=(W, E))

       
        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        
        root.bind('<Return>', self.stkrequest)
        root.mainloop()
