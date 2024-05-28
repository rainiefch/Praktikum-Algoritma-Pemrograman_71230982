# Latihan 13.1 
# Vidi adalah adik Tono yang sedang belajar bilangan prima. Vidi mengalami 
# kesulitan untuk menentukan suatu bilangan bilangan prima atau bukan. Untuk membantu adiknya
# Tono kemudian membuat program untuk pengecekan bilangan prima dengan menggunakan
# fungsi rekursif. Bantulah Tono untuk menyelesaikan tugas tersebut.

# def prima(a, b = None):
#     if b is None:
#         b = a - 1
#     while b >= 2:
#         if a % b == 0:
#             print("BUKAN PRIMA")
#             return False
#         else:
#             return prima(a, b - 1)
#     else:
#         print("PRIMA")
#         return True
        
# n = int(input("Masukkan angka :"))
# prima(n)

def prima(a, b = None):
    if b is None:
        b = a - 1
    while b > 1:
        if a % b == 0:
            return "BUKAN PRIMA"
        else:
            return prima(a, b - 1)
    else:
        return "PRIMA"
        
n = int(input("Masukkan angka :"))
print(prima(n))