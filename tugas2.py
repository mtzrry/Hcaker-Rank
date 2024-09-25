# nomor 4
def min2(x,y) :
    return (x+y-abs(x-y))/2
def max2(x,y) :
    return (x+y+abs(x-y))/2
def min3(x,y,z) :
    return min2(min2(x,y), z)
def max3(x,y,z) :
    return max2(max2(x,y), z)

def nilai_tengah(x,y,z) :
    return x+y+z-min3(x,y,z)-max3(x,y,z)

x = float(input("Masukan nilai pertama = "))
y = float(input("Masukan nilai kedua = "))
z = float(input("Masukan nilai ketiga = "))

print("Nilai Tengah =", nilai_tengah(x,y,z))

# nomor 4 v2
# def nilai_tengah(x,y,z) :
#     return (x+abs(y-x)+y+z-abs(y-z))/3

# print(nilai_tengah(1,2,3))



# nomor 5
def kecepatan(x,y) :
    if y == 0 :
        return ("Diam ditempat")
    else :
        return x/y

x = int(input("Masukan jarak yang ditempuh (dalam km) = "))
# dalam km
y = int(input("Masukan waktu tempuh (dalam jam) = "))
# dalam jam

print(kecepatan(x,y), "KM/jam")



# nomor 6 v1
def jumlah(angka) :
    return len(str(angka))

a = int(input("Masukan Angka = "))
b = int(input("Masukan Angka = "))
c = int(input("Masukan Angka = "))

def total_digit(a,b,c) :
    return jumlah(a) + jumlah(b) + jumlah(c)

print("Total jumlah digit = ", total_digit(a,b,c))

# nomor 6 v2 
def jumlah_digit(angka) :
    count = 0
    while angka > 0 :
    # while angka > 0 (untuk memastikan secara eksplisit, hanya untuk bilangan positif):
        angka //= 10
# disingkat angka = angka//10, guna menyimpan kembali variabel angka
        count += 1
# disingkat count = count + 1
    return count

def total(a,b,c) :
    return sum(map(jumlah_digit, (a,b,c)))

a = abs(int(input("Masukan angka = ")))
b = abs(int(input("Masukan angka = ")))
c = abs(int(input("Masukan angka = ")))
 
print(total(a,b,c))



# nomor 7
import math

def volume(r1,r2,r3) :
    return 4/3*math.pi*r1*r2*r3

r1 = float(input("jari-jari 1 = "))
r2 = float(input("jari-jari 2 = "))
r3 = float(input("jari-jari 3 = "))

print("Volume bola = ",volume(r1,r2,r3))



# nomor 8
import math

def kombinasi(n,r):
    if r > n:
        return "r tidak boleh lebih besar dari n"
    return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))

n = int(input("Masukkan nilai n: "))
r = int(input("Masukkan nilai r: "))

hasil = kombinasi(n,r)

print(f"Kombinasi dari({n},{r}) = {hasil}")
