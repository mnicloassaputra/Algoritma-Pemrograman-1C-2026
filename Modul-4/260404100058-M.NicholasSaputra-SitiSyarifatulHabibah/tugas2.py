gaji_pokok = 100000
shift_malam = 50000
total_gaji = 0

for hari in range(1,8):
    print(f"  Hari ke - {hari}    ")

    while True:
        jam_lembur = int(input("Masukkan jam lembur (0-8): "))
        if jam_lembur in [0, 1, 2, 3, 4, 6, 8]:
            break
        else:
            print("Jumlah lembur tidak sesuai, silakan ulangi!")
    
    if 1 <= jam_lembur <= 3:
        upah_lembur = jam_lembur * 25000
    elif jam_lembur == 4:
        upah_lembur = 100000
    elif jam_lembur == 6:
        upah_lembur = 200000
    elif jam_lembur == 8:
        upah_lembur = 300000
    else:
        upah_lembur = 0

    jawab_shift = input("Shift malam (y/n)? ")
    if jawab_shift == 'y':
        upah_shift = shift_malam
    else:
        upah_shift = 0
    
    gaji_harian = gaji_pokok + upah_lembur + upah_shift
    total_gaji += gaji_harian
    print(f"Gaji Hari ke-{hari}: Rp{gaji_harian:,}")

print(f"TOTAL GAJI MINGGUAN: Rp{total_gaji:,}")