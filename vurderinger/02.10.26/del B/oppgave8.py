"""
Oppgave 8: Funksjoner (4 poeng)
a) Lag en funksjon konverter_tid(sekunder) som tar inn et antall sekunder og returnerer hvor mange timer, minutter og sekunder det tilsvarer (tre returverdier). Kall funksjonen med 4000, og skriv ut resultatet på formen 1 t, 6 min, 40 s. (2 poeng)

b) Lag en funksjon er_sterkt_passord(passord) som returnerer True hvis passordet oppfyller alle kravene under, og False ellers: (2 poeng)

minst 8 tegn langt
inneholder minst ett siffer
inneholder minst én stor bokstav
Test funksjonen med disse tre passordene som viser at den fungerer: "hemmelig", "Hemmelig" og "Hemmelig1".

Tips: tegn.isdigit() gir True hvis tegn er et siffer, og tegn.isupper() gir True hvis tegn er en stor bokstav.

Bruk gjerne type hints på funksjonene dine.
"""

# a)
def konverter_tid(sekunder:int) -> tuple[int, int, int]:
    s: int = sekunder % 60
    m: int = (sekunder // 60) % 60
    t: int = (sekunder // 60) // 60
    return t,m,s

tid: tuple[int, int, int] = konverter_tid(4000)
print(f"{tid[0]} t, {tid[1]} min, {tid[2]} s")

# b)
def er_sterkt_passord(passord: str) -> bool:
    if not len(passord) > 8:
        return False
    digit = False
    upper = False
    for letter in passord:
        if letter.isupper():
            upper = True
        if letter.isdigit():
            digit = True

    if digit and upper:
        return True
    else: 
        return False

print(er_sterkt_passord("hemmelig"))
print(er_sterkt_passord("Hemmelig"))
print(er_sterkt_passord("Hemmel1g"))
print(er_sterkt_passord("Hemmelig1"))

    