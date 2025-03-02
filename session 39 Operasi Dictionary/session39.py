# Operator Dictionary

dataDict = {
    "nama": "Zidhan Raffly",
    "umur": 21,
    "pekerjaan": "Programmer"
}

# Panjang Dictionary
panjangDict = len(dataDict)
print(f"Panjang dictionary: {panjangDict}")

# Mengecek key exist                    
keyExist = "nama" in dataDict
print(f"Key 'nama' ada di dictionary: {keyExist}")

# Mengakses value (read) dengan get
# print(dataDict["nama"])
value = dataDict.get("nama")
print(f"Value 'nama': {value}")
value = dataDict.get("lahir")
print(f"Value 'lahir': {value}", "key tidak ditemukan") #Mengecek key dan memberi komentar


# Mengupdate data
dataDict["nama"] = "ucup bensin"
print(dataDict)

# Menambah nilai dengan cara salah
# dataDict["lahir"] = "Bogor"
# print(dataDict)

# Menambah nilai dengan cara benar
dataDict.update({"lahir" : "Bogor"})
print(dataDict)

# Menghapus data
del dataDict["lahir"]
print(dataDict)

