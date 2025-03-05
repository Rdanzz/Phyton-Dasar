# Latihan Fungsi

import os

# program menghitung luas dan keliling persegi panjang
os.system("clear")
def hitung_luas_dan_keliling(panjang, lebar):
    # Hitung luas persegi panjang
    luas = panjang * lebar

    # Hitung keliling persegi panjang
    keliling = 2 * (panjang + lebar)
    
    return luas, keliling


print(f"{'PROGRAM MENGHITUNG LUAS DAN KELILING PERSEGI PANJANG':^40}")
# Input panjang dan lebar
panjang = int(input("Masukan panjang persegi panjang: "))
lebar = int(input("Masukan lebar persegi panjang: "))

# Hitung luas dan keliling
luas, keliling = hitung_luas_dan_keliling(panjang, lebar)

# Cetak hasil
print(f"Luas persegi panjang adalah: {luas}")
print(f"Keliling persegi panjang adalah: {keliling}")