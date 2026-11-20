playlist = {}

while True:
    print("\n===== MENU PLAYLIST MUSIK =====")
    print("1. Membuat Playlist")
    print("2. Menambah Lagu")
    print("3. Menampilkan Semua Playlist")
    print("4. Mencari Lagu")
    print("5. Menghapus Lagu")
    print("6. Menghapus Playlist")
    print("7. Keluar")

    pilihan = input("Pilih menu (1-7): ")

    if pilihan == "1":
        nama = input("Masukkan nama playlist: ")

        if nama not in playlist:
            playlist[nama] = {}
            print("Playlist berhasil dibuat!")
        else:
            print("Playlist sudah tersedia.")

    elif pilihan == "2":
        nama = input("Masukkan nama playlist: ")

        if nama in playlist:
            judul = input("Masukkan judul lagu: ")
            penyanyi = input("Masukkan nama penyanyi: ")

            playlist[nama][judul] = penyanyi
            print("Lagu berhasil ditambahkan!")
        else:
            print("Playlist tidak ditemukan.")

    elif pilihan == "3":
        if len(playlist) == 0:
            print("Belum ada playlist.")
        else:
            for nama, lagu in playlist.items():
                print("\nPlaylist:", nama)

                if len(lagu) == 0:
                    print("Belum ada lagu.")
                else:
                    for judul, penyanyi in lagu.items():
                        print("-", judul, "oleh", penyanyi)

    elif pilihan == "4":
        cari = input("Masukkan judul lagu: ")
        ditemukan = False

        for nama, lagu in playlist.items():
            if cari in lagu:
                print("Lagu ditemukan!")
                print("Playlist:", nama)
                print("Judul:", cari)
                print("Penyanyi:", lagu[cari])
                ditemukan = True

        if not ditemukan:
            print("Lagu tidak ditemukan.")

    elif pilihan == "5":
        nama = input("Masukkan nama playlist: ")

        if nama in playlist:
            judul = input("Masukkan judul lagu: ")

            if judul in playlist[nama]:
                del playlist[nama][judul]
                print("Lagu berhasil dihapus!")
            else:
                print("Lagu tidak ditemukan.")
        else:
            print("Playlist tidak ditemukan.")

    elif pilihan == "6":
        nama = input("Masukkan nama playlist: ")

        if nama in playlist:
            del playlist[nama]
            print("Playlist berhasil dihapus!")
        else:
            print("Playlist tidak ditemukan.")

    elif pilihan == "7":
        print("Program selesai. Terima kasih!")
        break

    else:
        print("Pilihan tidak tersedia. Silakan coba lagi.")
