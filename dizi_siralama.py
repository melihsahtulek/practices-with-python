#######################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#                   RANDOM SAYI DİZİSİNİ              #
#                         SIRALAMA                    #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#######################################################
import random
uzunluk = int(input('ELEMAN SAYISI GİRİNİZ...:'))
dizi = []
for k in range(uzunluk):
    dizi.append(random.randint(0,100))
print('RASTGELE SEÇİLEN SAYI DİZİSİ...:', dizi)
siraliDizi = []
enBuyuk = 1
while(True):
    for i in range(dizi.__len__()):
        if dizi[i] < enBuyuk:
            pass
        else:
            enBuyuk = dizi[i]
    dizi.remove(enBuyuk)
    siraliDizi.append(enBuyuk)
    enBuyuk = 1
    if dizi.__len__() == 1:
        x = dizi[0]
        siraliDizi.append(x)
    if siraliDizi.__len__() == uzunluk:
        break
print('BÜYÜKTEN > KÜÇÜĞE SIRALAMA SONUCU...:',siraliDizi)


