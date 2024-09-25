# nomor 1
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
    
def menu() :
    print("Pilih operasi yang diinginkan : ")
    print("1. operasi penjumlahan")
    print("2. operasi pengurangan")
    print("3. operasi perkalian")
    print("4. operasi pembagian")

while True :
    menu()
    pilihan = int(input("Operasi Yang Diinginkan = "))
    x = float(input("Masukan angka pertama = "))
    y = float(input("Masukan angka kedua = "))

    if pilihan == 1 :
        print(f"Hasil Penjumlahan", penjumlahan(x,y))
    elif pilihan == 2 :
        print(f"Hasil Pengurangan", pengurangan(x,y))
    elif pilihan == 3 :
        print(f"Hasil Perkalian", perkalian(x,y))
    elif pilihan == 4 :
        print(f"Hasil Pembagian", pembagian(x,y))
    else :
        print("Tidak Valid")

    lanjut = input("Apakah ingin melakukan operasi lagi? (y/n): ")
    if lanjut.lower() != 'y' :
        break



# nomor 2
def operasi() :
    def jumlah() :
        banyak = int(input("Masukan jumlah angka = "))

        if banyak <= 0:
            return "Jumlah angka harus lebih dari 0"
    
        angka_list = []

        for i in range(banyak) :
            angka = int(input(f"Masukan nilai ke-{i+1} = "))
            angka_list.append(angka)
    
        return angka_list

    def digit(angka) :
        return len(str(angka))

    angka_list = jumlah()

    def jumlah_digit(angka_list) :
        return sum(len(str(angka)) for angka in angka_list)

    if isinstance(angka_list, list):
        for angka in angka_list:
            print(f"Jumlah digit dari {angka} = {digit(angka)}")
        print(f"Total digit keseluruhan adalah {jumlah_digit(angka_list)}")
    else:
        print(angka_list)

while True :
    operasi()
    lanjut = input("Apakah ingin melakukan operasi lagi? (y/n): ")
    if lanjut.lower() != 'y' :
        break



# nomor 3
def operasi() :
    banyak = int(input("Masukan jumlah angka = "))

    if banyak <= 0:
        return "Jumlah angka harus lebih dari 0"
    
    angka_list = []

    for i in range(banyak) :
        angka = int(input(f"Masukan nilai ke-{i+1} = "))
        angka_list.append(angka)
    
    rata_rata = sum(angka_list) / len(angka_list)

    angka_list.sort() 
    if len(angka_list) >= 2 :
        tertinggi = angka_list[-2] if len(angka_list) > 1 else angka_list[0]
        terendah = angka_list[1] if len(angka_list) > 1 else angka_list[0]
    else:
        tertinggi = terendah = angka_list[0] if angka_list else None

    return rata_rata, tertinggi, terendah

hasil = operasi()

if isinstance(hasil, str) :
    print("Tidak Valid")
else :
    rata_rata, tertinggi, terendah = hasil
    print(f"Rata-rata =, {rata_rata}")
    print(f"nilai yang lebih rendah dari nilai tertinggi =, {tertinggi}")
    print(f"nilai yang lebih tinggi dari nilai terendah =, {terendah}")



# nomor 4
def is_kabisat(y) :
    return y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)

def dpm(m) :
    if m == 1 :
        return 1
    elif m == 2 :
        return 32
    elif m == 3 :
        return 60
    elif m == 4 :
        return 91
    elif m == 5 :
        return 121
    elif m == 6 :
        return 152
    elif m == 7 :
        return 182
    elif m == 8 :
        return 213
    elif m == 9 :
        return 244
    elif m == 10 :
        return 274
    elif m == 11 :
        return 305
    elif m == 12 :
        return 335
    
def hari(d,m,y) :
    return dpm(m) + d - 1 +(1 if m>2 and is_kabisat(y) else 0)

def tanggal(d,m,y) :
    if hari(d,m,y) % 7 == 1 :
        return "Sabtu"
    elif hari(d,m,y) % 7 == 2 :
        return "Minggu"
    elif hari(d,m,y) % 7 == 3 :
        return "Senin"
    elif hari(d,m,y) % 7 == 4 :
        return "Selasa"
    elif hari(d,m,y) % 7 == 5 :
        return "Rabu"
    elif hari(d,m,y) % 7 == 6 :
        return "Kamis"
    elif hari(d,m,y) % 7 == 0 :
        return "Jum'at"
    
def is_kamis(d,m,y) :
    return tanggal(d+2,m,y) == "Kamis"
    
d = int(input("Masukan Tanggal Dalam Hari = "))
m = int(input("Masukan Tanggal Dalam Bulan = "))
y = int(input("Masukan Tanggal Dalam Tahun = "))

print("Jumlah Hari Adalah", hari(d,m,y), "Harinya adalah hari", tanggal(d,m,y))
print("Apakah 2 hari setelahnya adalah hari kamis?", is_kamis(d,m,y))



# nomor 5
def positif(x) :
    if x > 0 :
        return "Positif"
    elif x == 0 :
        return "Nol"
    else :
        return "Negatif"
    
def operasi() :
    banyak = int(input("Masukan Banyaknya Angka Yang Diinginkan = "))
    angka_list = []

    for i in range(banyak) :
        angka = float(input(f"Masukan Angka ke {i+1} = "))
        angka_list.append(angka)

    for angka in angka_list :
        if angka % 2 == 0 :
            print("Genap")
        else :
            print("Ganjil")
        
    for angka in angka_list :
        hasil = positif(angka)
        print(f"Angka {angka} adalah {hasil}")

while True :
    operasi()

    lanjut = input("Apakah ingin melanjutkan? (y/n) = ")
    if lanjut.lower() != 'y' :
        break