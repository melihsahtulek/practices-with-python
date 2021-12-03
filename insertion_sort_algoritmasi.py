"""
    insertion sort algoritması
"""
import random
DiziU = int(input('Eleman Sayısı Giriniz...:'))
dizi = []

while (True):
    s = random.randint(1,DiziU * 2)
    if s in dizi:
        pass
    else:
        dizi.append(s)
    if dizi.__len__() == DiziU:
        break

print('RastGele Oluşturulan Sayı Dizisi...:',dizi)
print('')
for k in range(dizi.__len__()):
    for i in range(1, dizi.__len__()):
        B = dizi[i - 1]
        if dizi[i] < B:
            dizi[i - 1] = dizi[i]
            dizi[i] = B
print('Sıralama Sonucu...:',dizi)
