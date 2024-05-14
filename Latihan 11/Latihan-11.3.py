# Latihan 11.3 Buatlah program untuk menghitung distribusi jam dalam satu hari dimana ada
# pesan yang diterima dari setiap email yang masuk. Gunakan file mbox-short.txt untuk sebagai
# datanya. Berikut ini adalah contoh output dari programmnya.

jumlah = dict()
file = input("Masukkan nama file: ")
try:
    f = open(file)
except:
    print("File tidak dapat dibuka")
    exit()

for baris in f:
    if baris.startswith("From "):
        waktu = baris.split()[5]
        jam = waktu.split(':')[0]
        jumlah[jam] = jumlah.get(jam, 0) + 1

urut = sorted(jumlah.items())

for jam, jumlah in urut:
    print(jam, jumlah)
