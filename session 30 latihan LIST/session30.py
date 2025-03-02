# Manipulasi List

# index   0        1        2
data = ["ucup", "otong", "komek"]
print(data)

# 1. Mengambil data di index ke 1
print(data[1])

# 2. Mengambil infor panjang data
print(len(data))

# 3. Mengubah data di index ke 2
data[2] = "jontong"
print(data)

# 4. Menambah data baru
data.append("dudung")
print(data)

# 5. Menghapus data di index ke 1
data.remove("otong")
print(data)

# 6. Menambahkan data sesuai posisi pada list
data.insert(2, "gemoy")
print(data)

# 7. Mengurutkan data menggunakan sort()
# data.sort()
data.sort(reverse=True)
print(data)

# 8. Menambah list baru

data2 = ["babi", "sapi"]
data.extend(data2)
print(data)

# 9. menghapus data ke terakhir
data.pop()
print(data)

# 10. Mencari data di dalam list
print("babi" in data)
print("jantung" in data)

# 11. Menghapus semua data
data.clear()
print(data)