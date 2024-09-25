def hargaAkhir(harga : int, kategori : str, VIP : bool, lokasi : str, hari : str) -> int:
    if int(harga) >0 :
        if hari == "Jumat" or hari == "Sabtu" or hari == "Minggu" or hari == "Rabu":
            if kategori == "elektronik":
                if VIP:
                    if hari == "Jumat" or hari == "Sabtu":
                        if lokasi == "dalam negeri":
                            return int(((harga * 0.7) * 0.95) * 1.1)
                        if lokasi == "luar negeri":
                            return int(((harga * 0.7) * 0.95) * 1.2)
                    elif hari == "Minggu":
                        if lokasi == "dalam negeri":
                            return int(((harga * 0.7) * 1.05) * 1.1)
                        if lokasi == "luar negeri":
                            return int(((harga * 0.7) * 1.05) * 1.2)
                    elif hari == "Rabu":
                        if lokasi == "dalam negeri":
                            return int((harga * 0.7) * 1.1)
                        if lokasi == "luar negeri":
                            return int((harga * 0.7) * 1.2)
                else:
                    if hari == "Jumat" or hari == "Sabtu":
                        if lokasi == "dalam negeri":
                            return int((harga * 0.9) * 1.1)
                        if lokasi == "luar negeri":
                            return int((harga * 0.9) * 1.2)
                    elif hari == "Minggu":
                        if lokasi == "dalam negeri":
                            return int(((harga * 0.9) * 1.05) * 1.1)
                        if lokasi == "luar negeri":
                            return int(((harga * 0.9) * 1.05) * 1.2)
                    elif hari == "Rabu":
                        if lokasi == "dalam negeri":
                            return int((harga * 0.9) * 1.1)
                        if lokasi == "luar negeri":
                            return int((harga * 0.9) * 1.2)
            elif kategori == "pakaian":
                if VIP:
                    if hari == "Jumat" or hari == "Sabtu":
                        if lokasi == "dalam negeri":
                            return int(((harga * 0.8) * 0.95) * 1.1)
                        if lokasi == "luar negeri":
                            return int(((harga * 0.8) * 0.95) * 1.2)
                    elif hari == "Minggu":
                        if lokasi == "dalam negeri":
                            return int(((harga * 0.8) * 1.05) * 1.1)
                        if lokasi == "luar negeri":
                            return int(((harga * 0.8) * 1.05) * 1.2)
                    elif hari == "Rabu":
                        if lokasi == "dalam negeri":
                            return int((harga * 0.8 * 0.95) * 1.1)
                        if lokasi == "luar negeri":
                            return int((harga * 0.8 * 0.95) * 1.2)
                else:
                    if hari == "Jumat" or hari == "Sabtu":
                        if lokasi == "dalam negeri":
                            return int((harga * 0.95) * 1.1)
                        if lokasi == "luar negeri":
                            return int((harga * 0.95) * 1.2)
                    elif hari == "Minggu":
                        if lokasi == "dalam negeri":
                            return int(((harga * 0.95) * 1.05) * 1.1)
                        if lokasi == "luar negeri":
                            return int(((harga * 0.95) * 1.05) * 1.2)
                    elif hari == "Rabu":
                        if lokasi == "dalam negeri":
                            return int((harga * 0.95 * 0.95) * 1.1)
                        if lokasi == "luar negeri":
                            return int((harga * 0.95 * 0.95) * 1.2)
            elif kategori == "makanan":
                if VIP:
                    if hari == "Jumat" or hari == "Sabtu":
                        if lokasi == "dalam negeri":
                            return int(((harga * 0.85) * 0.95) * 1.1)
                        if lokasi == "luar negeri":
                            return int(((harga * 0.85) * 0.95) * 1.2)
                    elif hari == "Minggu":
                        if lokasi == "dalam negeri":
                            return int(((harga * 0.85) * 1.05) * 1.1)
                        if lokasi == "luar negeri":
                            return int(((harga * 0.85) * 1.05) * 1.2)
                    elif hari == "Rabu":
                        if lokasi == "dalam negeri":
                            return int((harga * 0.85) * 1.1)
                        if lokasi == "luar negeri":
                            return int((harga * 0.85) * 1.2)
                else:
                    if hari == "Jumat" or hari == "Sabtu":
                        if lokasi == "dalam negeri":
                            return int((harga * 0.98) * 1.1)
                        if lokasi == "luar negeri":
                            return int((harga * 0.98) * 1.2)
                    elif hari == "Minggu":
                        if lokasi == "dalam negeri":
                            return int(((harga * 0.98) * 1.05) * 1.1)
                        if lokasi == "luar negeri":
                            return int(((harga * 0.98) * 1.05) * 1.2)
                    elif hari == "Rabu":
                        if lokasi == "dalam negeri":
                            return int((harga * 0.98) * 1.1)
                        if lokasi == "luar negeri":
                            return int((harga * 0.98) * 1.2)
        elif hari == "Senin" or hari == "Selasa" or hari == "Kamis":
            if kategori == "elektronik" and VIP:
                if lokasi == "dalam negeri":
                    return int(harga * 0.7 * 1.1)
                else:
                    return int(harga * 0.7 * 1.2)
            elif kategori == "elektronik":
                if lokasi == "dalam negeri":
                    return int(harga * 0.9 * 1.1)
                else:
                    return int(harga * 0.9 * 1.2)
            elif kategori == "pakaian" and VIP:
                if lokasi == "dalam negeri":
                    return int(harga * 0.8 * 1.1)
                else:
                    return int(harga * 0.8 * 1.2)
            elif kategori == "pakaian":
                if lokasi == "dalam negeri":
                    return int(harga * 0.95 * 1.1)
                else:
                    return int(harga * 0.95 * 1.2)
            elif kategori == "makanan" and VIP:
                if lokasi == "dalam negeri":
                    return int(harga * 0.85 * 1.1)
                else:
                    return int(harga * 0.85 * 1.2)
            elif kategori == "makanan":
                if lokasi == "dalam negeri":
                    return int(harga * 0.98 * 1.1)
                else:
                    return int(harga * 0.98 * 1.2)
            else:
                if lokasi == "dalam negeri" and hari == "Minggu" :
                    return int(harga*1.05*1.1)
                elif lokasi == "luar negeri" and hari == "Minggu" :
                    return int(harga*1.05*1.2)
                elif (hari == "Jumat" or hari == "Sabtu") and VIP and lokasi == "dalam negeri" :
                    return int(harga*0.95*1.1)
                elif (hari == "Jumat" or hari == "Sabtu") and VIP and lokasi == "luar negeri" :
                    return int(harga*0.95*1.2)
                else :
                    if lokasi == "dalam negeri" :
                        return int(harga*1.1)
                    return int(harga*1.2)

print(eval(input()))



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