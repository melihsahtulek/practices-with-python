n = int(input('N Sayısını Giriniz...:'))
a = 1
b = 1
t = 0
print(t,b,a , end=' ')
for i in range(1,n - 2):
    t = a + b
    b = a
    a = t
    print(t,end=' ')

#FIBO. SAYI DIZISI
