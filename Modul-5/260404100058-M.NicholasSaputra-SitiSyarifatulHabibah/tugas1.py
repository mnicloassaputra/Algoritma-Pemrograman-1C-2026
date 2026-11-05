def fibonacci(hari):
    if hari == 1 or hari == 2:
        return 1
    else:
        return fibonacci(hari - 1) + fibonacci(hari - 2)
    
while True:
    hari = int(input("Masukkan hari ke-: "))
    if hari > 0:
        break
    print("Hari harus berupa bilangan bulat positif, ulangi.")
print("Jumlah pelanggan pada hari ke-", hari, "adalah:", fibonacci(hari), "orang")

for i in range(1, hari + 1):
    print(fibonacci(i), end=" ")