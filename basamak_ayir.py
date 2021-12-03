#######################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#                       BASAMAK                       #
#                       AYIRMA                        #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#######################################################
s = int(input("4'BASAMAKLI SAYI GİRİNİZ...:"))

def hesapla(sayi):
    binler = int((sayi / 1000)) * 1000
    print('BİNLER BASAMAĞI...:' , binler)

    yuzler = int((sayi - binler) / 100) * 100
    print('YÜZLER BASAMAĞI...:' ,yuzler)

    onlar = int((sayi - (yuzler + binler)) / 10) * 10
    print('ONLAR BASAMAĞI...:' ,onlar)

    birler = int((sayi - (onlar + yuzler + binler)))
    print('BİRLER BASAMAĞI...:' ,birler)

hesapla(s)