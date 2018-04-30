archivo = open("C:\\Users\\kical\\Desktop\\BioInformatica\\rosalind_dna.txt","r")
ADN = archivo.readline()
Contador_A = 0
Contador_G = 0
Contador_C = 0
Contador_T = 0
print(ADN)
print(len(ADN))
for i in ADN:
	if i == 'A':
		Contador_A = Contador_A + 1
	elif i == 'G':
		Contador_G = Contador_G + 1
	elif i == 'C':
		Contador_C = Contador_C + 1
	elif i == 'T':
		Contador_T = Contador_T + 1
solucion =repr(Contador_A) + ' ' + repr(Contador_C) + ' ' + repr(Contador_G) + ' ' + repr(Contador_T)
print(solucion)
