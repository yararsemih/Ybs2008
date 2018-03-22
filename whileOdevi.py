def bir():
    sm = 500
    sf = 20
    ciro = 5000

    counter = 0
    while (ciro <= 500000):
        ciro = ciro+(sm*sf)
        sm = sm+200
        sf = sf+10    
        counter = counter+1

    yil =counter/12
    print("Şirketin Cirosu, 500 bin Tl yi ",counter," ay (yani ",round(yil,2)," yıl)","sonra geçer")

def iki():
    stok = 10000
    counter = 0
    while(stok > 0):
        #her ay...
        stok = (stok-500)+100
        counter = counter +1
    print("İşletme Stokları ",counter," ay sonra sıfırlanır. Yani",counter+1,". ayda")

def uc():
    print("3 bölümünden kalan sayıların Toplamı")
    kalanlar = 0
    
    while True:
        sayi = int(input("Sayı Giriniz : "))
        if(sayi > 0 ):
            kalanlar = kalanlar+(sayi%3)
            print("Girilen Sayıların 3 ile bölümünden kalanların toplamı =",kalanlar)
        else:
            break
        
    print("Girilen Sayıların 3 ile bölümünden kalanların toplamı =",kalanlar)

def dort():
    calisanSayi = 50
    haftalikCs = 40
    ekYevmiye = 0.10
    maksAylikCs = 22
    gYevmiye = 90
    

    while True:
        haftalikCalisilanSure =int(input("Haftalık Mesai Saati (tamsayı giriniz) :"))
        if ( (haftalikCalisilanSure-haftalikCs)*4 < maksAylikCs ):
            if(haftalikCalisilanSure <= haftalikCs):
                maas = (haftalikCalisilanSure*4)*gYevmiye
                
            elif(haftalikCalisilanSure > haftalikCs):
                ek_maas = (haftalikCalisilanSure-haftalikCs)*(gYevmiye*ekYevmiye)
                maas = (haftalikCs*gYevmiye)*4+(ek_maas*4)
                
            print("Maas =",maas)
            
        else:
            print("Hata!! Aylık ekstra çalısma süresi ",maksAylikCs," den fazla olamaz!")
            break


def bes():
    uretim = 200
    defoluMaksOran = 0.20
    birikimlidefolu = 0
    counter = 0
    while(birikimlidefolu < (uretim*defoluMaksOran)):
        defolu = int(input("Defolu mal sayısı giriniz :"))
        birikimlidefolu = birikimlidefolu + defolu
        counter= counter+1
        
        print(counter," Gün sonundaki Defolu Ürün Sayınız :",birikimlidefolu,"\n")
        
    print("Toplam Defolu Ürün Sayınız, üretim Miktarının %",defoluMaksOran," 'den fazla olamaz!")
        
    
        
    

        
while True:
    state  = int(input("Ödev Numarası Giriniz (1-5):"))  
    try:
        if(state == 1):
            bir()
        elif(state == 2):
            iki()
        elif(state == 3 ):
            uc()
        elif(state == 4 ):
            dort()
        elif(state == 5 ):
            bes()
    except  KeyboardInterrupt:
        exit()  
