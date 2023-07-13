print("Latihan dasar python")

print("Program menghitung luas persegi panjang")

p = float(input("Masukkan panjang  : "))
l = float(input("Masukkan lebar : "))

luas = p * l

print("luas", luas)

print("Program menghitung luas segitiga")
#ini adalah komentar
a = float(input("Masukkan alas : "))
t = float(input("Masukkan tinggi : "))

luassegitiga = 0.5 * a * t

print("luas segitiga", luassegitiga)

print("Program nilai")

nilai =float(input("Masukkan nilainya :"))

if nilai >= 80 :
    print("A")
elif nilai >= 60 :
    print("B")
else :
    print("C")