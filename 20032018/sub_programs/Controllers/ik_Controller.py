class ik_Controller:
    def __init__(self):
        pass
        
    def calculate(self,liste):
        fs_profit = self.ikCalculate( liste["fs_gelir"],liste["fs_gider"] )
        ls_profit = self.ikCalculate( liste["ls_gelir"],liste["ls_gider"] )

        total_profit = ls_profit - fs_profit

        if(total_profit > 5000):
            total_profit = [total_profit,2]
        elif(total_profit > 1000 and profit < 5000):
            total_profit = [total_profit,1]
        elif(total_profit < 1000):
            total_profit = [total_profit,0]

        return {"fs_profit":fs_profit,"ls_profit":ls_profit,"total_profit":total_profit}
        
    def ikCalculate(self,gelir,gider):
        gelirs = 0
        giders = 0
        
        for x in gelir:
            gelirs = gelirs+x
        for y in gider:
            giders = giders+y

        profit = gelirs - giders
        return profit
        
