"""
Oppgave 5: Løkker og feilhåndtering (3 poeng)
Lag et program som spør brukeren hvor mange billetter de vil kjøpe. Man kan kjøpe mellom 1 og 10 billetter.

Skriver brukeren noe som ikke er et heltall (for eksempel "to"), skal programmet gi en feilmelding og spørre på nytt, uten å krasje.
Skriver brukeren et tall utenfor 1–10, skal programmet også gi en (annen) feilmelding og spørre på nytt.
Når brukeren har skrevet et gyldig antall, skal programmet skrive ut totalprisen, med 150 kr per billett.
Eksempel på kjøring:

Antall billetter: to
Du må skrive inn et heltall.
Antall billetter: 14
Du kan kjøpe mellom 1 og 10 billetter.
Antall billetter: 3
Totalpris: 450 kr
"""

pris_per = 150

while True:
    try:
        antall = int(input("Antall biletter: "))
    except ValueError:
        print("Du må skrive inn et heltall.")
        continue
    if 1 <= antall <= 10:
        print(f"Totalpris: {pris_per*antall}kr")
        break
    else:
        print("Du kan kjøpe mellom 1 og 10 billetter.")