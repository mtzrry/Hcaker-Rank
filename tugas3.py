def is_kabisat(y) :
    return y%400 == 0 or (y%4 == 0 and y%100 != 0) 
    
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
    
def harike1900(d,m,y) :
    return dpm(m) + d - 1 +(1 if m>2 and is_kabisat(y) else 0)

def hari(d,m,y):
    if harike1900(d,m,y) % 7 == 1 :
        return "Sabtu"
    elif harike1900(d,m,y) % 7 == 2 :
        return "Minggu"
    elif harike1900(d,m,y) % 7 == 3 :
        return "Senin"
    elif harike1900(d,m,y) % 7 == 4 :
        return "Selasa"
    elif harike1900(d,m,y) % 7 == 5 :
        return "Rabu"
    elif harike1900(d,m,y) % 7 == 6 :
        return "Kamis"
    elif harike1900(d,m,y) % 7 == 0 :
        return "Jum'at"

def is_kamis(d,m,y) :
    return hari(d + 2,m,y) == "Kamis" 
    
d = int(input("Masukan tanggal = "))
m = int(input("Masukan bulan = "))
y = int(input("Masukan tahun = "))

print("jumlah hari",harike1900(d,m,y),"dan harinya adalah",f"{hari(d,m,y)}")
print(f"Apakah 2 hari setelahnya adalah hari Kamis?", is_kamis(d,m,y))