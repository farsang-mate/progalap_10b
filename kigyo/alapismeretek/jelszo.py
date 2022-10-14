eloremegadott = "admin"
eloremegadott1 = "admin1"
eloremegadott2 = "admin2"
eloremegadott3 = "admin3"
jelszo = input("Add meg a jelszót!: ")
megadott = input("Jelentkezz be!")
if megadott == jelszo:
    print ("sikeres bejelentkezés!")
elif megadott == eloremegadott:
    print("szia admin")
else:
    print ("A jogosulatlan felhasználókat elpusztítjuk!")
