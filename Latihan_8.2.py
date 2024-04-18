def kuis(file):
    with open(file, "r") as f:
        ls = [line.rstrip() for line in f]

    for l in ls:
        soal = l.split("||")
        print(f"Pertanyaan: {soal[0]}")
        kunci = soal[1].lower().strip()
        jawaban = input("Jawab: ").lower().strip()

        if kunci == jawaban:
            print("Jawaban benar!")
        else:
            print("Jawaban salah!")

file = input("Sebutkan file soal : ")
kuis(file)