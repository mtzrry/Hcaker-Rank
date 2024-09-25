# nomor 1
def min2(x,y) :
    return (x+y-abs(x-y))/2
def max2(x,y) :
    return (x+y+abs(x-y))/2
def min3(x,y,z) :
    return min2(min2(x,y),z)
def max3(x,y,z) :
    return max2(max2(x,y),z)

def nilai_tengah(x,y,z) :
    return x+y+z-max3(x,y,z)-min3(x,y,z)

print(nilai_tengah(1,2,3))



# nomor 2
def banyak_nilai() :
    banyak = int(input("Berapa Banyak Nilai ? = "))

    if banyak != 5 :
        return "Jumlah Nilai Harus 5"
    
    angka_list = []

    for i in range(banyak) :
        angka = float(input(f"Masukan nilai ke-{i+1} = "))
        angka_list.append(angka)

    return angka_list

def nilai(angka) :
    if angka <= 100 and angka >=80 :
        return "a"
    elif angka < 80 and angka >= 60 :
        return "b"
    elif angka < 60 and angka >= 40 :
        return "c"
    elif angka < 40 and angka >= 20 :
        return "d"
    elif angka < 20 and angka >= 0 :
        return "e"
    
def syarat_nilai(angka_list) :
    for angka in angka_list :
        if nilai(angka)== "a" or nilai(angka)== "b" :
            return True
        else :
            return False
    
def status(a) :
    return a == "aktif"

def semester(b) :
    return b >= 3 and b <= 8

def ipk(c) :
    return c>= 3.3 and c <= 4

def syarat_beasiswa(a,b,c,angka_list) :
    if  status(a) and semester(b) and ipk(c) and syarat_nilai(angka_list) :
        return "Dapat Beasiswa"
    else :
        return"Tidak Dapat Beasiswa"

angka_list = banyak_nilai()

if isinstance(angka_list, list) :
    a = str(input("Status anda(aktif/tidak)? = "))
    b = int(input("Mahasiswa Semester? = "))
    c = float(input("IPK Anda? = "))

    print(syarat_beasiswa(a,b,c,angka_list))

else :
    print(angka_list)