print('*** Faktöriyel Hesaplama ***'.upper())

n = int(input('Hesaplanacak Sayı...:'))
t = 1
for i in range(1,n + 1):
    t = t * i

print(n,"Sayısının Faktöriyel'i...:",t)
