year: int = int(input("Skriv ett år: "))

# Krav
# delelig med 4
# Ikke delelig med 100 (men hvis med 400 er det skuddår)

if ((year % 4 == 0) and not (year % 100 == 0 )) or (year % 400 == 0):
    print("Året er skuddår")
else:
    print("Året er ikke skuddår")