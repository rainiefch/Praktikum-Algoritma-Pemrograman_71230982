#Latihan 13.5 Buatlah fungsi rekursif untuk menghitung kombinasi!

def c(a, b):
    if b == 0:
        return 1
    else:
        int((a - b + 1 ) / b) 
        return (c(a , b - 1) * (a - b + 1) / (b))

a = int((input("Masukkan a :")))
b = int((input("Masukkan b :")))

print(c(a, b))


