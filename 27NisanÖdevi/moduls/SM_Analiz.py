class SM_Analiz:
    def __init__(self,entity):
        self.common = entity
        self.rslt = {} 

        for x in self.common:
            self.rslt[x] = 0
            
        self.hesapla()
             
    def hesapla(self):
        for x in self.common:
            result = (((self.common[x]["Like"] + self.common[x]["Comment"] + self.common[x]["Share"])/self.common[x]["Content"])/self.common[x]["Follower"])*100
            self.rslt[x] += round(result,2)
