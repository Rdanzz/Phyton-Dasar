# Looping Dictionary

dataDict = {
    "nama": "Zidhan Raffly",
    "umur": 21,
    "pekerjaan": "Programmer"
}

# looping first try untuk mengambil key nya
for key in dataDict:
    print(key)

# looping mengambil iterrables
for key in dataDict.keys():
    print(dataDict.get(key))

# looping second try untuk mengambil value nya
for value in dataDict.values():
    print(value)

items = dataDict.items()
print(items)

for item in dataDict.items():
    print(item)

for key, value in dataDict.items():
    print(f"Key: {key}, Value: {value}")