n = 5
alp = 65
for i in range(n+1):
    for j in range(n-i):
        print(" ", end= " ")
    for k in range(1, 2*i):
        print(chr(alp), end = " ")
        alp += 1
    alp = 65
    print()
    