# variabel
# a = 10
# nama = "zidhan"

# tipe data
# integer = 1
# string = "Zidhan"
# boolean = False
# float = 1.5
# complex = complex(5,6)

# print("type data integer :", integer, type(integer))
# print("type data integer :", string, type(string))
# print("type data integer :", boolean, type(boolean))
# print("type data integer :", float, type(float))
# print("type data integer :", complex, type(complex))

# casting / merubah tipe ke tipe lain
print("=====Integer====")
data_int = 0
print("type data integer :", data_int, type(data_int))

data_float = float(data_int)
data_string = str(data_int)
data_boolean = bool(data_int)
print("data float :", data_float)
print("data string :", data_string)
print("data boolean :", data_boolean) #bernilai false jika 0

print("=====Float====")
data_float = 0.5
print("type data float :", data_float, type(data_float))

data_int = int(data_float) #dibulatkan kebawah
data_string = str(data_float)
data_boolean = bool(data_float)
print("data int :", data_int)
print("data string :", data_string)
print("data boolean :", data_boolean) #bernilai false jika 0

print("=====Boolean====")
data_boolean = False
print("type data boolean :", data_boolean, type(data_boolean))

data_int = int(data_boolean) 
data_string = str(data_boolean)
data_float = float(data_boolean)
print("data int :", data_int)
print("data string :", data_string)
print("data float :", data_float) 

print("=====String====")
data_string = "10"
print("type data string :", data_string, type(data_string))

data_int = int(data_string) #string harus angka
data_boolean = bool(data_string) #false jika string kosong
data_float = float(data_string) #string harus angka
print("data int :", data_int) 
print("data boolean :", data_boolean)
print("data float :", data_float) 