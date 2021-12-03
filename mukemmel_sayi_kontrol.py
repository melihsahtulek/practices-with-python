sayi = int(input('Sayı Giriniz...:'))
ptBolenler = []
t = 0
for i in range(1,sayi): # n - 1
    if sayi % i == 0:
        ptBolenler.append(i)
        t = t + i
if t == sayi:
    print('Girilen Değer Mükemmel Sayıdır...:', sayi)
else:
    print('Girilen Değer Mükemmel Sayı Değildir...:' , sayi)

print('Pozitif Tam Bölenler...:' , ptBolenler)
