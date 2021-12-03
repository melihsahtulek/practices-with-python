#######################################################
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#                   EBOB HESAPLAMA                    #
#                       PROGRAMI                      #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#######################################################
ilk = int(input("İlk sayıyı giriniz: "))
ikinci = int(input("İkinci sayıyı giriniz: "))

if  ikinci<ilk:
    kucuk=ikinci
else:
    kucuk=ilk

for i in range(1,kucuk+1):
    if ilk%i == 0 and ikinci%i == 0:
        ebob = i

print("Ebob :",ebob)
