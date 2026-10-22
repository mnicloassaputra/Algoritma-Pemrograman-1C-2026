jumlah_A = 0
jumlah_B = 0
jumlah_C = 0
jumlah_D = 0
jumlah_E = 0
total_nilai = 0
tertinggi = -1
terendah = 101
nama_tertinggi = ""
nama_terendah = ""

n = int(input("input berapa mahasiswa? : "))

for i in range(1, n+1):
    print(f"\nMahasiswa ke-{i}")
    nama = input("Nama : ")
    tugas = float(input("Nilai tugas : "))
    uts = float(input("Nilai UTS : "))
    uas = float(input("Nilai UAS : "))

    akhir = 0.3 * tugas + 0.3 * uts + 0.4 * uas

    if akhir >= 85:
        kategori = "A"
        jumlah_A += 1
    elif akhir >= 75:
        kategori = "B"
        jumlah_B += 1
    elif akhir >= 65:
        kategori = "C"
        jumlah_C += 1
    elif akhir >= 50:
        kategori = "D"
        jumlah_D += 1
    else:
        kategori = "E"
        jumlah_E += 1

    print(f"-> {nama} | Nilai tugas: {tugas} | Nilai UTS: {uts} | Nilai UAS: {uas} | Akhir: {akhir:.1f} | Kategori: {kategori}")

    total_nilai += akhir
    if akhir > tertinggi:
        tertinggi = akhir
        nama_tertinggi = nama
    if akhir < terendah:
        terendah = akhir
        nama_terendah = nama

print("\nREKAP KELAS")
print(f"Jumlah A: {jumlah_A}")
print(f"Jumlah B: {jumlah_B}")
print(f"Jumlah C: {jumlah_C}")
print(f"Jumlah D: {jumlah_D}")
print(f"Jumlah E: {jumlah_E}")
print(f"Tertinggi: {tertinggi:.1f} ({nama_tertinggi})")
print(f"Terendah : {terendah:.1f} ({nama_terendah})")
print(f"Rata-rata: {total_nilai/n:.1f}")
