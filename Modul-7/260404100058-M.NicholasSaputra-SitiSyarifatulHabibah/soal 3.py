undangan = set()
webinar_A = set()
webinar_B = set()

jumlah = int(input("Masukkan jumlah undangan: "))

for i in range(jumlah):
    nama = input("Masukkan nama undangan: ")
    undangan.add(nama)

jumlah_A = int(input("\nMasukkan jumlah peserta Webinar A: "))

for i in range(jumlah_A):
    nama = input("Masukkan nama peserta: ")
    webinar_A.add(nama)

jumlah_B = int(input("\nMasukkan jumlah peserta Webinar B: "))

for i in range(jumlah_B):
    nama = input("Masukkan nama peserta: ")
    webinar_B.add(nama)

semua_peserta = webinar_A | webinar_B
print("\nSemua peserta:", semua_peserta)

kedua_webinar = webinar_A & webinar_B
print("Peserta yang hadir di kedua webinar:", kedua_webinar)

satu_webinar = webinar_A ^ webinar_B
print("Peserta yang hanya hadir di salah satu webinar:", satu_webinar)

tidak_hadir = undangan - (webinar_A | webinar_B)
print("Undangan yang tidak hadir:", tidak_hadir)

