lista = [5,6,4,4,8,9,4,2,7,3,5,6,6,9,4,2,3,4,4,4,4,4]
elementy = []
for x in lista:
    if (x not in elementy):
        elementy.append(x)
slownik = {}

for x in elementy:
    slownik[x] = 0

#print(slownik)

for x in lista:
    slownik[x] += 1

zmienna = 0

for x in slownik:
    if slownik[x] > zmienna:
        zmienna = slownik[x]

moda = 0

for x in slownik:
    if slownik[x] == zmienna:
        moda = x

print(moda)
