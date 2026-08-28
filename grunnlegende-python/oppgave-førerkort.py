"""
Førerkort: Be om alder. Under 16? Nope! 16+, moped. 18+, bil. 21+, buss. Øvre grense? Optimaliser if-else-bruken
"""

alder: int = int(input("Alder: "))

if alder >= 21:
    print("buss")
elif alder >= 18:
    print("bil")
elif alder >= 16:
    print("moped")
else:
    print("nope")
