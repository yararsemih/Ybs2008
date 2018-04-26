#main program
#runs on python 3.6.5

from moduls.isletme import *
from moduls.SM_Analiz import SM_Analiz as smanaliz

def isletmeKar_main():
    text1 = "Gelir Giriniz :"
    text2 = "Gider Giriniz :"
    result = isletme.karHesabi(text1,text2)

    if(result > 0):
        print(result," TL Kar")
    elif(result == 0):
        print(result," TL Başabaş")
    else:
        print(result," TL Zarar")

def isletmeABC_main():
    t1 = "Toplam Ciro Giriniz :"
    t2 = "Toplam Çalışan Sayısı Giriniz :"
    result = isletme.abCiro(t1,t2)

    print("Adam Başı Ciro : ",result)

def bilanco_main():
    entity = {
        "aktif":{
            "1 donen varlıklar":{
                "100 Kasa" :20000,
                "101 alınan cek" :10000,
                "102 Bankalar" :5000,
                "121 alacak senet" :28000,
                "153 ticari mal" :65000
            },

            "2 duran varlıklar":{
                "252 Binalar" :150000,
                "254 Taşıtlar" :25000,
                "255 Demirbaşlar" :8000   
            }
        },

        "pasif":{
            "3 kvyk":{
                "300 Banka Kredileri": 42000,
                "320 Satıcılar": 60000
                },
            "4 uvyk":{
                "400 Banka Kredileri": 35000,
                "421 Borç Senetleri": 115000
                },
            "5 özkaynaklar":{
                "500 Sermaye Hesabı": 59000
                }
          }
        }

    bilanco_modul= bilanco(entity)
    rslt = bilanco_modul.hesapla("aktif","pasif") # karsılaştırma için başlık seç
    bilanco_modul.show()

    print("________________________SONUÇ________________________________")
    if(rslt is True):
        print("Bilanço doğru hesaplanmıştır")
    else:
        print("Bilanço yanlış hesaplanmıştır")

def etkilesim_main():
    entity = {
                "YBS1":{
                        "Like": 365000,
                        "Comment":65000,
                        "Share":870,
                        "Content":500,
                        "Follower":1125000
                    },
                "YBS2":{
                        "Like": 450000,
                        "Comment":25000,
                        "Share":380,
                        "Content":100,
                        "Follower":1450000
                    },
                "YBS3":{
                        "Like": 582000,
                        "Comment":52000,
                        "Share":1200,
                        "Content":650,
                        "Follower":2000000
                    }
        }
    smanaliz_modul = smanaliz(entity)
    rslt = smanaliz_modul.rslt

    for x in rslt:
        if (rslt[x] >= 0.20):
            print(x," Etkileşim oranı : ",rslt[x]," Başarılı :)")
        else:
            print(x," Etkileşim oranı : ",rslt[x]," Başarısız :/")

while True:
    print("27Nisan 2018 Son Teslimli YBS2008 Modüller Ödevi \n İşletme Karı İçin 1 \n İşletme Adam Başı Ciro İçin 2 \n Bilanço İçin 3 \n Etkileşim Oranı İçin 4 \n Çıkmak için 0  Tuşlayınız")
    num = int(input("Ödev Numarası Giriniz : "))

    if( num == 1):
        isletmeKar_main()
    elif(num == 2):
        isletmeABC_main()
    elif(num == 3):
        bilanco_main()
    elif(num == 4):
        etkilesim_main()
    elif(num == 0):
        exit()
