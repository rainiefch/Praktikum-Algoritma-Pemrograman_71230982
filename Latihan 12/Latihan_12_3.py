# Latihan 12.3 Buatlah sebuah program yang dapat membaca dua file teks dan menampilkan
# semua kata-kata yang muncul pada kedua file tersebut. Beberapa hal yang perlu anda perhatikan:
# • Nama file adalah input user. Tampilkan pesan error jika file tidak ditemukan/tidak bisa
# dibaca.
# • Semua kata dikonversi dulu menjadi lowercase.
# • Sertakan contoh file teks yang anda pakai saat mengumpulkan laporan.

t1 = input("Masukkan nama file teks 1: ")
t2 = input("Masukkan nama file teks 2: ")

try:
    with open(t1, 'r') as f1, open(t2, 'r') as f2:
        kata1 = set(kata.lower() for baris in f1 for kata in baris.split())
        kata2 = set(kata.lower() for baris in f2 for kata in baris.split())

    sama = kata1.intersection(kata2)
    print("Kata-kata yang muncul pada kedua file:", sama)

except FileNotFoundError:
    print("File tidak ditemukan")