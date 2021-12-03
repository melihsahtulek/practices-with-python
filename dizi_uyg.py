n = int(input('Eleman Sayısı...:'))
dizi = []
t = 0
for i in range(1,n + 1):
    dizi.append(i)
for j in range(dizi.__len__()):
    t = dizi[j] + t
print('Diziniz...:',dizi,' T = ',t)
