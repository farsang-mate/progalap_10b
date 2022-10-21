pont = int(input("írd be a pontszámot: "))

if pont <= 42:
    print("elégtelen")
elif pont >= 43 and pont <= 57:
    print("elégséges")
elif pont >= 58 and pont <= 72:
    print("közepes")
elif pont >= 73 and pont <= 87:
    print("jó")
elif pont >= 88 and pont <= 100:
    print("jeles")
else:
    print("buta vagy")