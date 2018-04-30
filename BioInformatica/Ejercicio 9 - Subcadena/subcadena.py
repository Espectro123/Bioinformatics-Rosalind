def comparar_cadenas(cadena,sub_cadena):
    contador = 0
    for i in range(len(cadena)):
        if(cadena[i] == sub_cadena[i]):
            contador = contador + 1

    if(contador == len(cadena)):
        return 1
    else:
        return 0



archivo = open("rosalind_subs.txt","r")

ADN = archivo.readline()
sub_cadena = archivo.readline()
cadena = ''
tam = len(ADN)
flag = 0
resultado = ''

print(resultado)

for i in range(tam):
    if(sub_cadena[0] == ADN[i]):
        if(i+len(sub_cadena) < tam):
            cadena = ADN[i:i+len(sub_cadena)-1]
            flag = comparar_cadenas(cadena,sub_cadena)
            if(flag == 1):
                resultado = resultado + str(i+1) + ' '


print(resultado)