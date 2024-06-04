# Anda diminta untuk mencari seluruh teks yang berupa tanggal dengan format
# YYYY-MM-DD dan kemudian seluruh tanggal tersebut diambil dan ditampilkan kembali dalam
# format DD-MM-YYYY ditambah dengan perhitungan selisih dengan tanggal sekarang dalam hari.
# Contoh:
# Pada tanggal 1945-08-17 Indonesia merdeka. Indonesia memiliki beberapa pahlawan
# nasional, seperti Pangeran Diponegoro (TL: 1785-11-11), Pattimura (TL: 1783-06-08) dan Ki
# Hajar Dewantara (1889-05-02).
# Hasil:
# 1945-08-17 00:00:00 selisih 27209 hari
# 1785-11-11 00:00:00 selisih 85561 hari
# 1783-06-08 00:00:00 selisih 86448 hari
# 1889-05-02 00:00:00 selisih 47769 hari

import re
from datetime import datetime

rn = datetime.now()

yr = rn.year
mh = rn.month
dy = rn.day
tgl = (f'{dy}-{mh}-{yr}')
gp = re.compile(r'\d{4}-\d{2}-\d{2}')
text = open("tgl.txt", "r")
t = text.read()
cari = gp.findall(t)
x = []
for i in cari:
    a = i.split("-")
    b = (a[2]+'-'+a[1]+'-'+a[0])
    x.append(b)
form = '%d-%m-%Y'
tgl = datetime.strptime(tgl, form)
for j in x:
    c = datetime.strptime(j, form)
    d = tgl - c
    print(f'{tgl} 00:00:00 selisih {d.days} hari')


