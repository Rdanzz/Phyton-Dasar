import os

# input = int(input("Masukan angka: "))

# try:
#     hasil = 10 / input
#     print("Hasil pembagian:", hasil)
# except:
#     print("Error: Angka tidak boleh 0")

# contoh di apk
# while True:
#     try:
#         angka = int(input("Masukkan angka pembagi: "))
#         hasil = 10 / angka
#         print("Hasil pembagian:", hasil)
#     except ZeroDivisionError:
#         print("Error: Angka tidak boleh 0")
#         continue  
#     except ValueError:
#         print("Error: Masukkan harus berupa angka")
#         continue  

#     while True:  
#         isDone = input("Ingin melanjutkan? (y/n): ").lower()
#         if isDone == "y":
#             break 
#         elif isDone == "n":
#             exit()  
#         else:
#             print("Input yang dimasukkan harus 'y' atau 'n'.")

os.chdir("session 66 Try and Exception")

while True:
    try:
        with open("data.txt", "r") as file:
            print(file.read())
        break
    except FileNotFoundError:
        print("File tidak ditemukan dan membuat file baru")
        with open("data.txt", "w") as file:
            file.write("Isi file baru")
        break