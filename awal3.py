# # kalkulator sederhana
# def penjumlahan(x,y) :
#     return x+y
# def pengurangan(x,y) :
#     return x-y
# def perkalian(x,y) :
#     return x*y
# def pembagian(x,y) :
#     if y==0 :
#         return "Tidak terdefinisi" 
#     else :
#         return x/y

# x = float(input("Masukan nilai pertama = "))
# y = float(input("Masukan nilai kedua = "))

# print("penjumlahan:", penjumlahan(x,y))
# print("pengurangan:", pengurangan(x,y))
# print("perkalian:", perkalian(x,y))
# print("pembagian:", pembagian(x,y))



# kalkulator dengan menu operasi
# v1
def penjumlahan(x,y) :
    return x+y
def pengurangan(x,y) :
    return x-y
def perkalian(x,y) :
    return x*y
def pembagian(x,y) :
    if y==0 :
        return "Tidak dapat membagi dengan nol"
    else :
        return x/y
    
def tampilan_menu() :
    print("Pilih operasi yang diinginkan : ")
    print("1. operasi penjumlahan")
    print("2. operasi pengurangan")
    print("3. operasi perkalian")
    print("4. operasi pembagian")

while True :
    tampilan_menu()

    try :
        pilihan = int(input("Operasi yang diinginkan : "))
    except ValueError :
        print("Tidak dapat menjalankan operasi")
        continue
# sebenanarnya pilihan = input integer saja sudah cukup, namun ini untuk error handling

    x = float(input("Masukan nilai pertama = "))
    y = float(input("Masukan nilai kedua = "))

    if pilihan == 1 :
        print("Hasil penjumlahan : ",penjumlahan(x,y))
    elif pilihan == 2 :
        print("Hasil pengurangan : ",pengurangan(x,y))
    elif pilihan == 3 :
        print("Hasil perkalian : ",perkalian(x,y))
    elif pilihan == 4 :
        print("Hasil pembagian : ",pembagian(x,y))
    else :
        print("operasi yang dijalankan hanya sesuai prosedur")
        
    lanjut = input("Apakah ingin melakukan operasi lagi? (y/n): ")
    if lanjut.lower() != 'y':
        break



# v2
# def penjumlahan(x, y):
#     return x + y

# def pengurangan(x, y):
#     return x - y

# def perkalian(x, y):
#     return x * y

# def pembagian(x, y):
#     if y == 0:
#         return "Tidak Terdefinisi"
#     else:
#         return x / y

# def operasi(pilihan, x, y):
#     if pilihan == '1' :
#         print("Hasil Penjumlahan =", penjumlahan(x, y))
#     elif pilihan == '2':
#         print("Hasil Pengurangan =", pengurangan(x, y))
#     elif pilihan == '3':
#         print("Hasil Perkalian =", perkalian(x, y))
#     elif pilihan == '4':
#         print("Hasil Pembagian =", pembagian(x, y))
#     else:
#         print("Operasi Tidak Valid")

# while True:
#     print("Pilih Operasi")
#     print("1. Operasi Penjumlahan")
#     print("2. Operasi Pengurangan")
#     print("3. Operasi Perkalian")
#     print("4. Operasi Pembagian")

#     pilihan = input("Operasi yang diinginkan = ")
#     x = float(input("Masukkan nilai pertama = "))
#     y = float(input("Masukkan nilai kedua = "))

#     operasi(pilihan, x, y)

#     lanjut = input("Apakah ingin melakukan operasi kembali? (y/n) ")
#     if lanjut.lower() != 'y':
#         break



# operasi rata rata tertinggi terendah v1
def hitung() :
    banyak = int(input("berapa banyak angka yang anda ingin gunakan = "))

    angka_list = []

    for i in range(banyak) :
        angka = float(input(f"Masukan nilai ke-{i+1}= "))
        angka_list.append(angka)

    rata = sum(angka_list) / len(angka_list)
    tertinggi = max(angka_list)
    terendah = min(angka_list)

    print(f"Rata-rata = {rata}")
    print(f"Nilai Tertinggi = {tertinggi}")
    print(f"Nilai Terendah = {terendah}")

hitung()



# v2
def hitung() :
    banyak = int(input("berapa banyak angka yang anda ingin gunakan = "))

    angka_list = []

    for i in range(banyak) :
        angka = float(input(f"Masukan nilai ke-{i+1}= "))
        angka_list.append(angka)

        rata = sum(angka_list) / len(angka_list)
        tertinggi = max(angka_list)
        terendah = min(angka_list)

    return rata, tertinggi, terendah
# return untuk menampilkan hasil fungsi yang bisa berupa operasi ataupun nilai variabel
rata, tertinggi, terendah = hitung()

print(f"Rata-rata = {rata}")
print(f"Nilai Tertinggi = {tertinggi}")
print(f"Nilai Terendah = {terendah}")



# kalkulator faktorial dan perpangkatan
import math

def faktorial(x) :
    return math.factorial(x)
def pangkat(x,y) :
    return x**y

def menu_tampilan() :
    print("Pilih Operasi Yang Diinginkan = ")
    print("1. Operasi Faktorial")
    print("2. Operasi Perpangkatan")

while True :
    menu_tampilan()
    pilihan = input("Masukan Input Operasi Yang Diinginkan = ")

    if pilihan == '1' :
        a = int(input("Masukan Nilai = "))
        print(faktorial(a))
    elif pilihan == '2' :
        a = int(input("Masukan Nilai yang dipangkatkan= "))
        b = int(input("Masukan Nilai perpangkatan= "))
        print(pangkat(a,b))
    else :
        print("Operasi Tidak Valid")
    
    lanjut = input("Apakah ingin melakukan operasi lagi? (y/n): ")
    if lanjut.lower() != 'y':
        break