# Latihan 11.2 Buatlah program dengan menggunakan tuple yang dapat melalakukan proses
# seperti pada kasus 11.1, Gunakan data diri anda masing-masing dan lakukan perubahan supaya
# didapatkan output seperti contoh berikut ini :

data = ("Rainie Fanita Chrisabel Hadisantoso", "71230982", "Godean, DIY")

nim = tuple(data[1])
nama_depan = tuple(data[0].split()[0])
nama_terbalik = tuple(data[0].split()[::-1])
alamat = tuple(data[2])

print(f"NIM : {nim}")
print(f"NAMA DEPAN : {nama_depan}")
print(f"NAMA TERBALIK : {nama_terbalik}")
