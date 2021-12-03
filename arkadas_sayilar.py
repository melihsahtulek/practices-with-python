# ARKADAŞ SAYILAR #
n1 = int(input('Birinci Sayıyı Giriniz...:'))
n1Sum = 0
n2 = int(input('İkinci Sayıyı Giriniz...:'))
n2Sum = 0

def areFriends(n1,n2,n1Sum,n2Sum):
  for i in range(1, n1):
    if n1 % i == 0:
      n1Sum += i
      
  for j in range(1, n2):
    if n2 % j == 0:
      n2Sum += j


  if (n1Sum == n2 and n2Sum == n1):
    print('Girilen İKİ sayı Arkadaştır...:', n1, n2)
  else:
    print('TEKRAR DENEYİNİZ...')

areFriends(n1,n2,n1Sum,n2Sum)
