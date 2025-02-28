# continue, pass and break

# Pass -> berfungsi sebagai dummy, tidak akan di eksekusi

# angka = 0 

# while angka < 10:
#     angka += 1
#     if angka == 5:
#         print("angka 5")
#     if angka == 5:
#         pass
#     print(angka)

# Continous
angka = 0

while angka < 5:
    angka += 1
    print("angka sekarang adalah ", angka)

    if angka == 3:
        print("mantap")
        continue #loncat ke loop selanjutnya
    # print("angka sekarang adalah ", angka)
    print("Selamat datang") #ini di skip jika ada continue

