# Latihan 12.2 Buatlah sebuah program yang mendemonstrasikan konversi dari:
# • List menjadi Set
# • Set menjadi List
# • Tuple menjadi Set
# • Set menjadi Tuple
# Tampilkan isi data sebelum dan sesudah konversi.

data = input("Masukkan data yang mau dikonversi: ")  
   
print("List ke Set")
data = list(data)
print("List: ",data) 
data = set(data)
print("Set: ",data)
print()

print("Set ke List")
print("Set: ",data)
data = list(data)
print("List: ",data)  
print()

print("Tuple ke Set")
data = tuple(data) 
print("Tuple: ",data) 
data = set(data)
print("Set: ",data)  
print() 

print("Set ke Tuple") 
data = set(data)
print("Set: ",data)
data = tuple(data) 
print("Tuple: ",data)

