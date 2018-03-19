#################################
#       İsletme Kar view        #
#################################

try:
    from tkinter import *
    from tkinter import ttk
    
except ImportError: 
    #for python 2.7+
    
    from Tkinter import *
    import ttk

    
class ik_View:

    def __init__(self,cal):
        self.status = {0:"Yetersiz Kar",1:"Kar Normal",2:"Kar Yüksek"}
        
        self.cal = cal
        self.main()
        
        
    def ikrequest(self):
        state = self.cal.calculate({'fs_gelir':[f_yg.get(),f_fg.get(), f_usg.get()],'fs_gider':[f_cm.get(),f_kg.get(), f_dm.get()],'ls_gelir':[l_yg.get(),l_sg.get(), l_etg.get(),l_usg.get()],'ls_gider':[l_cm.get(),l_kg.get(), l_bm.get()]} )

        fs_profit.set(state["fs_profit"])
        ls_profit.set(state["ls_profit"])

        tp = state["total_profit"][0],self.status[state["total_profit"][1]]
        total_profit.set(tp)
       
    def main(self):

        #first 6 gelir
        global f_yg 
        global f_fg
        global f_usg

        #first 6 gider
        global f_cm 
        global f_kg
        global f_dm

        #----------------------------------------#
        
        #first 6 gelir
        global l_yg 
        global l_sg
        global l_etg
        global l_usg

        #last 6 gider
        global l_cm 
        global l_kg
        global l_bm
        
        global fs_profit 
        global ls_profit
        global total_profit
        
        
        root = Tk()
        root.title("İşletme Kar Hesabı")

        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)

        f_yg = IntVar()
        f_fg = IntVar()
        f_usg = IntVar()

        f_cm = IntVar()
        f_kg = IntVar()
        f_dm = IntVar()

        l_yg = IntVar()
        l_sg = IntVar()
        l_etg = IntVar()
        l_usg = IntVar()

        l_cm = IntVar()
        l_kg = IntVar()
        l_bm = IntVar()
        
        fs_profit = StringVar()
        ls_profit = StringVar()
        total_profit = StringVar()
        
       

        #first 6
        f_yg_entry = ttk.Entry(mainframe, width=10, textvariable=f_yg)
        f_fg_entry = ttk.Entry(mainframe, width=10, textvariable=f_fg)
        f_usg_entry = ttk.Entry(mainframe, width=10, textvariable=f_usg)
        
        f_cm_entry = ttk.Entry(mainframe, width=10, textvariable=f_cm)
        f_kg_entry = ttk.Entry(mainframe, width=10, textvariable=f_kg)
        f_dm_entry = ttk.Entry(mainframe, width=10, textvariable=f_dm)

        #last6
        l_yg_entry = ttk.Entry(mainframe, width=10, textvariable=l_yg)
        l_sg_entry = ttk.Entry(mainframe, width=10, textvariable=l_sg)
        l_etg_entry = ttk.Entry(mainframe, width=10, textvariable=l_etg)
        l_usg_entry = ttk.Entry(mainframe, width=10, textvariable=l_usg)
        
        l_cm_entry = ttk.Entry(mainframe, width=10, textvariable=l_cm)
        l_kg_entry = ttk.Entry(mainframe, width=10, textvariable=l_kg)
        l_bm_entry = ttk.Entry(mainframe, width=10, textvariable=l_bm)
        
        #gelir Labels

        ttk.Label(mainframe, text="------------------------------").grid(column=1, row=1, sticky=(W,E))
        ttk.Label(mainframe, text="İlk 6 Ay Gelir").grid(column=2, row=1, sticky=(W,E))
        ttk.Label(mainframe, text="------------------------------").grid(column=3, row=1, sticky=(W,E))

        ttk.Label(mainframe, text="Yazılım Geliri Tl ").grid(column=1, row=2, sticky=W)
        f_yg_entry.grid(column=2, row=2, sticky=(W, E))
        
        ttk.Label(mainframe, text="Finansman Geliri Tl ").grid(column=1, row=3, sticky=W)
        f_fg_entry.grid(column=2, row=3, sticky=(W, E))

        ttk.Label(mainframe, text="Ürün Satış Geliri ").grid(column=1, row=4, sticky=W)
        f_usg_entry.grid(column=2, row=4, sticky=(W, E))

        ttk.Label(mainframe, text="------------------------------").grid(column=1, row=5, sticky=(W,E))
        ttk.Label(mainframe, text="İlk 6 Ay Gider ").grid(column=2, row=5, sticky=(W,E))
        ttk.Label(mainframe, text="------------------------------").grid(column=3, row=5, sticky=(W,E))

        ttk.Label(mainframe, text="Çalışan Maaşları Tl (Toplam) ").grid(column=1, row=6, sticky=W)
        f_cm_entry.grid(column=2, row=6, sticky=(W, E))

        ttk.Label(mainframe, text="Kira Gideri Tl ").grid(column=1, row=7, sticky=W)
        f_kg_entry.grid(column=2, row=7, sticky=(W, E))

        ttk.Label(mainframe, text="Donanım Maliyeti Tl  ").grid(column=1, row=8, sticky=W)
        f_dm_entry.grid(column=2, row=8, sticky=(W, E))

        ttk.Label(mainframe, text="------------------------------").grid(column=1, row=9, sticky=(W,E))
        ttk.Label(mainframe, text="Son 6 Ay Gelirler ").grid(column=2, row=9, sticky=(W,E))
        ttk.Label(mainframe, text="------------------------------").grid(column=3, row=9, sticky=(W,E))

        ttk.Label(mainframe, text="Yazılım Geliri ").grid(column=1, row=10, sticky=W)
        l_yg_entry.grid(column=2, row=10, sticky=(W, E))

        ttk.Label(mainframe, text="Sponsorluk Geliri ").grid(column=1, row=11, sticky=W)
        l_sg_entry.grid(column=2, row=11, sticky=(W, E))

        ttk.Label(mainframe, text="E Ticaret Geliri ").grid(column=1, row=12, sticky=W)
        l_etg_entry.grid(column=2, row=12, sticky=(W, E))

        ttk.Label(mainframe, text="Ürün Satış Geliri ").grid(column=1, row=13, sticky=W)
        l_usg_entry.grid(column=2, row=13, sticky=(W, E))

        ttk.Label(mainframe, text="------------------------------").grid(column=1, row=14, sticky=(W,E))
        ttk.Label(mainframe, text="Son 6 Ay Giderler ").grid(column=2, row=14, sticky=(W,E))
        ttk.Label(mainframe, text="------------------------------").grid(column=3, row=14, sticky=(W,E))

        ttk.Label(mainframe, text="Çalışan Maaşları Tl (Toplam) ").grid(column=1, row=15, sticky=W)
        l_cm_entry.grid(column=2, row=15, sticky=(W, E))

        ttk.Label(mainframe, text="Kira Gideri Tl ").grid(column=1, row=16, sticky=W)
        l_kg_entry.grid(column=2, row=16, sticky=(W, E))

        ttk.Label(mainframe, text="Bakım Gideri Tl ").grid(column=1, row=17, sticky=W)
        l_bm_entry.grid(column=2, row=17, sticky=(W, E))       


        ttk.Button(mainframe, text="Hesapla", command=self.ikrequest).grid(column=3, row=18, sticky=W)



        ttk.Label(mainframe, text="İlk 6 Aylık  Kar Tl:").grid(column=1, row=18, sticky=E)
        ttk.Label(mainframe, textvariable=fs_profit).grid(column=2, row=18, sticky=(W, E))
        
        ttk.Label(mainframe, text="Son 6 Aylık  Kar Tl :").grid(column=1, row=19, sticky=E)
        ttk.Label(mainframe, textvariable=ls_profit).grid(column=2, row=19, sticky=(W, E))

        ttk.Label(mainframe, text="Dönemler Arası Kar Farkı Tl :").grid(column=1, row=20, sticky=E)
        ttk.Label(mainframe, textvariable=total_profit).grid(column=2, row=20, sticky=(W, E))

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        
        root.bind('<Return>', self.ikrequest)
        root.mainloop()
