# Latihan konversi satuan temperatur

# program konversi celcius ke satuan lain

print("\nPROGRAM KONVERSI")

celcius = float(input('Masukan suhu dalam celcius: '))
print("\nsuhu dalam celcius adalah : ", celcius, "celcius")

# reamur
reamur = (4/5) * celcius
print("\nsuhu dalam reamur adalah : ", reamur, "reamur")

# fahrenheit
fahrenheit = ((9/5) * 32) + celcius
print("\nsuhu dalam fahrenheit adalah : ", fahrenheit, "fahrenheit")

# kelvin
kelvin = celcius + 273
print("\nsuhu dalam kelvin adalah : ", kelvin, "kelvin")