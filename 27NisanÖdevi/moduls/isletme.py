#isletme modulu
class isletme:
    def karHesabi(text1,text2):
        gelir = int(input(text1))
        gider = int(input(text2))

        result = gelir-gider
        return result
    
    def abCiro(t1,t2): #adam bası ciro
         tc = int(input(t1))
         tcs = int(input(t2))

         result = tc/tcs
         return result

class bilanco:
    def __init__(self,entity): # entity is a dictionary or json data
        
        self.common = {}

        for x in entity:
            self.common[x] = 0
            for y in entity[x]:
                self.common[y] = 0
                for z in entity[x][y]:
                    if(len(entity[x])<3):
                        #print( entity[x][y][z])
                       
                        self.common[y] += entity[x][y][z]
                        self.common[x] += entity[x][y][z]
                    elif(len(entity[x])>=3):
                        #print( entity[x][y][z])    
            
                        self.common[y] += entity[x][y][z]
                        self.common[x] += entity[x][y][z]


    def hesapla(self,active,passive):
        if(self.common[active] == self.common[passive] ): #true
            return True
        else:
            return False

    def show(self):
        rslt = self.common
        for x  in rslt:
            print(x," = ",rslt[x])
         
        
