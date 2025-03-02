# Deep Nested List

data = [
    [1, 2,3],
    [4, 5, 6],
    [7, 8, 9]
]
print(f"Data List: {data}")

# Mengakses data di index ke 2, 1
print(f"Data di index 2,1: {data[2][1]}")


# jika ingin mengubah member dari list bersarang atau nested list tidak bisa gunakan copy() harus gunakan deepcopy dan import library nya