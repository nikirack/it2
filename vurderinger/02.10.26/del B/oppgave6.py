"""
Oppgave 6: Lister (4 poeng)
En værstasjon har målt temperaturen klokka 07 i ti dager:

temperaturer = [4.5, -2.0, 1.5, -6.5, 0.0, 3.0, -1.5, 7.0, 5.5, -3.5]
a) Skriv ut hvor mange målinger det er, og hva den første og den siste målingen var. Bruk indeksering. (1 poeng)

b) Regn ut og skriv ut gjennomsnittstemperaturen, avrundet til én desimal. (1 poeng)

c) Bruk en løkke til å telle hvor mange dager temperaturen var under 0 grader, og skriv ut svaret. (1 poeng)

d) Lag en ny liste som bare inneholder temperaturene som var over 0 grader, sortert fra varmest til kaldest. Skriv ut den nye lista. Den opprinnelige lista skal ikke endres. (1 poeng)
"""

temperaturer: list[float] = [4.5, -2.0, 1.5, -6.5, 0.0, 3.0, -1.5, 7.0, 5.5, -3.5]

# a)
print(f"Antall målinger: {len(temperaturer)}")
print(f"Første måling: {temperaturer[0]}")
print(f"Siste måling: {temperaturer[-1]}")

# b)
gjennomsnitt = sum(temperaturer)/len(temperaturer)

print(f"Gjennomsnittstemperatur: {gjennomsnitt:.1f}")

# c)
dager_under_0 = 0
for temp in temperaturer:
    if temp < 0:
        dager_under_0 += 1

print(f"Dager under 0: {dager_under_0}")

# d) Lag en ny liste som bare inneholder temperaturene som var over 0 grader, sortert fra varmest til kaldest. Skriv ut den nye lista. Den opprinnelige lista skal ikke endres. (1 poeng)

temperaturer_ny: list[float] = []

for temp in sorted(temperaturer, reverse=True):
    if temp > 0:
        temperaturer_ny.append(temp)

print(temperaturer_ny)

