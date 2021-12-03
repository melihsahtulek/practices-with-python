# En Yakın Asal Sayı #

n = int(input('Sayı Giriniz...:'))
c = False
b = False

for k in range(2, n): #Asal kontrol
    if n % k == 0:
        c = True

if c == False:
    print('Girilen Sayı Asaldır...')

if c == True:
    for i in range(n - 1, 1, -1):
        if n % i == 0:
            n = n - 1
            b = True
               
    if b == True:
        print(n)

        
            


            
        

            
        
        
        
