jumlah = 0
total_pendapatan = 0
total_jarak = 0
jarak_terjauh = 0

while True:
    jarak = int(input("Masukkan jarak tempuh (km) atau 0 untuk selesai: "))
    if jarak == 0:
        break
    elif jarak < 0:
        print("Jarak tidak boleh negatif. Silakan masukkan jarak yang valid.")
        continue
    jumlah += 1

    if jarak <= 5:
        tarif = 3000
    elif jarak <= 15:
        tarif = 3000 + (jarak - 5) * 1000
    elif jarak > 15:
        tarif = 13000 + (jarak - 15) * 500

    if jumlah % 5 == 0:
        tarif = tarif * 0.5 
        print("Penumpang ke-" + str(jumlah) + " mendapatkan diskon 50%!")

    print("Tarif: Rp", int(tarif))

    total_pendapatan += tarif
    total_jarak += jarak
    if jarak > jarak_terjauh:
        jarak_terjauh = jarak

print("Ringkasan Pendapatan Bus Pak Budi")
print("Total penumpang:", jumlah)
if jumlah > 0:
    print("Total pendapatan: Rp", int(total_pendapatan))
    print("Jarak terjauh: ", jarak_terjauh, "km")
    print("Rata-rata jarak: ", total_jarak / jumlah, "km")
else:
    print("Belum ada penumpang.")