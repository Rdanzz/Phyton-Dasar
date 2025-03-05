# *args

def fungsi(nama, tinggi, berat) :
    print(f"Nama : {nama}")
    print(f"Tinggi : {tinggi}")
    print(f"Berat : {berat}")

fungsi("ucup", 170, 55)

# mulai *args
def fungsi_args(*args) :
    nama, tinggi, berat = args

    print(f"Nama : {nama}")
    print(f"Tinggi : {tinggi}")
    print(f"Berat : {berat}")

fungsi_args("ucup", 170, 55)

# studi kasus

def tambah(*data):
    total = 0
    for item in data:
        total += item
    return total

print(tambah(1, 2, 3, 4, 5)) # 15