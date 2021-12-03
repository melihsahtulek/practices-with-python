import random
dizi = []
for x in range(1,20 + 1):
    rndS = random.randint(1, 100)
    dizi.append(rndS)
while (dizi.__len__() < 20):
    rndS = random.randint(1, 100)
    if rndS in dizi:
        pass
    else:
        dizi.append(rndS)
ciftS = []
tekS = []
for i in range(dizi.__len__()):
    if dizi[i] % 2 == 0:
        ciftS.append(dizi[i])
    else:
       tekS.append(dizi[i])

print('RANDOM SAYILAR DİZİSİ...:', dizi)
print('ÇİFT SAYILAR...:', ciftS)
print('TEK SAYILAR...:',  tekS)