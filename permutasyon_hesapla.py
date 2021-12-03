n = int(input("N'sayısını Giriniz...:"))
r = int(input("R'sayısını Giriniz...:"))
if r >= n:
    print('R Değeri , N değerinden küçük olmalı...')
else:
    print('****************************************')

    nT = 1
    for i in range(1, n + 1):
        nT = i * nT

    rT = 1
    for j in range(1, r + 1):
        rT = j * rT

    x = n - r
    y = 1
    for z in range(1, x + 1):
        y = z * y

    per = nT / y
    print('Permütasyon Sonucu...:', "P",(n, r), "=", round(per))
