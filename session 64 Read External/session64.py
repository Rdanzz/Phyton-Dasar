# Cara membaca file eksternal

import os

os.chdir("session 64 Read External")

# 1. Membuka file
file = open("data.txt", mode="r")

print(f"Status read: {file.readable()}")
print(f"Status write: {file.writable()}")

# 2. Membaca isi file
print(file.read())

# 3. Membaca per baris
# print(file.readlines()) -> baris pertama 
# print(file.readlines()) -> baris selanjutnya

# 4. Membaca semua sebagai list
# print(file.readlines())

print(f"apakah file sudah di close? {file.closed}")

# 5. Menutup file
file.close()
print(f"apakah file sudah di close? {file.closed}")


# membuka file di python dan otomatis tertutup
with open("data.txt", mode="r") as file:
    print("\nMembuka file dengan with")
    print(file.read())

print(f"apakah file sudah di close? {file.closed}")