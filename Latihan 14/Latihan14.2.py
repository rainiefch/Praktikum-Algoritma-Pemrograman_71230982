# Anda diminta untuk mencari seluruh teks yang berupa email dan kemudian ambil
# semua username dari email tersebut untuk digenerate password random 8 karakter yang terdiri
# dari angka dan huruf.
# Contoh:
# Berikut adalah daftar email dan nama pengguna dari mailing list:
# anton@mail.com dimiliki oleh antonius
# budi@gmail.co.id dimiliki oleh budi anwari
# slamet@getnada.com dimiliki oleh slamet slumut
# matahari@tokopedia.com dimiliki oleh toko matahari
# Hasil:
# anton@mail.com username: anton , password: 8u78A2UD
# budi@gmail.co.id username: budi , password: bdP066Ld
# slamet@getnada.com username: slamet , password: Ab1FiHXb
# matahari@tokopedia.com username: matahari , password: 5KYyaP6

import re
import random
import string

g = re.compile(r'\S+@\S+')
text = open("akun.txt", "r")
t = text.read()    
cari = g.findall(t)

for k in cari:
    at = k.split('@')
    h = at[0]
    pw_alfa = string.ascii_letters + string.digits
    pw = ''.join(random.choice(pw_alfa) for i in range(8))
    print(f'{k}: {h}, password: {pw}')

