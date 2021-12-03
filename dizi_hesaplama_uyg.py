import random
n = int(input('Eleman Sayısını Giriniz...:'))
dizi = []
for i in range(1,n + 1):
    rndSayi = random.randint(1,10)
    dizi.append(rndSayi)
yeniDizi = []
while(yeniDizi.__len__() < n):
    rndSayi = random.randint(1, n + 1)
    if(rndSayi in yeniDizi):
        pass
    else:
        yeniDizi.append(rndSayi)
pT = 0
nT = 0
for j in range(0,yeniDizi.__len__()):
    if yeniDizi[j] % 2 == 0:
        yeniDizi[j] = yeniDizi[j] * (-1)
    if yeniDizi[j] < 0:
        nT = nT + yeniDizi[j]
    else:
        pT = pT + yeniDizi[j]
print(yeniDizi)
print('Pozitif Sayılar Toplamı...:',pT)
print('Negatif Sayılar Toplamı...:',nT)
print('En Büyük Sayı...:',max(yeniDizi) , ' - - - ' ,'En Küçük Sayı...:',min(yeniDizi))
enKucukIndex = 0
enBuyukIndex = 0
for x in range(0,yeniDizi.__len__()):
    if min(yeniDizi) == yeniDizi[x]:
        enKucukIndex = x
    if max(yeniDizi) == yeniDizi[x]:
        enBuyukIndex = x
print('En Buyuk Değerin İndex No...:', enBuyukIndex)
print('En Kucuk Değerin İndex No...:',enKucukIndex)


