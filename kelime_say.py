cumle = "KELİME SAYAR"
kelimeSayisi = 1

for i in range(cumle.__len__()):
    if cumle[i] == chr(32):
        kelimeSayisi = kelimeSayisi + 1

print(kelimeSayisi)