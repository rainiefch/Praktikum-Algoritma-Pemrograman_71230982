file  = input("Masukkan nama file: ")
email = dict()
try:
    f = open(file)
except:
    print('File tidak dapat dibuka')
    exit()

for baris in f:
    isi = baris.split()
    if len(isi) < 2 or isi[0] != "From":
        continue
    else:
        email[isi[1]] = 1 +  email.get(isi[1],0)  

print(email)   