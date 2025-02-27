print(30 * "=")
print("Kalkulator Sederhana")
print(30 * "=")

# Input angka pertama
angka1 = float(input("\nMasukkan angka pertama: "))

# Input operator dengan pengecekan ulang
operator = input("\nMasukkan operator (+, -, *, /): ")

while operator not in ["+", "-", "*", "/"]:
    print("\nError: Operator salah!")
    operator = input("\nMasukkan operator yang valid (+, -, *, /): ")

# Input angka kedua
angka2 = float(input("\nMasukkan angka kedua: "))

# Penanganan operator
if operator == "+":
    hasil = angka1 + angka2
    print("\nHasil Perhitungan adalah: ", hasil)
elif operator == "-":
    hasil = angka1 - angka2
    print("\nHasil Perhitungan adalah: ", hasil)
elif operator == "*":
    hasil = angka1 * angka2
    print("\nHasil Perhitungan adalah: ", hasil)
elif operator == "/":
    if angka2 == 0:
        print("\nError: Pembagian dengan 0!")
    else:
        hasil = angka1 / angka2
        print("\nHasil Perhitungan adalah: ", hasil)
