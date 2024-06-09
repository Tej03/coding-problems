n = 5
for i in range(n+1):
    for j in range(n-i):
        print(" ", end= " ")
    for k in range(1, 2*i):
        print("#", end = " ")
    print()
    