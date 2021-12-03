'''
Soru 3: En büyük asal çarpan
'''
N , bAsal = 680 , 0
control = bool
asalList = []

for i in range(1,N):
    control = False
    for j in range(2,i):
        if i % j == 0:
            control = True
      
    if control == False:
        asalList.append(i)
        
for k in range(len(asalList)):
    if N % asalList[k] == 0:
        bAsal = asalList[k]

print("{} Sayısının - En Büyük Asal Çarpanı: {}".format(N,bAsal))
            

