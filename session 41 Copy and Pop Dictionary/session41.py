# Copy Dictionary

dataDict = {
    "nama": "Zidhan Raffly",
    "umur": 21,
    "pekerjaan": "Programmer"
}

dataDictCopy = dataDict.copy()
print(dataDict)
print(dataDictCopy)

# ubah data dataDict

dataDict["nama"] = "Zidhan"
print(dataDict)
print(dataDictCopy)  # dataDictCopy tetap sama, karena copy() bukan deep copy. Menyimpan referensi ke objek asli.

# Pop Dictionary -> ambil berdasarkan key
dataDict.pop("umur")
print(f"\nini adalah hasil pop: {dataDict}")

# Pop item dictionary -> ambil data terakhir saja
item = dataDict.popitem()
print(f"\nini adalah hasil popitem: {item}")