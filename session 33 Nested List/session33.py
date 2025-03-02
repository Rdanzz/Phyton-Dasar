# Nested List

data1 = [1,2,3]
data2 = [4,1,3]

listBiasa = [1,2,3,4,5]

print(f"nestedList: {data1, data2}")
print(f"listBiasa: {listBiasa}")

nestedList = [
    [
        1,2,3
    ],
    [
        4,1,3
    ],
]

print(f"nestedList: {nestedList}")

# Contoh dengan Loop
pesertaSatu = ["otong", 20, "Laki-Laki"]
pesertaDua = ["meeley", 22, "Perempuan"]
pesertaTiga = ["dudung", 21, "Laki-Laki"]

listPeserta = [pesertaSatu, pesertaDua, pesertaTiga]

for peserta in listPeserta:
    print(f"\nNama\t\t: {peserta[0]}")
    print(f"Umur\t\t: {peserta[1]}")
    print(f"Jenis Kelamin\t: {peserta[2]}\n")

