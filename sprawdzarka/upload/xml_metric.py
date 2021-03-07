import re

def xmlmetricf(file):
    sline = ""
    for line in file:
        sline += str(line.decode("utf-8"))
    mo = re.compile(r'<\?xml version="1\.0" encoding="UTF-8"\?>(\r\n)*<!DOCTYPE\ssprawozdanie\sPUBLIC\s"sprawozdanie"\s"http:\/\/mhanckow\.vm\.wmi\.amu\.edu\.pl:20002/zajecia/file-storage/view/sprawozdanie\.dtd">(\r\n)*<sprawozdanie\sprzedmiot="[AaĄąBbCcĆćDdEeĘęFfGgHhIiJjKkLlŁłMmNnŃńOoÓóPpRrSsŚśTtUuWwYyZzŹźŻż]{3}" temat="[AaĄąBbCcĆćDdEeĘęFfGgHhIiJjKkLlŁłMmNnŃńOoÓóPpRrSsŚśTtUuWwYyZzŹźŻż]{1}">(\r\n)*<imie_nazwisko>[AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻ][aąbcćdeęfghijklłmnńoóprsśtuwyzźż]+(\s[AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻ][aąbcćdeęfghijklłmnńoóprsśtuwyzźż]+)+</imie_nazwisko>(\r\n)*<nr_indeksu>[0-9]{6}</nr_indeksu>(\r\n)*<liczba_pkt>([0-9]+|([0-9]+\.[0-9]+))</liczba_pkt>(\r\n)*(<zadanie\snr="-?[0-9]+[AaĄąBbCcĆćDdEeĘęFfGgHhIiJjKkLlŁłMmNnŃńOoÓóPpRrSsŚśTtUuWwYyZzŹźŻż]*"\spkt="([0-9]+|([0-9]+\.[0-9]+))+"></zadanie>(\r\n)*)+</sprawozdanie>')
    res = re.findall(mo, sline)
    if res:
        return True
    else:
        return False