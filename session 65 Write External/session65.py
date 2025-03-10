import os

os.chdir("session 65 Write External")

# mode write -> membuat file baru jika tidal ada file
# dan menimpa isinya
with open("data.txt", "w") as file:
    print("\nMembuka file dengan with")
    file.write("Coba")

# mode append -> menambahkan ke isi file
with open("data2.txt", "a") as file:
    print("\nMenambahkan ke isi file")
    file.write(" Lagi")

# mode r+ -> bisa membaca dan menulis
# akan menimpa isi teks dengan panjang data
with open("data3.txt", "r+") as file:
    print("\nMengedit isi file")
    data = file.read()
    file.write("Baru dengan R+")
    print(data)