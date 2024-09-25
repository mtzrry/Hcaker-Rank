# latihan 1
def digit_angka(angka) :
    count = 0
    while angka > 0 :
        angka //= 10
        count += 1
    return count

# def total(a,b,c) :
#     return sum(map(digit_angka, (a,b,c)))

def total(a,b,c) :
    return digit_angka(a) + digit_angka(b) + digit_angka(c)

a = abs(int(input("Masukan angka = ")))
b = abs(int(input("Masukan angka = ")))
c = abs(int(input("Masukan angka = ")))
 
print(total(a,b,c))



# latihan 2
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
        pilihan = int(input("Pilih Operasi Yang Diinginkan = "))
    except ValueError :
        print("Pilihan Tidak Valid")
        continue
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

    lanjut = input("Apakah ingi menjalankan operasi lagi? (y/n) = ")
    if lanjut.lower() != 'y' :
        break



# latihan 3
def rataan() :
    banyak = int(input("Berapa banyak angka yang anda inginkan? = "))
    angka_list = []

    for i in range(banyak) :
        angka = float(input(f"angka ke-{i+1} = "))
        angka_list.append(angka)

        rata = sum(angka_list) / len(angka_list)
        tertinggi = max(angka_list)
        terendah = min(angka_list)
    
    return rata, tertinggi, terendah

rata, tertinggi, terendah = rataan()

print(f"Rata-rata = {rata}")
print(f"Nilai Tertinggi = {tertinggi}")
print(f"Nilai Terendah = {terendah}")