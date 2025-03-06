
# **kwargs

# fungsi biasa
def fungsi (nama,tinggi,berat):
    print(f"Nama : {nama}")
    print(f"Tinggi : {tinggi}")
    print(f"Berat : {berat}")
fungsi("ucup", 170,45)

def fungsi(**kwargs):
    nama = kwargs["nama"]
    tinggi = kwargs["tinggi"]
    berat = kwargs["berat"]
    print(f"Nama : {nama}, Tinggi {tinggi}, Berat {berat}")
fungsi(nama="ucup", tinggi=170, berat=45)

# studi kasus
def math (*args, **kwargs):
    total = 0
    if kwargs["option"] == "tambah":
        for angka in args:
            total += angka
        print(f"Total : {total}")
    elif kwargs["option"] == "kali":
        hasil = 1
        for angka in args:
            hasil *= angka
        print(f"Hasil : {hasil}")
    else:
        print("Pilihan option salah")

hasil = math(1,2,3,4, option="tambah")
hasil = math(1,2,3,4, option="kali")