dersAdet = int(input('DERS SAYISI...:'))
dersler = []
kredi = []
vize = []
odev = []
final = []
ortalama = []
harfNotu = []
x = 0
y = 0
# UPDATE ---> Vize - Ödev - Final : Yüzde Hesabını Dinamik Hale Getirdim.
vizeH = int(input('Vize Notu Hesaplama Yüzdesi...:'))
odevH = int(input('Ödev Notu Hesaplama Yüzdesi...:'))
finalH = int(input('Final Notu Hesaplama Yüzdesi...:'))
print('***************************************************')
for i in range(dersAdet):
    dersAdi = input('DERS GİRİNİZ...:').upper()
    dersler.append(dersAdi)
    k = int(input('KREDİ SAYISI...:'))
    kredi.append(k)
    v = input('VİZE NOTU GİRİNİZ...:')
    vize.append(v)
    o = input('ODEV NOTU GİRİNİZ...:')
    odev.append(o)
    f = input('FİNAL NOTU GİRİNİZ...:')
    final.append(f)

    if odev[i] == "":
        ortHesapla = ((int(vize[i]) * (vizeH/100)) + (int(final[i]) * (finalH/100)))
    else:
        ortHesapla = ((int(vize[i]) * 0.3) + (int(odev[i]) * (odevH/100)) + (int(final[i]) * 0.6))
    ortalama.append(ortHesapla)

    if (ortalama[i]) >= 87.5:
        harfNotu.append("AA")
        x = (kredi[i] * 4) + x
    elif (ortalama[i]) >= 80.5 and ortalama[i] <= 87.4:
        harfNotu.append("BA")
        x = (kredi[i] * 3.50) + x
    elif (ortalama[i]) >= 73.5 and ortalama[i] <= 80.4:
        harfNotu.append("BB")
        x = (kredi[i] * 3) + x
    elif (ortalama[i]) >= 66.5 and ortalama[i] <= 73.4:
        harfNotu.append("CB")
        x = (kredi[i] * 2.50) + x
    elif (ortalama[i]) >= 59.5 and ortalama[i] <= 66.4:
        harfNotu.append("CC")
        x = (kredi[i] * 2) + x
    elif (ortalama[i]) >= 52.5 and ortalama[i] <= 59.4:
        harfNotu.append("DC")
        x = (kredi[i] * 1.50) + x
    elif (ortalama[i]) >= 45.5 and ortalama[i] <= 52.4:
        harfNotu.append("DD")
        x = (kredi[i] * 1) + x
    else:
        harfNotu.append("FD - FF ")
        x = (kredi[i] * 0) + x

for j in range(dersAdet):
    print('Ders Adı...:' , end="" + " ")
    for z in range(dersler[j].__len__()):
        print(dersler[j][z] , end="")
    print(" " + 'Vize Notu...:', vize[j] + ' ' + 'Ödev Notu...:',
        odev[j] + ' ' + 'Final Notu...:', final[j] + ' ' + 'Ortalama = ', ortalama[j] , 'Kredi Sayısı = '+ str(kredi[j]) + ' ' + 'HARF NOTU = ', harfNotu[j])

for a in range(kredi.__len__()):
    y = kredi[a] + y

print('****************')
print(' ')
print('GANO HESABI...:', round((x / y),2))

