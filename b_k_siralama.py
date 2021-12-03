# Girilen 3 Sayıyı Büyükten Küçüğe Sıralama #
n1 = int(input('Sayı 1:'))
n2 = int(input('Sayı 2:'))
n3 = int(input('Sayı 3:'))
dizi = [n1,n2,n3]
A = 0
print('Girilen 3 Sayıyı Büyükten Küçüğe Sıralama...:')



for i in range(dizi.__len__()):
  for j in range(dizi.__len__() - 1):
    if dizi[j] > dizi[j + 1]:
      pass
    else:
      A = dizi[j]
      dizi[j] = dizi[j + 1]
      dizi[j + 1] = A


print(dizi)


