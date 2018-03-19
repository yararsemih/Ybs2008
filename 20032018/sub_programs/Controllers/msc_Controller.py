class msc_Controller:
    def __init__(self):
        global lastMCS
        global currentMCS
        
    def calculate(self,liste):
        lastCs = liste["last"][0] # gecen yıl calısılan sure
        lastMs = liste["last"][1] # gecen yıl musteri sayi

        lastMCS = self.mcsCalculate(lastCs,lastMs)

        currentCs = liste["current"][0] #baz yıl calısılan sure
        currentMs = liste["current"][1] #baz yıl musteri sayi

        currentMCS =  self.mcsCalculate(currentCs,currentMs)

        farkMCS = currentMCS - lastMCS

        return {"lastMCS":lastMCS,"currentMCS":currentMCS,"farkMCS":farkMCS}

    def mcsCalculate(self,Cs,Ms):
        if(Ms == 0):
            Ms = 1
        result = Cs / Ms
        return result
