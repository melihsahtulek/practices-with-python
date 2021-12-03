# Süre Görüntüleme (HESAPLAMA) #
sure = int(input('Saniye Cinsinden Veri Giriniz...:'))
def hesapla(sure):
    saat = 0 ; dakika = 0 ; saniye = 0 ; tut = 0
    while True:
        if sure >= 3600:
            saat += 1
            sure = sure - 3600
        if sure >= 60:
            dakika += 1
            sure = sure - 60
        if sure < 60:
            saniye = sure
            break

    print(saat,"saat - ",dakika,"dakika - ",saniye,"saniye")
hesapla(sure)
