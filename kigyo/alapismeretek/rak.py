# ev = int(input("2000 utáni év: "))

# if ev >= 2000:
#     if ev % 4 == 0:
#         print("szökőév")
#     else: print("Nem szökőév")


ev = int(input("2000 utáni év: "))

if ev >= 2000 and ev % 4 == 0:
    print("szökőév")
elif ev >= 2000:
    print("Nem szökőév")
else:
    print("2000 től nagyobbat adj meg máskor te retard!")
    exit()