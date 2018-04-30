archivo = open("rosalind_hamm.txt","r")

ADN_1 = archivo.readline()
ADN_2 = archivo.readline()
distancia = 0
print(ADN_1)
print(ADN_2)
for i in range(len(ADN_1)):
    if(ADN_1[i] == ADN_2[i]):
        distancia = distancia
    else:
        distancia = distancia + 1

print(distancia)

