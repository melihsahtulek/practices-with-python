cumle = ['a','aa','aaa','MELİH','Melihşah Tülek','volkan']
uzunluk = []

for i in range(0,cumle.__len__()):
    uzunluk.append(cumle[i].__len__())

yeniBoy = 0
for j in range(0,uzunluk.__len__()):
    if uzunluk[j] >= yeniBoy:
        yeniBoy = uzunluk[j]

yer = 0
for x in range(0,uzunluk.__len__()):
    if yeniBoy == uzunluk[x]:
        yer = x

print('Cümle...:',cumle)
print('')
print('En Uzun Kelime...:',cumle[yer] , ">>>",yeniBoy,'Haneli')





