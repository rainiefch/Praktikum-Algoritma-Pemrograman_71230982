# Latihan 12.1 Dari contoh kasus kategori kasus di Play Store, tambahkan kemampuan-kemampuan berikut ini:
# • Tampilkan nama-nama aplikasi yang hanya muncul di satu kategori saja.
# • Untuk input n>2, tampilkan nama-nama aplikasi yang muncul tepat di dua kategori sekaligus

n = int(input('Masukkan jumlah kategori: '))

daftar_app = {}

for i in range(n):
    kate = input('Masukkan nama kategori:')
    print('Masukkan 5 nama aplikasi di kategori', kate)
    app = []
    for j in range(5):
        nama_app = input('Nama aplikasi: ')
        app.append(nama_app)
    daftar_app[kate] = app

daftar_app_ls = []

for app in daftar_app.values():
    daftar_app_ls.append(set(app))

if n == 2:
    sym_diff = daftar_app_ls[0].symmetric_difference(daftar_app_ls[1])
    print("Aplikasi Yang Hanya Muncul Di Satu Kategori Saja: ", sym_diff)
elif n > 2:
    for y in range(1,n):
        sym_diff = daftar_app_ls[i] and daftar_app_ls[i-1] 
    else:
        sym_diff = daftar_app_ls[0] and daftar_app_ls[1] 
    print("Aplikasi Yang Muncul Di Dua Kategori Sekaligus: ", sym_diff)

