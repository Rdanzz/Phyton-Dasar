# Latihan Date and Time

import datetime as dt

# # Mengambil tanggal hari ini

today = dt.date.today()

# # Mencetak tanggal hari ini

# print("Tanggal hari ini: ", today)

# tanggal_lahir = dt.date(2003,4,10)
# print(f"hari lahir gua adalah:  {tanggal_lahir}")

print("masukan tanggal, bulan, tahun anda")
tanggal = int(input(f"masukan tanggal anda \t:"))
bulan = int(input(f"masukan bulan anda \t:"))
tahun = int(input(f"masukan tahun anda \t:"))

lahir = dt.date(tahun, bulan, tanggal)
print(f"Tanggal Lahir anda adalah : {lahir}")
print(f"Hari nya adalah : {lahir:%A}")

umurHari = today - lahir
umurTahun = umurHari.days // 365

print(f"Umur anda sekarang adalah : {umurTahun} tahun")

