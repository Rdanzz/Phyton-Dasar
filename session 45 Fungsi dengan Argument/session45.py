""" Fungsi dengan Argumen (input) """

def cetakTeks(teks): #(teks) -> sebagai parameter atau menerima inputan
    print(teks)

cetakTeks("Hello world") # (teks) -> sebagai parameter atau menerima

# Fungsi dengan Argumen yang diberikan nilai default
def cetakTeksDenganDefault(teks="Halo dunia"):
    print(teks)

cetakTeksDenganDefault() # teks default adalah "Halo dunia"

def sayHi(listPeserta):
    dataPeserta = listPeserta.copy()
    for peserta in dataPeserta:
        print(f"Halo, {peserta}")

peserta = ["Alice", "Bob", "Charlie"]
sayHi(peserta) # listPeserta -> sebagai parameter yang diberikan