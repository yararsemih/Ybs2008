class stok_Controller:
    def __init__(self):
        global stok_k
        global stok_y
        global stok_d

        

        global ort_k
        global ort_y
        global ort_d
        
    def calculate(self,db_k,db_y,db_d,dsa_k,dsa_y,dsa_d,dss_k,dss_y,dss_d):
        self.stok_k =  db_k
        self.stok_y =  db_y
        self.stok_d =  db_d

        print(self.stok_k)
        
        self.artma(dsa_k,dsa_y,dsa_d)
        self.azaltma(dss_k,dss_y,dss_d)
        self.ort(db_k,db_y,db_d)

        dss_stok = "Koltuk:",self.stok_k,"\n","Yatak",self.stok_y,"\n","Dolap",self.stok_d
        ort_stok = "Koltuk:",self.ort_k,"\n","Yatak",self.ort_y,"\n","Dolap",self.ort_d
        result ={
            "dss_stok":dss_stok,
            "ort_stok":ort_stok
            }
        return result

    def artma(self,dsa_k,dsa_y,dsa_d):
        self.stok_k =self.stok_k + dsa_k
        self.stok_y = self.stok_y+dsa_y
        self.stok_d = self.stok_d+dsa_d
        
    def azaltma(self,dss_k,dss_y,dss_d):
        self.stok_k = self.stok_k - dss_k
        self.stok_y = self.stok_y - dss_y
        self.stok_d = self.stok_d - dss_d

    def ort(self,db_k,db_y,db_d):
        self.ort_k = (db_k + self.stok_k)/2
        self.ort_y = (db_y + self.stok_y)/2
        self.ort_d = (db_d + self.stok_d)/2
        
        

    
