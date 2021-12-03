'''
Soru 2: Çift Fibonacci sayıları
'''
a , b = 0 , 1
top = []
ciftTop = 0
for i in range(10): # 4 Milyon :)
    top.append(a + b)
    a = b
    b = top[i]
    if top[i] % 2 == 0:
        ciftTop += top[i]

print("Oluşan Dizi: {} Çift Sayılar Toplamı: {}".format(top,ciftTop))




