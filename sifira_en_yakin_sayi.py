# Sıfıra En yakın Sayıyı Bulma #
nDizi = [10,25,-2,15,3,5,2]
sonuc = 0

for k in range(len(nDizi)):
    if nDizi[k] == 0:
        sonuc = nDizi[k]
    for j in range(len(nDizi) - 1):
        if nDizi[j] < 0:
            nDizi[j] = -nDizi[j]
        else:
            if nDizi[j] < nDizi[j + 1]:
                tut = nDizi[j]
                nDizi[j] = nDizi[j + 1]
                nDizi[j + 1] = tut
    sonuc = nDizi[k]

print('0"a En Yakın Sayı...:', sonuc)


                
            
        

    
