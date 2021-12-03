import math
# STANDART SAPMA HESAPLAMASI #
dizi = []
for i in range(1,10 + 1):
    dizi.append(i)

print('Veriler Dizisi...:',dizi)

verilerTop = 0
for j in range(0,dizi.__len__()):
    verilerTop = verilerTop + dizi[j]
print('Veriler Toplamı...:',verilerTop)

arOrtalama = verilerTop / dizi.__len__()
print('Aritmetik Ortalama...:',int(arOrtalama))

karelerTop = 0
for z in range(dizi.__len__()):
    karelerTop = pow(int(arOrtalama - dizi[z]),2) + karelerTop

print('Kareler Toplamı...:',karelerTop)

standartSapma = math.sqrt(karelerTop / (dizi.__len__() - 1))
print('Standart Sapma...:',round(standartSapma,2))

varyans = round(pow(standartSapma,2),1)
print('Varyans...:',varyans)


