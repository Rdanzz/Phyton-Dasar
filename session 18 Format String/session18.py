# Format string

# contoh generic
nama = "zidhan"
asal = "karawang"
# str = "halo" + nama
format_str = f"halo saya {nama} asal dari kota {asal}"
print(format_str)

angka = 2005.5
format_str = f"angka kamu adalah {angka}"
print(format_str)

# bilangan ordo ribuan
angka = 2000000
format_str = f"jutaan {angka:,}"
print(format_str)

# bilangan desimal
angka = 2025.54321
format_str = f"desimal {angka:.3f}"
print(format_str)