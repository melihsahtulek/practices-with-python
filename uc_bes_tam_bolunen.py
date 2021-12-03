s1 = 5,10,15,20,25,30,35,40,45,50

t1 = 0
t2 = 0
print("5'e Tam Bölünen Sayılar...:")
for i in range(0,s1.__len__()):
    if s1[i] % 5 == 0:
        t1 = s1[i]
        print(t1,end=",")
print(" ")
print(" ")
print("3'e Tam Bölünen Sayılar...:")
for i in range(0,s1.__len__()):
    if s1[i] % 3 == 0:
        t2 = s1[i]
        print(t2,end=",")



