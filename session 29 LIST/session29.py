# List

# kumpulan data angka
dataAngka = [1, 2, 3]
print(dataAngka)

# kumpulan data string
dataString = ["satu", "dua", "tiga"]
print(dataString)

# kumpulan data boolean
dataBoolean = [True, False, True]
print(dataBoolean)

# Kumpulan data campuran
dataCampuran = [1, "dua", True, 3.5]
print(dataCampuran)

# Cara alternatif membat list
dataRange = range(1, 10, 2) #range(start), stop, step
print(dataRange)
dataList = list(dataRange)
print(dataList)

# Membuat List dengan for loop
dataList = [
    i for i in range (0, 10)
]
print(dataList)

# Membuat list dengan for dan if
dataList = [ 
    i 2 for i in range(0, 10)
    # i ** 2 for i in range(0, 10)
    # if i % 2 == 0
    if i % 2 != 0
    # if i != 5
    ]
print(dataList)
