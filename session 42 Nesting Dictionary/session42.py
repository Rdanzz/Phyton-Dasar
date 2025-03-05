import datetime

# List untuk menyimpan banyak data mahasiswa
mahasiswa_list = [
    {
        "nama": "Zidhan Raffly",
        "nim": 123456789,
        "kelas": "TI-2A",
        "jurusan": "Teknik Informatika",
        "ipk": 3.85,
        "hobi": ["coding", "membaca", "menyanyi"],
        "beasiswa": False,
        "lahir": datetime.date(2003, 4, 10)
    },
    {
        "nama": "Aisyah Putri",
        "nim": 987654321,
        "kelas": "TI-2B",
        "jurusan": "Teknik Informatika",
        "ipk": 3.90,
        "hobi": ["menulis", "olahraga"],
        "beasiswa": True,
        "lahir": datetime.date(2002, 7, 15)
    }
]

# Menampilkan data mahasiswa dengan looping
for mahasiswa in mahasiswa_list:
    print("="*30)
    print(f"Nama      : {mahasiswa['nama']}")
    print(f"NIM       : {mahasiswa['nim']}")
    print(f"Kelas     : {mahasiswa['kelas']}")
    print(f"Jurusan   : {mahasiswa['jurusan']}")
    print(f"IPK       : {mahasiswa['ipk']}")
    print(f"Hobi      : {', '.join(mahasiswa['hobi'])}")
    print(f"Beasiswa  : {'Ya' if mahasiswa['beasiswa'] else 'Tidak'}")
    print(f"Lahir     : {mahasiswa['lahir'].strftime('%d-%m-%Y')}")
    print("="*30)


