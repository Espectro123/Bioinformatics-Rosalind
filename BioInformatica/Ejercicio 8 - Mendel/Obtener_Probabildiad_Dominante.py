archivo = open("rosalind_iprb.txt","r")

datos = archivo.read()

k = '' #Homocigotico domiante AA
m = '' #heterocigotico Aa
n = '' #Homocigotico recesivo aa

poblacion_total = 0
contador = 0

#Leo los datos
for i in range(len(datos)):
    if datos[i] != ' ' and contador == 0:
        k = k + datos[i]
    elif datos[i] != ' ' and contador == 1:
        m = m + datos[i]
    elif datos[i] != ' ' and contador == 2:
        n = n + datos[i]
    else:
        contador = contador + 1

poblacion_total = int(k) + int(m) + int(n)

#Comienzo a calcular la probabilidad
#La probabilidad de que un descendiente no sea homocigotico es 1 - (Probabilidad_heterocigotico + recesivo)/50

probabilidad = 0.0
probabilidad = ((int(m)+int(n))/poblacion_total) * 0.32

print(1 - probabilidad)