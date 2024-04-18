def banding(file1, file2):
    with open(file1, "r") as f1:
        ls1 = [line.rstrip() for line in f1]

    with open(file2, "r") as f2:
        ls2 = [line.rstrip() for line in f2]

    gabung = zip(ls1, ls2)
    no = 1
    for l1, l2 in gabung:
        if l1 != l2:
            print(f"Perbedaan di baris {no}:")
            print(f"File 1: {l1}")
            print(f"File 2: {l2}")
        no += 1

file1 = input("Masukkan nama file pertama : ")
file2 = input("Masukkan nama file kedua : ")
banding(file1, file2)

