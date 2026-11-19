print("=== Penjadwalan shift Asisten Laboratorium ===")

asisten_awal_list = []

print("=== Input Nama Asisten ===")
while True:
    nama_asisten_awal = input("Masukkan nama asisten (atau ketik 'Cukup' untuk berhenti): ").capitalize()
    if nama_asisten_awal == "Cukup":
        break
    elif nama_asisten_awal.strip() == "":
        print("Nama tidak boleh kosong, ulangi.")
    else:
        asisten_awal_list.append(nama_asisten_awal)
asisten_awal_tuple = tuple(asisten_awal_list)

print("\n=== Input Nama Asisten Baru ===")
while True:
    nama_asisten_baru = input("Masukkan nama asisten baru (atau ketik 'Cukup' untuk berhenti): ").capitalize()
    if nama_asisten_baru == "Cukup":
        break
    elif nama_asisten_baru.strip() == "":
        print("Nama tidak boleh kosong, ulangi.")
    else:
        asisten_baru_tuple = (nama_asisten_baru,)

asisten_final_tuple = asisten_awal_tuple + asisten_baru_tuple

hari_list = []

print("\n=== Input Hari ===")
while True:
    hari = input("Masukkan hari (atau ketik 'Cukup' untuk berhenti): ").capitalize()
    if hari == "Cukup":
        break
    elif hari.strip() == "":
        print("Hari tidak boleh kosong, ulangi.")
    else:
        hari_list.append(hari)
hari_tuple = tuple(hari_list)

print("\n=== Pengecualian Jadwal ===")
while True:
    nama_pengecualian = input("Masukkan nama asisten yang ingin dikecualikan dari penjadwalan (atau ketik 'Tidak Ada' jika tidak ada): ").capitalize()
    hari_pengecualian = input("Masukkan hari yang ingin dikecualikan dari penjadwalan (atau ketik 'Tidak Ada' jika tidak ada): ").capitalize()
    if nama_pengecualian == "Tidak Ada" and hari_pengecualian == "Tidak Ada":
        break
    elif nama_pengecualian.strip() == "" or hari_pengecualian.strip() == "":
        print("Nama dan hari tidak boleh kosong, ulangi.")
    else:
        print(f"Nama asisten yang dikecualikan: {nama_pengecualian}, Hari yang dikecualikan: {hari_pengecualian}")
        break

print("\n=== Jadwal Asisten Laboratorium ===")
for asisten in asisten_final_tuple:
    for hari in hari_tuple:
        if nama_pengecualian == asisten and hari_pengecualian == hari:
            continue
        else:
            print(f"{asisten} - {hari}")
