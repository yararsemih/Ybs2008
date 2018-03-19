#################################
#   musteri calsima süresi view #
#################################

try:
    from tkinter import *
    from tkinter import ttk
    
except ImportError: 
    #for python 2.7+
    
    from Tkinter import *
    import ttk

    
class msc_View:

    def __init__(self,cal):
        self.status = {0:"Katma Değer Ciro Yerlerde!",1:"Katma Değer Ciro Normal",2:"Katma Değer Ciro Yüksek"}
        
        self.cal = cal
        self.main()
        
        
    def mscrequest(self):
        state = self.cal.calculate({'last':[lastCs.get(),lastMs.get()],'current':[CurrentCs.get(),CurrentMs.get()]} )
        lastMCS.set(state["lastMCS"])
        currentMCS.set(state["currentMCS"])
        farkMCS.set(state["farkMCS"])
       
    def main(self):
        global lastCs #gecen yıl calısılan sure
        global lastMs #gecen yıl musteri sayisi
        
        global CurrentCs # simdiki yıl calısılan sure
        global CurrentMs # simdiki yıl musteri sayı 
        
        

        global lastMCS
        global currentMCS
        global farkMCS

        
        root = Tk()
        root.title("Müşterilerle Çalışma Süresi Hesabı")

        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)

        lastCs = IntVar()
        lastMs = IntVar()
        
        CurrentCs = IntVar()
        CurrentMs = IntVar()

        lastMCS = StringVar()
        currentMCS = StringVar()
        farkMCS = StringVar()

        #last
        lastCs_entry = ttk.Entry(mainframe, width=10, textvariable=lastCs)
        lastMs_entry = ttk.Entry(mainframe, width=10, textvariable=lastMs)

        #Current
        CurrentCs_entry = ttk.Entry(mainframe, width=10, textvariable=CurrentCs)
        CurrentMs_entry = ttk.Entry(mainframe, width=10, textvariable=CurrentMs)
        

        #gelir Labels
        ttk.Label(mainframe, text="Bir Önceki Yıl Çalışılan Süre (Saat) ").grid(column=1, row=1, sticky=W)
        lastCs_entry.grid(column=2, row=1, sticky=(W, E))
        
        ttk.Label(mainframe, text="Bir Önceki Yıl Müşteri Sayısı ").grid(column=1, row=2, sticky=W)
        lastMs_entry.grid(column=2, row=2, sticky=(W, E))

       

        ttk.Label(mainframe, text="------------------------------").grid(column=1, row=3, sticky=(W,E))
        ttk.Label(mainframe, text="Baz Yıl Verileri").grid(column=2, row=3, sticky=(W,E))
        ttk.Label(mainframe, text="------------------------------").grid(column=3, row=3, sticky=(W,E))

        #gider Labels
       
        ttk.Label(mainframe, text="Baz Yıl Çalışılan Süre (Saat) ").grid(column=1, row=4, sticky=W)
        CurrentCs_entry.grid(column=2, row=4, sticky=(W, E))
        
        ttk.Label(mainframe, text="Baz Yıl Müşteri Sayısı ").grid(column=1, row=5, sticky=W)
        CurrentMs_entry.grid(column=2, row=5, sticky=(W, E))


       


        ttk.Button(mainframe, text="Hesapla", command=self.mscrequest).grid(column=3, row=6, sticky=W)



        ttk.Label(mainframe, text="Bir Önceki Yılda ki Müşterilerle Çalışma Süresi :").grid(column=1, row=6, sticky=E)
        ttk.Label(mainframe, textvariable=lastMCS).grid(column=2, row=6, sticky=(W, E))
        
        ttk.Label(mainframe, text="Baz Yıl Müşterilerle Çalışma Süresi :").grid(column=1, row=7, sticky=E)
        ttk.Label(mainframe, textvariable=currentMCS).grid(column=2, row=7, sticky=(W, E))

        
        ttk.Label(mainframe, text="Yıllar Arası Fark Müşterilerle Çalışma Süresi :").grid(column=1, row=8, sticky=E)
        ttk.Label(mainframe, textvariable=farkMCS).grid(column=2, row=8, sticky=(W, E))

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        
        root.bind('<Return>', self.mscrequest)
        root.mainloop()
