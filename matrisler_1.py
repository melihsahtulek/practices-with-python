matris = []
k = 0
for i in range(0,5):
    matris.append([])
    for j in range(0,5):
        matris[i].append(0)
    matris[i][k] = 1
    k = k + 1
    

for i in range(len(matris)):
    print(matris[i])
