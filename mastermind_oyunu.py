# Mastermind Oyunu #
# Oyun Kuralları bu sayfadan alınmıştır...: http://www.csystem.org/calisma-sorulari/mastermind-oyunu

import random
rN = ""
for i in range(4):
    rN += str(random.randint(0,9))
#print('Tutulan Sayı (Bilgisayar)...:',rN)
c = 0
y = 0
while True:
    playerN = input('BİR TAHMİNDE BULUNUN...:')
    if len(playerN) < 4:
        print('4 Basamaklı Sayı Giriniz...')
    else:
        for j in range(len(rN)):
            if playerN[j] == rN[j]:
                print('+', end=",")
                y += 1
            else:
                print('-', end=",")

    c += 1
    print('')
    if c == 4:
        break
    if y == 4:
        break
    
            


