#print("Hello World")

a = 10  # przypisanie do zmiennej a liczby 10 typ int
b = 15
c = a + b 

#print(c)

boolean = True # typ bool (prawda, fałsz)

#print(boolean)

char = 'w' # typ char, znak
char2 = 'e'
c = char + char2 # typ string, ciąg znaków 'we'

lista = []

lista.append(char)
lista.append(char2)


#print(c[1])

liczba = 0
#while(liczba<10):
#    print(liczba)
#    liczba = liczba + 1


def zad1(a,b):
    a = float(a)
    b = float(b)
    return a/b

#print(zad1(21,4))

a = float(21)
#print(a)
a = int(a)
##print(a)


lista = ['M','I','C','H','A','Ł','C','D','E']

imie = ''

for i in lista:
    imie = imie + i

#print(imie)

def polacz(a,b):
    a = str(a)
    b = str(b)
    #print(a+b)
polacz(20,40)

#print(len(lista))

#print(abs(-14))

x = 2.8323423

#print(round(3.34545,2))

def czy_pierwsza(n):
    n = int(n)
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def liczby_pierwsze(n):
    for i in range(n):
        if czy_pierwsza(i):
            print(i)

liczby_pierwsze(70)

    print(str(n)+ ' ' + "Jest liczbą parzystą")
