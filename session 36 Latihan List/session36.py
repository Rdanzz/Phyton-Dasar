# Program List Buku

listBuku = []
while True:
    judul = input("Judul buku\t: ")
    author = input("Nama Penulis\t: ")

    buku = [judul, author]
    listBuku.append(buku)

    for index, buku in enumerate(listBuku):
        print(f"{index+1}. {buku[0]} - {buku[1]}")

    islanjut = input("Apakah ingin membuat data lagi? (y/n)\t:")
    if islanjut.lower() != "y":
        print("Prorgam Selesai")
        break