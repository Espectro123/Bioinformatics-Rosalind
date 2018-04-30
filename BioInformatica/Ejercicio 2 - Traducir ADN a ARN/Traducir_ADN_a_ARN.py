archivo = open("rosalind_rna.txt","r")
DNA = archivo.readline()
contador = 0
ARN = ''
for i in DNA:
    if(i == 'T'):
        ARN = ARN + 'U'
    else:
        ARN = ARN + i
    contador = contador + 1

print(ARN)
with open('salida.txt', 'w') as f:
    f.write(ARN)