kata2 = []
with open("berita.txt", "r") as f:
    for w in f:
        kata = w.split()
        kata2.extend(kata)

print(kata2)
