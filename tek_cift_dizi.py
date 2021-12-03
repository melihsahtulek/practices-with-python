dizi = [1,2,3,4,5,6,7,8,9,10]
tekDizi = []
ciftDizi = []
yeniDizi = []

for i in range(dizi.__len__()):
    if dizi[i] % 2 == 0:
        ciftDizi.append(dizi[i])
    if dizi[i] % 2 != 0:
        tekDizi.append(dizi[i])

yeniDizi.append(tekDizi)
yeniDizi.append(ciftDizi)
print(yeniDizi)