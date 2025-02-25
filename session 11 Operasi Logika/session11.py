# Operasi Logikan atau Boolean

# and, or, not, xor

#  not, 
print("===== NOT =====")
a = True
b = not a
print("nilai a adalah :", a)
print("nilai b adalah:", b)

# or
print("\n===== OR =====")
a = False
b = False 
c = a or b
print(f"{a} or {b} = {c}")

a = True
b = False 
c = a or b
print(f"{a} or {b} = {c}")

a = False
b = True 
c = a or b
print(f"{a} or {b} = {c}")

a = True
b = True 
c = a or b
print(f"{a} or {b} = {c}")


# and
print("\n===== AND =====")
a = False
b = False 
c = a and b
print(f"{a} and {b} = {c}")

a = True
b = False 
c = a and b
print(f"{a} and {b} = {c}")

a = False
b = True 
c = a and b
print(f"{a} and {b} = {c}")

a = True
b = True 
c = a and b
print(f"{a} and {b} = {c}")

print("\n===== XOR =====")
a = False
b = False 
c = a ^ b
print(f"{a} xor {b} = {c}")

a = True
b = False 
c = a ^ b
print(f"{a} xor {b} = {c}")

a = False
b = True 
c = a ^ b
print(f"{a} xor {b} = {c}")

a = True
b = True 
c = a ^ b
print(f"{a} xor {b} = {c}")