import math
n = int(input('Kuvveti Hesaplanacak Sayı...:'))
us = int(input('Kuvvet Giriniz...:'))
def usHesapla(sayi,kuvvet):
    print('Sonuç...:',int(math.pow(sayi,kuvvet)))

usHesapla(n,us)
