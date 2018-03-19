class kdc_Controller:
    def __init__(self):
        self.kdcUst_esik = 1000
        self.kdcAlt_esik = 500

        
    def calculate(self,tsm, hmm, bog, sg, sahg):
        result = tsm-(hmm+bog+sg+sahg)

         # 0,zarar ; 1,between alt-ust ; 2,kar
        if(result < self.kdcAlt_esik):
            return [result,0]
        elif(result >= self.kdcAlt_esik and result < self.kdcUst_esik):
            return [result,1]
        elif(result >= self.kdcUst_esik):
            return [result,2]
