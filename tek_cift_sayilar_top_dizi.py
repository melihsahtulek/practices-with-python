#######################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#                   TEK VE ÇİFT                       #
#                 SAYILAR TOPLAMI                     #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#######################################################
import random

def randSayi(hane):
    randDizi = []
    for i in range(hane):
        randDizi.append(random.randint(1, 99))
    return randDizi


print('OLUŞTURULAN DİZİ...:',randSayi(10))


def hesapla(dizi):
    tekTop = 0
    ciftTop = 0
    for j in range(dizi.__len__()):
        if dizi[j] % 2 == 0:
            ciftTop = ciftTop + dizi[j]
        else:
            tekTop = tekTop + dizi[j]
    print('Tek Sayılar Toplamı...:', tekTop)
    print('Çift Sayılar Toplamı...:' , ciftTop)


hesapla(randSayi(10))