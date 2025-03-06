#  Global and Local Scope

global_nama = "Zidhan" # global variable

def tampilkan_nama():
    nama = "Raffly" # local variable
    print(f"Nama saya adalah {nama}")
    print(f"Nama global: {global_nama}")

tampilkan_nama()

print(nama) # cannot acces cause variable name is local scope
