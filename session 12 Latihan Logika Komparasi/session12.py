#  Latihan komparasi dan logika

# mengecek nilai 
# +++++3----5+++++
inputUser = float(input("masukan angka: "))

# Cek apakah inputUser < 3
kurangDari = inputUser < 3

# Cetak hasil perbandingan
print(f"{inputUser} kurang dari 3: {kurangDari}")

# Cek apakah inputUser > 5
lebihDari = inputUser > 5

# Cetak hasil perbandingan
print(f"{inputUser} lebih dari 5: {lebihDari}")


# Cek dengan OR

# +++++3----5+++++
isOr = kurangDari or lebihDari

# Cetak hasil perbandingan
print(f"{inputUser} kurang dari 3 atau lebih dari 5: {isOr}")

# Cek dengan AND

# ----3+++++7----
kurangDari = inputUser < 7
lebihDari = inputUser > 3
isAnd = kurangDari and lebihDari

# Cetak hasil perbandingan

print(f"{inputUser} lebih dari 3 dan kurang dari 7: {isAnd}")
