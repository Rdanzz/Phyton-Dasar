# Templte Dictionary Mahasiswa
import datetime
import os

mahasiswaTemplate = {
    "nama": "John Doe",
    "nim": "1234567890",
    "lulus": 0,
    "tanggal_lahir": datetime.date(1111,1,1),
}

dataMahasiswa = {}

os.system("clear")
print(f"{'Selamat Datang' :^20}") 
print(f"{'Data Mahasiswa' :^20}") 

mahasiswa = dict.fromkeys(mahasiswaTemplate.keys())
print(mahasiswa)

mahasiswa["nama"] = input("Masukan Nama Mahasiswa: ")
mahasiswa["nim"] = input("Masukan NIM Mahasiswa: ")
mahasiswa["lulus"] = int(input("Masukan Data Kelulusan: "))
tahunLahir = int(input("Tahun Lahir (YYYY): "))
bulanLahir = int(input("Tanggal Lahir (1-12): "))
tanggalLahir = int(input("Tanggal Lahir (1-31): "))
mahasiswa["tanggal_lahir"] = datetime.date(tahunLahir,bulanLahir,tanggalLahir)
print(mahasiswa)
