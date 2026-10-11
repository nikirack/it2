# a)
minutter = 135
print(f"{minutter // 60} t og {minutter % 60} min")
# Dette vil printe ut: 2 t og 15 min
# Siden // er heltalsdivisjon og % er modulus (restene av divisjon)

# b)
fag = "Programmering"
print(fag[0:4].upper() + fag[-3:])
# Dette vil printe ut: PROGing
# Siden fag[0:4].upper() gir PROG og fag[-3:] gir ing

# c)
tall = [3, 8, 1, 6]
tall.sort(reverse=True)
print(tall[1], len(tall))
# tall.sort(reverse=True) vil gi [8,6,3,1]
# tall[1] er 6 og len(tall) er  4
# så den vil printe ut: 6 4

# d)
total = 0
for i in range(1, 10, 3):
    total += i
print(total)
# range(1,10,3) vil gi 1,4,7
# så total vil bli 0+1+4+7 som blir 12
# den vil printe ut: 12