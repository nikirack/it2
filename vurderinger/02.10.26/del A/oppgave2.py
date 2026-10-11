alder = input("Hvor gammel er du? ")

if alder >= 18
    print("Du er myndig.")
elif alder = 17:
    print("Du blir myndig neste år!")
else:
    print(f"Du blir myndig om {18 - alder} år.")

# alder må være en int for at det skal funke
# du kan heller ikke bruke alder = 17: siden det må være == ikke = 
# den glemte også : etter if alder >= 18

# fikset
alder: int = int(input("Hvor gammel er du? "))

if alder >= 18:
    print("Du er myndig.")
elif alder == 17:
    print("Du blir myndig neste år!")
else:
    print(f"Du blir myndig om {18 - alder} år.")