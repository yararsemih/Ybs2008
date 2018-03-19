#################################
#   #Katma değer ciro view       #
#################################

try:
    from tkinter import *
    from tkinter import ttk
    
except ImportError: 
    #for python 2.7+
    
    from Tkinter import *
    import ttk

    
class kdc_View:

    def __init__(self,ik):
        self.status = {0:"Katma Değer Ciro Yerlerde!",1:"Katma Değer Ciro Normal",2:"Katma Değer Ciro Yüksek"}

        self.ik = ik
        self.main()
        
        
    def request(self):
        state = self.ik.calculate(tsm.get(), hmm.get(), bog.get(), sg.get(), sahg.get() )
        
        if(state is not None):
            state=str(state[0])+" TL "+self.status[state[1]]
            durum.set(state)
        
    def main(self):
        global tsm #total satış miktar +
        
        global hmm #ham madde maliyet -
        global bog # bakım onarım girder -
        global sg #sevkiyat gideri - 
        global sahg #satınalınan hizmet gider -
        

        global durum

        
        root = Tk()
        root.title("Katma Değer Ciro Hesabı")

        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)

        tsm = IntVar()
        
        hmm = IntVar()
        bog = IntVar()
        sg = IntVar()
        sahg = IntVar()

        durum = StringVar()

        #gelir
        tsm_entry = ttk.Entry(mainframe, width=10, textvariable=tsm)
        
        #Giderler
        hmm_entry = ttk.Entry(mainframe, width=10, textvariable=hmm)
        bog_entry = ttk.Entry(mainframe, width=10, textvariable=bog)
        sg_entry = ttk.Entry(mainframe, width=10, textvariable=sg)
        sahg_entry = ttk.Entry(mainframe, width=10, textvariable=sahg)

        #gelir Labels
        ttk.Label(mainframe, text="Toplam Satış Miktarı ").grid(column=1, row=1, sticky=W)
        tsm_entry.grid(column=2, row=1, sticky=(W, E))

       

        ttk.Label(mainframe, text="------------------------------").grid(column=1, row=2, sticky=(W,E))
        ttk.Label(mainframe, text="Gider/Maliyetler").grid(column=2, row=2, sticky=(W,E))
        ttk.Label(mainframe, text="------------------------------").grid(column=3, row=2, sticky=(W,E))

        #gider Labels
       
        ttk.Label(mainframe, text="Hammadde Maliyeti ").grid(column=1, row=3, sticky=W)
        hmm_entry.grid(column=2, row=3, sticky=(W, E))
        
        ttk.Label(mainframe, text="Bakım Onarım Giderleri ").grid(column=1, row=4, sticky=W)
        bog_entry.grid(column=2, row=4, sticky=(W, E))

        ttk.Label(mainframe, text="Sevkiyat Giderleri ").grid(column=1, row=5, sticky=W)
        sg_entry.grid(column=2, row=5, sticky=(W, E))

        ttk.Label(mainframe, text="Satın Alınan Hizmet Giderleri ").grid(column=1, row=6, sticky=W)
        sahg_entry.grid(column=2, row=6, sticky=(W, E))

       


        ttk.Button(mainframe, text="Hesapla", command=self.request).grid(column=3, row=7, sticky=W)



        ttk.Label(mainframe, text="Durum :").grid(column=1, row=7, sticky=E)
        ttk.Label(mainframe, textvariable=durum).grid(column=2, row=7, sticky=(W, E))


        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        
        root.bind('<Return>', self.request)
        root.mainloop()
