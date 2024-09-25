# def max2(a,b) :
#     if a >= b :
#         return a
#     else :
#         return b
    
# print(max2(1,4))



# def max3(a,b,c) :
#     if a>b :
#         if a>c :
#             return a
#         else :
#             return c
#     else :
#         if b>c :
#             return b
#         else :
#             return c
        
# a = int(input("Masukan Nilai A = "))
# b = int(input("Masukan Nilai B = "))
# c = int(input("Masukan Nilai C = "))

# print("Bilangan Terbesar", max3(a,b,c))



def max3(a,b,c) :
    if (a>b) and (a>c) :
        return a
    elif (b>a) and (b>c) :
        return b
    elif (c>a) and (c>b) :
        return c
    
def min3(a,b,c) :
    if (a<b) and (a<c) :
        return a
    elif (b<a) and (b<c) :
        return b
    elif (c<a) and (c<b) :
        return c

def operasi(pilihan) :
    if pilihan == '1' :
        return print(max3(a,b,c))
    elif pilihan == '2' :
        return print(min3(a,b,c))

def menu() :
    print("Pilih Operasi = ")
    print("1.Mencari Nilai Maksimum = ")
    print("2.Mencari Nilai Minimum = ")

while True :
    menu()
    pilihan = input("Pilih Operasi yang diinginkan = ")
    a = int(input("Masukan Nilai A = "))
    b = int(input("Masukan Nilai B = "))
    c = int(input("Masukan Nilai C = "))
    
    print("Bilangan Terbesar", max3(a,b,c))
    
    lanjut = input("Apakah ingin melanjutkan (y/n)")
    if lanjut.lower() != 'y' :
        break



# def tahun(y) :
#     if y%400 == 0 or (y%4 == 0 and y%100 != 0) :
#         return "Tahun Kabisat"
#     else :
#         return "Bukan Tahun Kabisat"
    
# while True :

#     y = int(input("Masukan Tahun = "))
#     print(tahun(y))

#     lanjut = input("Apakah ingin melanjutkan (y/n)")
#     if lanjut.lower() != 'y' :
#         break
