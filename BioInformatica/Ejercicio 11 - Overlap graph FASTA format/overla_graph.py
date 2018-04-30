
#Obtengo el numero de caracteres del archivo
archivo = open("rosalind_grph.txt","r")

datos = archivo.read()

nombre = archivo.readline()
tam_etiqueta = len(nombre) - 2
tam_archivo = len(datos) + len(nombre)
datos = ''
nombre = ''

archivo.close()

#Creo un dicionario con los campos: Etiqueta , [Prefijo,Sufijo]
#El elemento dato es una lista. Se accede a sus datos de la siguiente manera: diccionaro["primero"][0 o 1]

#Abro de nuevo el archivo para leerlo linea a linea

archivo = open("rosalind_grph.txt","r")

ADN = ''
prefijo = ''
sufijo = ''
caracter = ''
etiqueta = ''
diccionario = {}
tam_sufijo = 3 #Define la longuitud del sufijo
tam_prefijo = 3 #Define la longuitud del prefijo


# Elimino el caracter > de la primera etiqueta
caracter = archivo.read(1)
tam_archivo = tam_archivo - 1
caracter = ''

#Voy leyendo el archivo caracter a carater.
#El ciclo termina cuando tam_archivo llege a 0 (o si es navidad)
while(tam_archivo > 0):

    etiqueta = archivo.readline() #Leo la etiqueta de la cadena
    #Leo la cadena de ADN
    while(caracter != '>' and tam_archivo >= 0):
        caracter = archivo.read(1)
        tam_archivo = tam_archivo - 1
        if(caracter != '\n' and caracter != '>'):
            ADN = ADN + caracter

    prefijo = ADN[0:tam_prefijo]
    sufijo = ADN[len(ADN)-tam_prefijo:len(ADN)] #Le resto dos porque el ultimo caracter es el salto de linea
    diccionario[etiqueta[0:len(etiqueta)-1]] = [prefijo,sufijo] #Añado la nueva entrada al diccionario. Elimino \n de las etiquetas

    tam_archivo = tam_archivo - (len(etiqueta))

    caracter = ''
    ADN = ''

#Una vez creado el diccionario comienzo a crear el grafo comparando sufijos y prefijos

cadenas_por_comparar = len(diccionario) #Numero de elementos del diccionario

grafo = {}
lista_de_claves = []

#Obtengo una lista con las claves para iterarla
for i in diccionario:
    lista_de_claves.append(i)

for i in range(len(diccionario)):
    for j in range(cadenas_por_comparar):
        if(i != j):
            if diccionario[lista_de_claves[i]][1] == diccionario[lista_de_claves[j]][0]:
                print(lista_de_claves[i],lista_de_claves[j])

