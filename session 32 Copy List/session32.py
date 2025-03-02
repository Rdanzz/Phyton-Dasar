# Teknik Menduplikat List

a = ["ucup", "otong", "dudung"]
print(f"isi data dari a : {a}")

b = a
# ini bukan copy atau duplikat list
print(f"isi data dari b : {b}")

# merubah data dari a
a[0] = "zidhan"
b.sort()
# cek perubahan data

print(f"\nisi data yang sama antara a dan b setelah diubah :")
print(f"a : {a}")
print(f"b : {b}")

# menduplikat list

print("\nMenduplikat list")
c = a.copy()
print("\nMenduplikat list", c)

