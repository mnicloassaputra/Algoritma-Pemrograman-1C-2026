jumlah_penuh = 0

for i in range(10):
    if jumlah_penuh == 3:
        break

    nama = input("Nama mahasiswa: ")
    ipk = float(input("IPK: "))

    if ipk < 3.00:
        print("Tidak memenuhi syarat")
        continue

    penghasilan = int(input("Penghasilan orang tua: "))

    if penghasilan <= 3000000:
        print("Beasiswa penuh")
        jumlah_penuh += 1
    elif penghasilan <= 5000000:
        print("Beasiswa sebagian")
    else:
        print("Tidak mendapat beasiswa")

print("Jumlah beasiswa penuh:", jumlah_penuh)