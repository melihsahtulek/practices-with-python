#######################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#                   GİRİLEN İKİ SAYININ               #
#                    ASAL ÇARPANLARINI                #
#                   HESAPLAYAN PROGRAM                #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#######################################################
n1 = int(input('BİRİNCİ SAYIYI GİRİNİZ..:'))
s1 = n1
degerTut_1 = 0
n2 = int(input('İKİNCİ SAYIYI GİRİNİZ..:'))
s2 = n2
degerTut_2 = 0
bolen = 2
sonuc_1 = []
sonuc_2 = []

for i in range(s1 + s2):

    if s1 % bolen == 0:
        degerTut_1 = (int(s1 / bolen))
        s1 = degerTut_1
        sonuc_1.append(bolen)
    else:
        if s2 % bolen == 0:
            degerTut_2 = (int(s2 / bolen))
            s2 = degerTut_2
            sonuc_2.append(bolen)
        else:
            bolen = bolen + 1

print('*************************************************')
print(n1,':Sayısının Asal Çarpanları...:',sonuc_1)
print(n2,':Sayısının Asal Çarpanları...:',sonuc_2)
print('*************************************************')