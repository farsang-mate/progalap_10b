a = int(input("ird be az a számot: "))
b = int(input("ird be az b számot: "))
c = int(input("ird be az c számot: "))

if a + b > c and a + c > b and b + c > a:
    print ("szerkeszthető")
else: print("Nem szerkeszthető!")