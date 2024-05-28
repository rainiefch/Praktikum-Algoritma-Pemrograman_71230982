#Latihan 13.4 
#Buatlah fungsi rekursif untuk mengetahui jumlah digit dari suatu bilangan. Seperti
#misalnya tulisan: "234" maka jumlah digitnya adalah 2+3+4 = 9!

def jmlhdigit(x):
    y = len(x)-1
    if y == 0:
        return x
    else:
        z = int(x[-1])
        x = x[:-1]
        return z + int(jmlhdigit(x))

x = (input("Masukkan bilangan :"))
print(jmlhdigit(x))