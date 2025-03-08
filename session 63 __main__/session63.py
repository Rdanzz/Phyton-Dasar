#  __main__ -> top level env

# __name__ -> __main__

# __name__ pada file program utama
print(f"nilai __name pada session63.py : {__name__}")

import fungsi

# contoh penggunaan __main__

# deklarasi
def fungsiTambah(a: int, b: int)->int:
    return a + b

# fungsi utama
if __name__ == '__main__':
    print(fungsiTambah(10, 5))


# import package
import package