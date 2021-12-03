def sifreleMetin(giris,n):
    girisCevir = []  # ascii kodları eklendi.
    cikis = []  # şifreli metin
    cikisCevir = []  # ascii kodları eklendi.
    for i in range(giris.__len__()):
        if ord(giris[i]) >= 65 and ord(giris[i]) <= 90:
            if ord(giris[i]) >= 90 - n:
                girisCevir.append(ord(giris[i]) - ord(giris[i]) + (65 - n) + i)
                cikis.append(chr(girisCevir[i] + n))  # Çevrildi.
                cikisCevir.append(ord(cikis[i]))  # ascii Kodları Eklendi.
            else:
                girisCevir.append(ord(giris[i]))  # ascii Kodları Eklendi.
                cikis.append(chr(girisCevir[i] + n))  # Çevrildi.
                cikisCevir.append(ord(cikis[i]))  # ascii Kodları Eklendi.
        else:
            print('TÜRKÇE HARF GİRMEYİNİZ!')
            exit()
    #for j in range(girisCevir.__len__()):
        # print(giris[j], " = ", girisCevir[j])
    #print(' ************************************* ')
    print('Şifreleme Sonucu:')
    for z in range(girisCevir.__len__()):
        #print(cikis[z], " = ", cikisCevir[z])
        print(cikis[z] ,end=" ")
    print(' ')
    print('Çözümlenen Metin:')
    for m in range(girisCevir.__len__()):
            print(chr(cikisCevir[m] - n), end=" ")
metin = input('METİN GİRİNİZ...:').upper()
artis = int(input('N SAYISI...:'))
sifreleMetin(metin,artis)

