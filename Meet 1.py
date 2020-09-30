# Nama            : Akhmad Rizaldi Irvana
# NIM             : 190411100128
# Matakuliah      : Pemrograman Desktop C

import math

# No 1
# Buat program ddan deklarasikan 5

v1 = 5
v2 = 9
v3 = 3
v4 = 6
v5 = 4

avg = (v1+v2+v3+v4+v5)/5

print("No. 1")
print("Rata-rata 5 variable")
print("variable 1 =", v1)
print("variable 2 =", v2)
print("variable 3 =", v3)
print("variable 4 =", v4)
print("variable 5 =", v5)
print("rata-rata =", avg)
print('')

# No 2
# Buat program untuk mencari luas dan keliling bangun datar dengan inputan dari user
print("\n")
print("No. 2")
print("Luas dan keliling bangun datar")
salah = True
while salah == True:
    print("pilih bangun datar :")
    print("1. Persegi panjang")
    print("2. Segitga sama kaki")
    print("3. Lingkaran")
    pilih = int(input("pilih nomor 1, 2, atau 3 ? "))
    
    if pilih == 1:
        p = int(input("masukkkan panjang (cm) : "))
        l = int(input("masukkan lebar (cm) : "))
        print("")
        L = p * l
        k = (2 * p) + (2 * l)
        print("Luas =", L, "cm2")
        print("Keliling =", k, "cm")
        break
    
    elif pilih == 2:
        a = int(input("masukkkan alas (cm) : "))
        t = int(input("masukkan tinggi (cm) : "))
        print("")
        L = (a * t)/2
        k = a + (2*(math.sqrt((a/2)**2 + t**2)))
        print("Luas =", L, "cm2")
        print("Keliling =", k, "cm")
        break
    
    elif pilih == 3:
        r = int(input("masukkan jari-jari (cm) : "))
        print("")
        L = 3.14 * r * r
        k = 2 * 3.14 * r
        print("Luas =", L, "cm2")
        print("Keliling =", k, "cm")
        break
    
    else:
        print("Harap masukkan angka 1, 2, atau 3")


# No 3
# Buat program untuk mengelompokkan body mass index (BMI)
print("\n")
print("No. 3")
print("Pengelompokan Body Mass Index")
tinggi_cm = float(input("Masukkkan tinggi (cm) : "))
berat = float(input("Masukkan berat badan (kg) : "))
print("")
tinggi_m = tinggi_cm/100

BMI = berat / (tinggi_m**2)
if BMI < 18.5:
    print("berat badan anda kurang")
elif BMI >= 18.5 and BMI <23:
    print("berat badan anda normal")
elif BMI >= 23 and BMI < 30:
    print("berat badan anda berlebih (cenderung obesitas)")
elif BMI >= 30:
    print("anda obesitas")

# No 4
# Buat program untuk menentukan nilai maksimal dan minimal dari sejumlah nilai N
print("\n")
print("No. 4")
print("Menentukan Nilai Maksimal dan Minimal")

n = int(input("berapa banyak angka yang ingin anda masukkan : "))
data = []
for i in range (0, n):
    angka = int(input("masukkan angka : "))
    data.append(angka)

minimal = data[0]
maksimal = data[len(data)-1]
for j in range (0, n-1):
    if data[j+1] > data [j]:
        minimal = data[j]
        maksimal = data[j+1]
    else:
        continue
print("")
print("data =", data)
print("data angka minimal =", minimal)
print("angka maksimal =", maksimal)

# No. 5
# Buat program untuk validasi username dan password sebanyak 3x
print("\n")
print("No. 5")
print("Buat program untuk validasi username dan password sebanyak 3 kali")
username = input("masukkan username baru : ")
password = input("masukkan password baru : ")
print("")

k = 0
fail = False
while k < 3 and not fail:
    vUsername = input("konfigurasi username : ")
    vPassword = input("konfigurasi password : ")

    if vUsername != username or vPassword != password:
        fail = True
    else:
        fail = False
            
    k += 1
    print("")
    
if not fail:
    print("Anda berhasil Masuk")
else:
    print("maaf, username dan password salah")





