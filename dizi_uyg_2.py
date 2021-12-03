n = int(input('Sayı Giriniz...:'))
toplam = 0

for i in range(n + 1):
    toplam = toplam + i

print(toplam)


n = int(input('Sayı Giriniz...:'))
toplam = 0

for i in range(0,n + 1,2):
    toplam = toplam + i

print(toplam)
