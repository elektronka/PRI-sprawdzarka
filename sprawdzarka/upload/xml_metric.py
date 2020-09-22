import difflib
import string
import re
def xmlmetricf( plik):
	file1 = open('template.txt',  encoding='utf8')
	file2 = open(plik,            encoding='utf8')

	d = difflib.Differ()

	diff = d.compare(file1.readlines(), file2.readlines())

	delta = ''.join(x[2:] for x in diff if x.startswith('? ')+ x.startswith('  '))

	with open('output_file.txt', 'w') as f:
		f.write(delta)



	mylines = []
	with open ('output_file.txt', 'rt', encoding='utf8') as myfile:
		for myline in myfile:
			mylines.append(myline)
	wynik=True


	if(bool(re.search('xml version="1.0" encoding="UTF-8"', str(mylines)))):
		if(bool(re.search('<!DOCTYPE sprawozdanie PUBLIC "sprawozdanie" "http://mhanckow.vm.wmi.amu.edu.pl:20002/zajecia/file-storage/view/sprawozdanie.dtd">', str(mylines)))):
			if(bool(re.search('( ){25}[+]{3}( ){9}[+]{1}[^\n][n]', str(mylines)))):
				if(bool(re.search('( ){15}[+]+[^\n][n]', str(mylines)))):
					if(bool(re.search('( ){15}[+]+[^\n][n]', str(mylines)))):
						if(bool(re.search('( ){12}[+]{6}[^\n][n]', str(mylines)))):
							if(bool(re.search('( ){12}[+]+[^\n][n]', str(mylines)))):
								if(bool(re.search('( ){15}[+]{1}[^\n][n]', str(mylines)))):
									pass
								else:
									wynik=False
							else:
								wynik=False
						else:
							wynik=False
					else:
						wynik=False
				else:
					wynik=False
			else:
				wynik=False
		else:
			wynik=False
	else:
		wynik=False
	if(wynik):
		return 'Poprawne'
	else:
		return  'Niepoprawne'






