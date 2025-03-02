# Looping dari List

# for loop
data = [3,2,1,7,6,5,4]

print(f"\nFOR LOOP")
for angka in data:
    print(f"angka : {angka}")

# for loop dan range
data = [1,2,3,4]

print(f"\nFOR LOOP RANGE")
for i in range(len(data)):
    print(f"angka : {data[i]}")

# while loop
print(f"\nWHILE LOOP")
i = 0
while i < len(data) :
    print(f"angka : {data[i]}")
    i += 1

# list comprehension
print(f"\nLIST COMPREHENSION")
data = ["dudung", 2, 3, 4, "otong"]
[print(f"data = {i}") for i in data]

# Enumerate

print(f"\nENUMERATE")
data = ["dudung", 2, 3, 4, "otong"]
for index, value in enumerate(data):
    print(f"index = {index}, value = {value}")