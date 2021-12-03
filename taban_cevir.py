#######################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#                   10'TABANINDAN                     #
#                 2'TABANINA ÇEVİREN                  #
#                      PROGRAM                        #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#######################################################
def tabanCevir(bolunen , bolen): # 2 TABANI SABİT!
    kalan = []

    while(True):
        ilkBolum = int(bolunen / bolen)
        kalan.append(bolunen - (bolen * ilkBolum))
        bolunen = ilkBolum

        if ilkBolum < bolen:
            kalan.append(ilkBolum)
            kalan.reverse()
            return kalan
            break

print('**** İŞLEM SONUCU ****')
for i in tabanCevir(20,2):
    print(i,end="")



