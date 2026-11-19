print("=== Pendaftaran Anggota Klub Robotika===")
print("=== Input Nama Anggota ===")
nama_anggota = []

while True:
    nama = input("Masukkan nama anggota (atau ketik 'Selesai' untuk berhenti): ").capitalize()
    if nama == "Selesai":
        break
    elif nama.strip() == "":
        print("Nama tidak boleh kosong, ulangi.")
    else:
        nama_anggota.append(nama)

print("\n=== Daftar Anggota ===")
print(f"Nama anggota yang terdaftar: {nama_anggota}")
print(f"Jumlah anggota yang terdaftar: {len(nama_anggota)} orang")

print("\n=== Validasi Nama Anggota ===")
for i in nama_anggota:
    if i == "Admin" or len(i) < 4:
        print(f"Nama anggota {i} tidak valid.")

print("\n=== Pengecekan Penyusup ===")
penghapusan = input("Apakah ada penyusup? (y/n): ").lower()
if penghapusan == "y":
    while True:
        nama_penyusup = input("Masukkan nama penyusup (atau ketik 'Selesai' untuk berhenti): ").capitalize()
        if nama_penyusup == "Selesai":
            break
        elif nama_penyusup.strip() == "":
            print("Nama tidak boleh kosong, ulangi.")
        else:
            if nama_penyusup in nama_anggota:
                nama_anggota.remove(nama_penyusup)
                print(f"Nama penyusup {nama_penyusup} telah dihapus dari daftar anggota.")
            else:
                print(f"Nama penyusup {nama_penyusup} tidak ditemukan dalam daftar anggota.")
else:
    print("Tidak ada penyusup yang dihapus.")

print("\n=== Update Daftar Anggota ===")
print(f"Nama anggota yang terdaftar: {nama_anggota}")
print(f"Jumlah anggota yang terdaftar: {len(nama_anggota)} orang")
