todo = {}

while True:
    print("\n===== MENU TO-DO LIST =====")
    print("1. Tambah Tugas")
    print("2. Tampilkan Tugas")
    print("3. Tandai Tugas Selesai")
    print("4. Hapus Tugas")
    print("5. Jumlah Tugas")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        tugas = input("Masukkan nama tugas: ")
        todo[tugas] = "Belum Selesai"
        print("Tugas berhasil ditambahkan!")

    elif pilihan == "2":
        if len(todo) == 0:
            print("Belum ada tugas.")
        else:
            print("\nDaftar Tugas:")
            for tugas, status in todo.items():
                print(tugas, ":", status)

    elif pilihan == "3":
        tugas = input("Masukkan nama tugas: ")
        if tugas in todo:
            todo[tugas] = "Selesai"
            print("Tugas berhasil diselesaikan!")
        else:
            print("Tugas tidak ditemukan.")

    elif pilihan == "4":
        tugas = input("Masukkan nama tugas: ")
        if tugas in todo:
            del todo[tugas]
            print("Tugas berhasil dihapus!")
        else:
            print("Tugas tidak ditemukan.")

    elif pilihan == "5":
        selesai = 0
        belum = 0

        for status in todo.values():
            if status == "Selesai":
                selesai += 1
            else:
                belum += 1

        print("Jumlah tugas selesai:", selesai)
        print("Jumlah tugas belum selesai:", belum)

    elif pilihan == "6":
        print("Program selesai. Terima kasih!")
        break

    else:
        print("Pilihan tidak tersedia. Silakan coba lagi.")