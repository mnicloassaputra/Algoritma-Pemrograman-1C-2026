print("=== Sistem Pendataan Inventaris PC ===")

print("=== Input Jumlah PC ===")
while True:
    jumlah_pc = int(input("Masukkan jumlah PC yang ingin didata: "))
    if jumlah_pc <= 0:
        print("Jumlah PC harus lebih dari 0, ulangi.")
    else:
        break

inventaris_pc = []
for i in range(jumlah_pc):
    print(f"\n=== Input Data PC ke-{i + 1} ===")

    nama_pc = input("Masukkan nama PC: ").upper()
    status_pc = input("Masukkan status PC (Normal/Rusak): ").capitalize()

    ram = input("Masukkan kapasitas RAM (dalam GB): ")

    data_pc = [nama_pc, status_pc, ram]
    inventaris_pc.append(data_pc)

def evaluasi_pc(status_pc, ram):
    if status_pc == "Normal" and int(ram) >= 8:
        return "Layak"
    else:
        return "Tidak Layak"

print("\n=== Hasil Evaluasi Inventaris PC ===")
for pc in inventaris_pc:
    nama_pc = pc[0]
    status_pc = pc[1]
    ram = pc[2]

    try:
        hasil = evaluasi_pc(status_pc, ram)
    except (ValueError, TypeError):
        hasil = "Format RAM Kacau"

    hasil_cetak = f'{{ "PC": "{nama_pc}", "Status": "{hasil}" }}'
    print(hasil_cetak)

