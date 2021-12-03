def cevir(x):
    for i in range(x.__len__()):
        if ord(x[i]) >= 64 and ord(x[i]) <= 90:
            print(chr(ord(x[i]) + 32), end=" ")
        elif ord(x[i]) >= 97 and ord(x[i]) <= 122:
            print(chr(ord(x[i]) - 32), end=" ")

veri = input('Veri Giriniz...:')
cevir(veri)


