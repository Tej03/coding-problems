n = 5
alp = 65
for i in range(n):
    print(" " * (n-i), end = " ")
    for j in range(i+1):
        print(chr(alp), end = " ")
        alp += 1
    alp = 65
    print()