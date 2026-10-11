"""
Oppgave 4: Valgsetninger (3 poeng)
En kino har disse billettprisene:

Hvem	Pris
Barn under 12 år	80 kr
Honnør (67 år eller eldre)	100 kr
Student (mellom 12 og 30 år, og har studentbevis)	110 kr
Alle andre	150 kr
Lag et program som spør brukeren om alder og om de har studentbevis (ja/nei), og som skriver ut hva billetten koster. Er alderen under 0 eller over 120, skal programmet skrive ut en feilmelding i stedet for en pris.

Svaret på ja/nei skal fungere uansett om brukeren skriver med store eller små bokstaver.
"""

alder = int(input("Hva er din alder?: "))

if 0 <= alder <= 120:
    if alder < 12:
        print("80kr")
    elif 67 <= alder < 120:
        print("100kr")
    elif 12 <= alder <= 30:
        if input("har du studentbevis? (ja/nei): ").lower() == "ja":
            print("110kr")
        else:
            print("150kr")
    else:
        print("150kr")
else:
    print("Tallet er utenfor godkjente aldere: 0 til 120")