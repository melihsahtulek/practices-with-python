# İlk 1000 Asal Sayı #
dizi = []
control = False
for i in range(2,1000):
    control = False
    for j in range(2,i):
        if i % j == 0:
           control = True

    if control == False:
        dizi.append(i)

print(dizi)
                
                
        

