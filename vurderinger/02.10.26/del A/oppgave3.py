def dobbel_partall(liste: list[int]):
    resultat: list[int] = []
    for tall in liste:
        if tall % 2 == 0:
            resultat.append(tall * 2)
        else:
            resultat.append(tall)
    return resultat

tallene = [1, 2, 3, 4]
nye = dobbel_partall(tallene)
print(nye)
print(tallene)
print(sum(nye) > 10)

# a)
# programmet går gjennom alle tall i en liste og dobbler partallene
# programmet vil skrive ut:
# [1,4,3,8]
# [1,2,3,4]
# True

# b)
# alt denne koden gjør er å skjekke om et tall er et partal ved å se på restene av tallet som er igjen etter å dele på a
# hvis resten er 0, betyr det at tallet er et partal og da ganger koden tallet med 2
# dette gjør koden med alle tallene i listen