"""
Oppgave 7: Dictionary (3 poeng)
Her er poengsummene fra en quiz:

poeng = {"Ada": 42, "Linus": 17, "Grace": 58, "Alan": 17, "Guido": 33}
a) Bruk en for-løkke til å skrive ut hver deltaker på formen Ada har 42 poeng. (1 poeng)

b) Regn ut og skriv ut hvor mange poeng deltakerne har til sammen, og hvem som vant. (1 poeng)

c) Spør brukeren om et navn. Finnes navnet, skal programmet skrive ut poengsummen. Finnes det ikke, skal programmet skrive ut Fant ingen deltaker med navnet ... i stedet for å krasje. (1 poeng)
"""

poeng: dict[str, int] = {"Ada": 42, "Linus": 17, "Grace": 58, "Alan": 17, "Guido": 33}
# a)
for navn, tall in poeng.items():
    print(f"{navn} har {tall} poeng. ")

# b) 
print(f"Totalsum: {sum(poeng.values())}")
vinner: dict[str,int|str] = {"navn":"","poeng":0}
for navn, tall in poeng.items():
    if tall > vinner["poeng"]: # type: ignore
        vinner["navn"] = navn
        vinner["poeng"] = tall
print(vinner)

# d)

navn = input("Skriv et navn: ")

try:
    person_poeng = poeng[navn]
    print(f"{navn} har {person_poeng} poeng")
except:
    print(f"Fant ingen deltaker med navnet {navn}")