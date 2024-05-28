#Latihan 13.2 
#Buatlah fungsi rekursif mengetahui suatu kalimat adalah palindrom atau bukan!

def palin(k):
    if len(k) == 0:
        return "PALINDROM"
    else:
        if k[0] == k[-1]:
            return palin(k[1:-1])
        else:
            return "BUKAN PALINDROM"
            
k = str(input("Masukkan kalimat :"))
print(palin(k))