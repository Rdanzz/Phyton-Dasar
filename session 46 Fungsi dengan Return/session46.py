# Fungsi dengan Return

# struktur
# def namaFungsi (arguments):
#     badan fungsi
#     return output

def cetakSalam(nama):
    return f"Selamat pagi, {nama}!"

# pemanggilan fungsi
namaUser = input("Masukan nama anda: ")
print(cetakSalam(namaUser))

# Fungsi dengan Return dan Parameter
def hitungLuasSegitiga(alas, tinggi):
    luas = 0.5 * alas * tinggi
    return luas

alasSegitiga = float(input("Masukan alas segitiga: "))
tinggiSegitiga = float(input("Masukan tinggi segitiga: "))

print(f"Luas segitiga dengan alas {alasSegitiga} dan tinggi {tinggiSegitiga} adalah: {hitungLuasSegitiga(alasSegitiga, tinggiSegitiga)}")

