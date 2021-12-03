# Komut Satırı Argumanlarını Tersten Yazdıran Program #

txt = "ahmet hasan mehmet ali"
newTxt = txt.split(" ")
for i in range(len(newTxt) - 1, -1, -1):
    print(newTxt[i], end=" ")
    
    
