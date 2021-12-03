# Rastgele Oluşturulan Dizide En Çok Tekrar Eden Değeri Bulmak #
import random

girdi = int(input('Random Sayı Dizisi Kaç Elemanlı Olsun...:'))
nArr = [] # Sayı Dizimiz
arr = []  # Tekrar Sayıları
s = 0     # Kontrol
tekrarEden = 0 # Sonuç

for x in range(girdi):
    nArr.append(random.randint(0,girdi))
    
print('*********************************')
print('Yeni Dizi...:', nArr)
print('*********************************')

for i in range(len(nArr)):
    s = 0
    for j in range(len(nArr)):
        if nArr[i] == nArr[j]:
            s = s + 1
            if len(arr) >= 1:
                if s == max(arr):
                    tekrarEden = nArr[i]
    arr.append(s)
    
print('EN ÇOK TEKRAR EDEN DEĞER...:', tekrarEden)



   

