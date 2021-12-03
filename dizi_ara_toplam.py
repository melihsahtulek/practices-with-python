sB = int(input('Başlangış Değerini Giriniz...:'))
sS = int(input('Bitiş Sayısını Griniz...:'))
sA = int(input('Artış Değerini Giriniz...:'))
sT = 0

for i in range(sB ,sS + 1 ,sA):
    sT = sT + i
    print(i , sT)

print('Girilen Aralığın Toplamı...:',sT,end=" ")