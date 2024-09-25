# nomor 1
def fahrenheit(x) :
    return (9/5)*x + 32
def reamur(x) :
    return (4/5)*x
def kelvin(x) :
    return x + 273.15

def menu() :
    print("Pilih nilai konversi = ")
    print()
    print("1. Konversi Celcius ke Fahrenheit")
    print("2. Konversi Celcius ke Reamur")
    print("3. Konversi Celcius ke Kelvin")
    print()

while True :
    menu()
    pilihan = input("Pilih operasi konversi = ")
    x = float(input("Masukan besaran dalam Celcius = "))

    if pilihan == '1' :
        print()
        print(fahrenheit(x), "Derajat Fahrenheit")
    elif pilihan == '2' :
        print()
        print(reamur(x), "Derajat Reamur")
    elif pilihan == '3' :
        print()
        print(kelvin(x), "Derajat Kelvin")
    else :
        print("Tidak Valid")

    print()
    lanjut = str(input("Apakah ingin melanjutkan operasi (y/n) = "))
    if lanjut.lower() != 'y' :
        break



# nomor 2
def wujud_air(a) :
    if a <= 0 :
        return "berwujud Padat/Es"
    elif a>0 and a<100 :
        return "berwujud cair"
    else :
        return "berwujud Uap/Gas"
    
a = float(input("Masukan nilai suhu air = "))
print()
print("maka air akan", wujud_air(a))



# nomor 3
def segitiga(a,b,c) :
    if a == b == c :
        return "Segi tiga sama sisi"
    elif (a == b and (a>c or a<c)) or (b == c and (b>a or b<a)) or (a == c and (a>b or a<b)) :
        return "Segi tiga sama kaki"
    else :
        return "Segi tiga sembarang"

a = int(input("Masukan panjang sisi a = "))
b = int(input("Masukan panjang sisi b = "))
c = int(input("Masukan panjang sisi c = "))

print("Wujud nya adalah", segitiga(a,b,c))



# nomor 4
def fx2(x) :
    return x*x
def x1(a,b,c) :
    if a != 0 :
        return -1*((b+(fx2(b)-4*a*c)**0.5)/(2*a))
    else :
        return "Tidak Valid"
def x2(a,b,c) :
    if a != 0 :
        return -1*((b-(fx2(b)-4*a*c)**0.5)/(2*a))
    else :
        return "Tidak Valid"
def pembagian(a,b,c) :
        if x1(a,b,c) > x2(a,b,c) :
            return x1(a,b,c) / x2(a,b,c)
        elif x2(a,b,c) > x1(a,b,c) :
            return x2(a,b,c) / x1(a,b,c)
        elif x1(a,b,c) == x2(a,b,c) :
            return x1(a,b,c) / x2(a,b,c)
        else :
            return "Tidak Valid"

a = int(input("Masukan nilai a = "))
b = int(input("Masukan nilai b = "))
c = int(input("Masukasn nilai c = "))

print(pembagian(a,b,c))