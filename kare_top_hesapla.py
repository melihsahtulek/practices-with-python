n = int(input('Bir Sayı Giriniz...:'))
toplam = 0

import math
for i in range(1, n + 1):
    toplam = toplam + math.pow(i,2)

print('Sayıların Karelerinin Toplamı...:', toplam)