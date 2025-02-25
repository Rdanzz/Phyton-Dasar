# Operasi dan Manipulasi String

# 1. Menymabung string (concatenate)
nama_awal = "Zidhan"
nama_akhir = "Raffly"
nama_lengkap = nama_awal + " " + nama_akhir

print(nama_lengkap)

# 2. Menghitung panjnag string
panjang_nama = len(nama_lengkap)
print(f"{nama_lengkap} Panjang nama lengkap: {panjang_nama}")

# 3. Operator untuk string
# mengecek apakah ada komponen char atau string di string
d = "D"
status = d in nama_lengkap
statusNot = d not in nama_lengkap

print(f"{d} ada di {nama_lengkap}: {status}")
print(f"{d} tidak ada di {nama_lengkap}: {statusNot}")

# 4. mengulang string
print(f"wk" * 10)

# 5. Indexing
print(f"Index ke 0 adalah hurug : {nama_lengkap[0]}")
print(f"Index ke 1 adalah hurug : {nama_lengkap[1]}")
print(f"Index ke -1 adalah hurug : {nama_lengkap[-1]}")
print(f"Index ke -2 adalah hurug : {nama_lengkap[-2]}")
print(f"Index ke 0 sampai 5 adalah hurug : {nama_lengkap[0:5]}")

# 6. Operator dalam bentuk method
data = "otong surotong jontong"
jumlah = data.count("o")

print(f"Jumlah huruf 'o' dalam {data} adalah: {jumlah}")