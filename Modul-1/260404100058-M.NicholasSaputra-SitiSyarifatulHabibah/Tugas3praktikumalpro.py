jarak_kerumah_keluarga = 100
total_jarak_pulang_pergi = 200
konsumsi_bensin = 40
sisa_bensin = 1.5
harga_bensin = 10000

total_pulang_pergi = jarak_kerumah_keluarga + total_jarak_pulang_pergi
total_bensin = total_jarak_pulang_pergi / konsumsi_bensin


print("total_pulang_pergi=", jarak_kerumah_keluarga *  total_jarak_pulang_pergi)
print("total_bensin=", total_jarak_pulang_pergi / konsumsi_bensin)


total_beli_bensin = total_bensin - sisa_bensin
print("total_beli_bensin=",total_bensin - sisa_bensin)

bayar_bensin = total_beli_bensin * harga_bensin
print("bayar_bensin = ", total_beli_bensin * harga_bensin)

print("total jarak pulan-pergi :",total_pulang_pergi, "km")
print("total kebutuhan bensin :",total_bensin, "liter")
print("total beli bensin :", total_beli_bensin, "liter")
print("total biaya bensin :", "Rp", bayar_bensin)

