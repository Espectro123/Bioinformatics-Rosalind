archivo = open("rosalind_revc.txt","r")
DNA = archivo.readline()
DNA_Complemtario_reverso = ''
for i in reversed(DNA):
    if(i == 'A'):
        DNA_Complemtario_reverso = DNA_Complemtario_reverso + 'T'
    elif(i == 'G'):
        DNA_Complemtario_reverso = DNA_Complemtario_reverso + 'C'
    elif(i == 'C'):
        DNA_Complemtario_reverso = DNA_Complemtario_reverso + 'G'
    elif( i == 'T'):
        DNA_Complemtario_reverso = DNA_Complemtario_reverso + 'A'

with open('salida.txt', 'w') as f:
    f.write(DNA_Complemtario_reverso)