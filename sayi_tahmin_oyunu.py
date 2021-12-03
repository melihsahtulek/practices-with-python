import random
rS = random.randint(1,50)
hak = 5
print("1 - 50 Arasında Sayı Tahmin Oyunu...")

while(hak > 0):
    kS = int(input('Bir Sayı Giriniz...:'))
    if kS == rS:
        print('Tebrikler... Doğru Bildiniz...:',kS)
        break
    if kS != rS:
        hak = hak - 1
        print('kalan Hakkınız...:',hak)
    if hak == 0:
        print('Kaybettiniz...:')
        kontrol = input("Yeniden Denemek İçin e/h...:")
        if kontrol == "e":
            hak = 5
        if kontrol == "h":
            print('Sistemin Tuttugu Sayı...:', rS)
            break
