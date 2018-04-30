def ObtenerCodficacion(triplete):
    letra_codificada = ' '
    if(triplete == "UUU" or triplete == "UUC"):
        letra_codificada = 'F'
    elif(triplete == "UUA" or triplete == "UUG" or triplete == "CUU" or triplete == "CUC" or triplete == "CUA" or triplete == "CUG"):
        letra_codificada = 'L'
    elif(triplete == "UCU" or triplete == "UCC" or triplete == "UCA" or triplete == "UCG"):
        letra_codificada = 'S'
    elif(triplete == "UAU" or triplete == "UAC"):
        letra_codificada = 'Y'
    elif(triplete == "UAA" or triplete == "UAG" or triplete == "UGA"):
        letra_codificada = 'STOP'
    elif(triplete == "UGU" or triplete == "UGC"):
        letra_codificada = 'C'
    elif(triplete == "UGG"):
        letra_codificada = 'W'
    elif(triplete == "CCU" or triplete == "CCC" or triplete == "CCA" or triplete == "CCG"):
        letra_codificada = 'P'
    elif(triplete == "CAU" or triplete == "CAC"):
        letra_codificada = 'H'
    elif(triplete == "CAA" or triplete == "CAG"):
        letra_codificada = 'Q'
    elif(triplete == "CGU" or triplete == "CGC" or triplete == "CGA" or triplete == "CGG" or triplete == "AGA" or triplete == "AGG"):
        letra_codificada = 'R'
    elif(triplete == "AUU" or triplete == "AUC" or triplete == "AUA"):
        letra_codificada = 'I'
    elif(triplete == "AUG"):
        letra_codificada = 'M'
    elif(triplete == "ACU" or triplete == "ACC" or triplete == "ACG" or triplete == "ACA"):
        letra_codificada = 'T'
    elif(triplete == "AAU" or triplete == "AAC"):
        letra_codificada = 'N'
    elif(triplete == "AAA" or triplete == "AAG"):
        letra_codificada = 'K'
    elif(triplete == "AGU" or triplete == "AGC"):
        letra_codificada = 'S'
    elif(triplete == "GUU" or triplete == "GUC" or triplete == "GUA" or triplete == "GUG"):
        letra_codificada = 'V'
    elif(triplete == "GCU" or triplete == "GCC" or triplete == "GCA" or triplete == "GCG"):
        letra_codificada = 'A'
    elif(triplete == "GAU" or triplete == "GAC"):
        letra_codificada = 'D'
    elif(triplete == "GAA" or triplete == "GAG"):
        letra_codificada = 'E'
    elif(triplete == "GGU" or triplete == "GGC" or triplete == "GGG" or triplete == "GGA"):
        letra_codificada = 'G'

    return letra_codificada

archivo = open("rosalind_prot.txt","r")
ARN = archivo.readline()
proteina = ''
triplete = ''
contador = 0
letra = ''

for i in ARN:
    if(len(triplete) < 3):
        triplete = triplete + i

    if(len(triplete) == 3):
        letra = ObtenerCodficacion(triplete)
        proteina = proteina + letra
        triplete = ''


with open('salida.txt', 'w') as f:
    f.write(proteina)

