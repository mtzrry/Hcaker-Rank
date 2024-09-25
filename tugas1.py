# nomor 1
def math1(x) :
    return x*60
def math2(x) :
    return math1(x*60)
def math3(x) :
    return math2(x*24)
def math4(x) :
    return math3(x*365)
def waktu (tahun,hari,jam,menit,detik) :
    return (math4(tahun) + math3(hari) + math2(jam) + math1(menit) + detik)

tahun = int(input("Berapa tahun = "))
hari = int(input("Berapa hari = "))
jam = int(input("Berapa jam = "))
menit = int(input("Berapa menit = "))
detik = int(input("Berapa detik = "))

print(waktu(tahun,hari,jam,menit,detik))



# nomor 2 cara 1
def fx2(x) :
    return x*x
def x1(a,b,c) :
    return (-b+(fx2(b)-4*a*c)**0.5)/2*a
def x2(a,b,c) :
    return (-b-(fx2(b)-4*a*c)**0.5)/2*a
def jumlah(a,b,c) :
    return fx2(x1(a,b,c)) + fx2(x2(a,b,c))

a = int(input("Masukan nilai a = "))
b = int(input("Masukan nilai b = "))
c = int(input("Masukan nilai c = "))

print(jumlah(a,b,c))

# nomor 2 cara 1 (long version)
# def fx2(x) :
#     return x*x
# def diskriminan(a,b,c) :
#     return fx2(b)-4*a*c
# def x1(a,b,c) :
#     return (-b+(diskriminan(a,b,c))**0.5)/2*a
# def x2(a,b,c) :
#     return (-b-(diskriminan(a,b,c))**0.5)/2*a
# def jumlah(a,b,c) :
#     return fx2(x1(a,b,c))+ fx2(x2(a,b,c))

# a = int(input("Masukan nilai a = "))
# b = int(input("Masukan nilai b = "))
# c = int(input("Masukan nilai c = "))

# print(jumlah(a,b,c))

# nomor 2 cara 2
def x1(a,b,c) :
    return -b/a
# x1 adalah hasil penjumlahan akar fungsi kuadrat
def x2(a,b,c) :
    return c/a
# x2 adalah hasil perkalian akar fungsi kuadrat
def fx2(x) :
    return x*x
def f2(x) :
    return x+x
def fungsi(a,b,c) :
    return fx2(x1(a,b,c))-f2(x2(a,b,c))

a = int(input("Masukan nilai a = "))
b = int(input("Masukan nilai b = "))
c = int(input("Masukan nilai c = "))

print(fungsi(a,b,c))

# nomor 2 cara 2 (shortcut version)
# def fungsi (a,b,c) :
#     return (-b/a)**2-(c/a)*2

# a = int(input("Masukan nilai a = "))
# b = int(input("Masukan nilai b = "))
# c = int(input("Masukan nilai c = "))

# print(fungsi(a,b,c))



# nomor 3
def cumlaude(x,y) :
    return x>=3.5 and y<=54

x = int(input("Masukan nilai IPK = "))
y = int(input("Masukan jumlah bulan = "))

print(cumlaude(x,y))



# nomor 4
def kabisat(x) :
    return x%400==0 or (x%4==0 and x%100!=0)
    # if x%400==0 or (x%4==0 and x%100!=0) :
    #     return "Tahun Kabisat"
    # else :
    #     return "Bukan Tahun Kabisat"

# y = int(input("Masukan tahun = "))

# print(kabisat(y))
x = int(input("Masukan tahun = "))

print(kabisat(x))



# nomor 5
# bunga majemuk
def modal(n,r) :
    return 1+r/n
def hasil(n,r,t) :
    return modal(n,r)**(n*t)
def bungatotal(p,n,r,t) :
    return p*hasil(n,r,t)

p = int(input("Masukan uang awal = "))
# untuk nominal ditulis angkanya saja dan tanpa titik
r = float(input("Masukan bunga per tahun = "))
# untuk contoh pada r, bila bunga pertahun adalah 5% maka ditulis 0.05
n = int(input("bunga yang tadi didapat dalam kurun waktu(tahun)? = "))
# langsung tulis dalam bentuk angka
t = int(input("waktu berinvestasi(tahun) = "))
# langsung tulis dalam bentuk angka

print(bungatotal(p,n,r,t))