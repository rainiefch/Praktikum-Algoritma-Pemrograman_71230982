# Buatlah program untuk melakukan pengecekan apakah semua anggota yang ada
# didalam tuple sama.
def comper(tup):
    hasil = all(isi == tup[0] for isi in tup)
    print(hasil)   

tA = (90, 90, 90, 90)
comper(tA)
tB = (1, 2, 3, 4)
comper(tB)

