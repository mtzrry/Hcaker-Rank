#  nomor 1
def jam(j,m,s) :
    if j>=0 and j<=59 and m>=0 and m<=59 and s>=0 and s<=59 :
        return f"Jam: {j}, Menit: {m}, Detik: {s}"
    else :
        return "Waktu tidak valid"
    
print(eval(input()))

# nomor 2
def monitor_pesawat(x,y,z):
    if y>900 or y<200 :
        return "Kecepatan Berbahaya"
    elif x>12000 :
        return "Terlalu Tinggi"
    elif z<20 :
        return "Bahan Bakar Rendah"
    elif x<5000 and (y>=200 and y<=900) and z>50 :
        return "Aman untuk Mendarat"
    else :
        return "Berjalan Normal"
    
print(eval(input()))

# nomor 3
def fx2(x) :
    return x*x
def fx(x) :
    return x**0.5
def jalanSemut(x,y,z):
    if x<=1000 and x>=1 and y<=1000 and y>=1 and z<=1000 and z>=1 :
        d1 = fx(fx2(x+y)+fx2(z))
        d2 = fx(fx2(x+z)+fx2(y))
        d3 = fx(fx2(y+z)+fx2(x))
        return round(min(d1,d2,d3), 3)

print(eval(input()))

# nomor 4
def BelajarTenang(dB, m):
    if dB>=1 and dB<=1000000 and m>=1 and m<=1000000 :
        jarak_minimal = 15*10**((dB-40)/20)
        if m>= jarak_minimal :
            return f"{round((jarak_minimal), 3)} meter"
        else : 
            return "Isi bensin dulu, bang"
print(eval(input()))

# nomor 5
def denumeratorSeq(x) :
    if ((10**(len(x))-1) / int(x)) % 1 == 0 :
        return f"Ada: {int((10**(len(x))-1) / int(x))}"
    else :
        return "Tidak ada"
    
print(eval(input()))

# nomor 6
def f(x) :
    return 3*x**2+2*x-5
def gradien(a,b) :
    return (f(a)-f(b))/(a-b)

print(eval(input()))

# nomor 7
def pajak(harga,lokasi) :
    if lokasi == "dalam negeri" :
        return harga*1.1
    else :
        return harga*1.2
def diskon(harga,kategori,VIP) :
    if VIP :
        if kategori == "elektronik" :
            return harga*0.7
        elif kategori == "pakaian" :
            return harga*0.8
        elif kategori == "makanan" :
            return harga*0.85
        else :
            return harga
    else :
        if kategori == "elektronik" :
            return harga*0.9
        elif kategori == "pakaian" :
            return harga*0.95
        elif kategori == "makanan" :
            return harga*0.98
        else :
            return harga
def hari_pembelian(harga,hari,VIP,kategori) :
    if (hari == "Jumat" or hari == "Sabtu") and VIP :
        return harga*0.95
    elif hari == "Minggu" :
        return harga*1.05
    elif hari == "Rabu" and kategori == "pakaian":
        return harga*0.95
    else :
        return harga
    
def hargaAkhir(harga : int, kategori : str, VIP : bool, lokasi : str, hari : str) -> int:
    if harga > 0 :
        return int(pajak((hari_pembelian((diskon(harga,kategori,VIP)),hari,VIP,kategori)),lokasi))
    
print(eval(input()))

# nomor 8
def min2(x, y): return y if x > y else x

def max2(x, y): return x if x > y else y

def min3(x, y, z): return min2(min2(x, y), z)

def max3(x, y, z): return max2(max2(x, y), z)

def ahli(AS, AM, AIP):
    return max3(AS, AM, AIP) - min3(AS, AM, AIP)

def rata_rata(D) :
    if D == "senin" : return float(15000/3)
    elif D == "selasa" : return float(14000/3)
    elif D == "rabu" : return float(11000/3)
    elif D == "kamis" : return float(7000/3)
    elif D == "jumat" : return float(9000/3)
    elif D == "sabtu" : return float(6800/3)
    elif D == "minggu" : return float(3000/3)

def lama_waktu(X, Y):
    return (Y - X)

def EstimateGreatLib(D, X, Y, SS, SR, AS, AM, AIP, R):
    ahli_value = ahli(AS, AM, AIP)
    rata_rata_D = rata_rata(D)

    if X >= SR and Y <= SS: return round(lama_waktu(X, Y) * ahli_value / rata_rata_D, 5)
    elif X < SR and Y > SR and Y <= SS: return round(((lama_waktu(X, SR) * ahli_value * (R / 100) / rata_rata_D) + (lama_waktu(SR, Y) * ahli_value / rata_rata_D)) / 2, 5)
    elif X >= SR and X < SS and Y > SS: return round(((lama_waktu(X, SS) * ahli_value / rata_rata_D) + (lama_waktu(SS, Y) * ahli_value * (R / 100) / rata_rata_D)) / 2, 5)
    elif X < SR and Y > SS: return round(((lama_waktu(X, SR) * ahli_value * (R / 100) / rata_rata_D) + (lama_waktu(SR, SS) * ahli_value / rata_rata_D) + (lama_waktu(SS, Y) * ahli_value * (R / 100) / rata_rata_D)) / 3, 5)
    elif (X < SR and Y <= SR) or (X >= SS and Y > SS): return round(((lama_waktu(X, Y)) * ahli_value * (R / 100) / rata_rata_D), 5)

print(eval(input()))