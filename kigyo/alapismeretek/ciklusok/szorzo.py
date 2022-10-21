n = int(input("Írj be egy egész számot: "))

for j in range(1, n+1):
    for i in range(n+1):
        print(i * j, end=" ")
    print()