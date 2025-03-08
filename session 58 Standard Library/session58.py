import datetime

date = datetime.datetime.now()

print("Tanggal:", date.day)
print("Bulan:", date.month)
print("Tahun:", date.year)

print("Jam:", date.hour)

print("Menit:", date.minute)

print("Detik:", date.second)

print("Hari dalam minggu:", date.weekday())

print("Tanggal dalam bulan:", date.strftime("%d %B %Y"))

print(f"Hari: {date.strftime('%A')}")


from collections import Counter

data = ["a", "b", "c", "d", "e", "f"]
counter = Counter(data)

print(counter)
print(f"data huruf a: {counter['a']}")

import io
import os

# print(os.listdir())  # Melihat daftar file di direktori

os.chdir("session 58 Standard Library")
print("Sekarang berada di:", os.getcwd())

file = io.open("file_text.txt", "r")
print(file.read())