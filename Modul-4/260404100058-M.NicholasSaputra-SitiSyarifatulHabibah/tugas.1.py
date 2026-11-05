jumlah_baris = int(input("Masukkan jumlah baris lampu: "))
lampu_per_baris = int(input("Masukkan jumlah lampu per baris: "))

print("pemeriksaan lampu")

for baris in range(1, jumlah_baris + 1):
    print(f"Baris {baris}:")

    for lampu in range(1, lampu_per_baris + 1):
        
        if lampu % 3 == 0:
            print(f"  Lampu {lampu}: Mengalami gangguan")
        else:
            print(f"  Lampu {lampu}: Berfungsi normal")

print("pemeriksaan selesai, periksa sumber listrik utama taman")