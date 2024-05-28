#Latihan 13.3 
#Buatlah fungsi rekursif untuk menghitung jumlah deret ganjil dari 1 + 3 + 7 + . . .+ n!

# def jumlah( x , y = 1):
#     if x < y:
#         return 0
#     else:
#         return y + jumlah(x, y + 2)

# x = int(input("Masukkan n:"))
# print("Jumlah bilangan ganjil :",jumlah(x))

# def jumlah( x , y = 1):
#     if y == 1:
#         print(y,end=" ")
#         return y + jumlah(x, y + 2)
#     elif x > y:
#         print("=", end=" ")
#         return 0
#     else:
#         print("+",y,end=" ")
#         return y + jumlah(x, y + 2)
        
def jumlah(x,y):
    if x > y:
        return 0
    return x + jumlah(x + 2,y)    

x = 1
y = int(input("Masukkan n:"))
print(jumlah(x,y))