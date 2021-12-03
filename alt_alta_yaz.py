m = input('Metin Giriniz...:').upper()

for i in range(m.__len__()):
    if m[i] == chr(32):
        print(' ')
    if m[i] != chr(32):
        print(i + 1, ".Harf", m[i])
