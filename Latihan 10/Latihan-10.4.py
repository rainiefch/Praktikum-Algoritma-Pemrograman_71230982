domain = dict()
file = input("Masukkan nama file: ")
try:
    f = open(file)
except:
    print("File tidak dapat dibuka")
    exit()

for baris in f:
    isi = baris.split()
    if len(isi) > 0  and isi[0] == "From:" :
        domain[isi[1][isi[1].find("@")+1:]] =  domain.get(isi[1][isi[1].find("@")+1:],0) + 1

print(domain)