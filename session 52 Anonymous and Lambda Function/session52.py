# Lambda Function

# biasa
def kuadrat (angka):
    return angka ** 2
print(kuadrat(3))

# lambda
kuadrat_lambda = lambda angka: angka ** 2
print(kuadrat_lambda(3))

# custom
kuadrat = lambda num, pow : num ** pow
print(kuadrat(4, 2))

# sorting data dengan lambda
data = [("Andi", 25), ("Budi", 30), ("Caca", 28)]
data.sort(key=lambda x: x[1])
print(data)

# filter data dengan lambda
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_data = list(filter(lambda x: x % 2 == 0, data))
print(filtered_data)

# map data dengan lambda
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mapped_data = list(map(lambda x: x ** 2, data))
print(mapped_data)

# Anonymous Function
# currying <- haskell curry

def pangkat(angka, n):
    hasil = angka ** n
    print(hasil)

pangkat(2,3)

# currying
def pangkat(n):
    return lambda angka: angka ** n

pangkat_dua = pangkat(2)

print(pangkat_dua(10))