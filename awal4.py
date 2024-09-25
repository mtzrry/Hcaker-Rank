print("Fungsi Rata-Rata")
    
def jumlah() :
    banyak = int(input("Masukan jumlah angka = "))

    if banyak <= 0:
        return "Jumlah angka harus lebih dari 0"
    
    angka_list = []

    for i in range(banyak) :
        angka = float(input(f"Masukan nilai ke-{i+1} = "))
        angka_list.append(angka)

    rata = sum(angka_list)/len(angka_list)

    angka_list.sort ()

    if len(angka_list) >= 2 :
        tertinggi = angka_list[-2] if len(angka_list) > 1 else angka_list[0]
        terendah = angka_list[1] if len(angka_list) > 1 else angka_list[0]
    else:
        tertinggi = terendah = angka_list[0] if angka_list else None

    return rata, tertinggi, terendah

result = jumlah()

if isinstance(result, str) :  # Jika result adalah string (pesan error)
    print(result)
else:
    rata, tertinggi, terendah = result
    print(f"Rata-rata = {rata}")
    print(f"Nilai Tertinggi ke-2 = {tertinggi}")
    print(f"Nilai Terendah ke-2 = {terendah}")