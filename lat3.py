def positif(x) :
    if x > 0 :
        return "Positif"
    elif x == 0 :
        return "Nol"
    else :
        return "Negatif"
    
def tabel() :
    banyak = int(input("Berapa banyak angka yang anda inginkan? = "))
    angka_list = []

    for i in range(banyak) :
        angka = float(input(f"angka ke-{i+1} = "))
        angka_list.append(angka)
        
    for angka in angka_list :
        if angka % 2 == 0 :
            print("Genap")
        else :
            print("Ganjil")

    for angka in angka_list :
        hasil = positif(angka)
        print(f"{angka} adalah {hasil}")

while True :
    tabel()

    lanjut = input("Apakah ingin melanjutkan (y/n) = ")
    if lanjut.lower() != 'y' :
        break