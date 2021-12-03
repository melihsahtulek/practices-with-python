# Sayısal Loto Kuponu Basan Program #

# Yazılım Kuralları Bu Sayfadan Alınmıştır...: http://www.csystem.org/calisma-sorulari/sayısal-loto-kuponu-basan-program

import random
print('# Sayısal Loto Kuponu Basan Program #')
colons = []
for i in range(8):
    colons.append([])
    while True:
        n = random.randint(1,50)
        if n in colons[i]:
            pass
        else:
            colons[i].append(n)
        if len(colons[i]) == 6:
            break
            
    print(i+1,". KOLON...: ",colons[i], end="")
    print('')




