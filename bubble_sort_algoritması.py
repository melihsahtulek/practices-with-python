'''
BENZERSİZ SAYILARDAN OLUŞAN DİZİYİ BUBBLE SORT ALGORİTMASI İLE SIRALAMA
'''
import random
uzunluk = int(input('UZUNLUK SAYISI GİRİNİZ...:'))
dizi = []

while(True):
    rastGele = random.randint(0, uzunluk * 10)
    if rastGele in dizi:
        pass
    else:
        dizi.append(rastGele)
    if dizi.__len__() == uzunluk:
        break

print('*********************************************************************************')
print('DİZİ UZUNLUĞU...:'+ str(uzunluk))
print('RANDOM SEÇİLEN BAŞLANGIÇ DİZİSİ...:', dizi)


for i in range(uzunluk):
    for j in range(uzunluk - 1):
        if dizi[j] > dizi[j + 1]:
            A = dizi[j]
            dizi[j] = dizi[j + 1]
            dizi[j + 1] = A



print('*********************************************************************************')
print('SIRALAMA SONUCU...:' ,dizi)
print('*********************************************************************************')
