def palindrom(kata):
    kata = kata.lower()
    balik = ""

    for huruf in kata:
        balik = huruf + balik

    if kata == balik:
        return True
    else:
        return False

kata = input("Masukkan sebuah kata: ")
if palindrom(kata):
    print("Kata", kata, "merupakan palindrom.")
else:
    print("Kata", kata, "bukan palindrom.")