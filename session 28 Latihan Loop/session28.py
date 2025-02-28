# Latihan Loop 

# n = 5
# for i in range(1, n + 1):
#     print("*" * i)

for i in range (1, 6):
    print("*" * i)

n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)


n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
