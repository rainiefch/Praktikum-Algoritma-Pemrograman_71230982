nilai = []
print("Masukkan nilai-nilai (kalau sudah ketik 'done')")
masuk = False
i = 1
while masuk == False:
  hasil = input(f"Nilai {i}: ")
  i += 1
  try:
    hasil = int(hasil)
    nilai.append(hasil)
  except:
    if hasil.lower() == "done":
      masuk = True
    else:
      print("Input salah!")

print(f"Nilai minimum: {min(nilai)}")
print(f"Nilai maximum: {max(nilai)}")