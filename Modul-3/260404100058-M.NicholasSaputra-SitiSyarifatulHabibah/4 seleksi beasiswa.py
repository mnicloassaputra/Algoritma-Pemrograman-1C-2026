penuh = 0

for i in range(1, 11):
    print("Mahasiswa ke-" + str(i))
    nama = input("Nama : ")
    ipk = float(input("IPK : "))
    
    if ipk < 3.00:
        print("Hasil: " + nama + " - TIDAK memenuhi syarat (IPK < 3,00)")
        print("")
        continue
    
    penghasilan = int(input("Penghasilan orang tua/bln : "))

    if penghasilan <= 3000000:
        print("Hasil: " + nama + " - Beasiswa PENUH")
        penuh = penuh + 1
    elif penghasilan <= 5000000:
        print("Hasil: " + nama + " - Beasiswa SEBAGIAN")
    else:
        print("Hasil: " + nama + " - Tidak mendapat beasiswa")

    print("")

    if penuh == 3:
        print("Kuota beasiswa penuh (3 orang) terpenuhi. Seleksi dihentikan.")
        break

print("Total penerima beasiswa penuh: " + str(penuh))