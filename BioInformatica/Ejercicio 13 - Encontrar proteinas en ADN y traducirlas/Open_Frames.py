def ObtenerCodficacion(triplete):
    archivo = open("diccionario.txt", "r")
    datos = archivo.read()
    tam = len(datos)
    archivo.close()
    archivo = open("diccionario.txt", "r")
    diccionario = {}
    secuencia = ''
    caracter = ''
    secuencia = archivo.read(3)
    caracter = archivo.read(1)
    caracter = archivo.read(1)
    diccionario[secuencia] = caracter
    tam = tam - 5

    while (tam > 0):
        caracter = archivo.read(1)
        tam = tam - 1
        while (caracter == '\n' or caracter == ' '):
            caracter = archivo.read(1)
            tam = tam - 1

        secuencia = caracter + archivo.read(2)
        caracter = archivo.read(1)
        caracter = archivo.read(1)
        tam = tam - 4
        diccionario[secuencia] = caracter

    caracter = diccionario[triplete]


    return caracter

def traducir_ADN_ARN(ADN):
    #Convierto el ADN en ARN
    ARN = ''
    for i in ADN:
        if (i == 'T'):
            ARN = ARN + 'U'
        else:
            ARN = ARN + i
    return ARN

def ADN_inverso(ADN):

    ADN_5_3 = ''
    for i in ADN:
        if i == 'T':
            ADN_5_3 = ADN_5_3 + 'A'
        elif i == 'A':
            ADN_5_3 = ADN_5_3 + 'T'
        elif i == 'C':
            ADN_5_3 = ADN_5_3 + 'G'
        elif i == 'G':
            ADN_5_3 = ADN_5_3 + 'C'
        else:
            print("Las has jodido muchisimo o has leido datos equivocados. Posiblemente lo primero.")

    return ADN_5_3


def obtenerProteina(ARN,posicion):


    triplete = ''
    stop = ["TAA", "TAG", "TGA"]
    proteina = ''
    parada = 0
    while(parada == 0 and (posicion + 3) < len(ARN)):
        triplete = ARN[posicion:posicion+3]
        if triplete != stop[0] and triplete != stop[1] and triplete != stop[2]:
            proteina = proteina + ObtenerCodficacion(triplete)
            posicion = posicion + 3
        else:
            parada = 1

        triplete = ''

    if parada == 0:
        proteina = ''
    return proteina

def string_reverse(string):
    return string[::-1]


nombre_archivo = "ejemplo.txt"

archivo = open(nombre_archivo,"r")

datos = archivo.read()
tam = len(datos)

archivo.close()

archivo = open(nombre_archivo,"r")

caracter = ''
ADN = ''
etiqueta = archivo.readline() #Leo la etiqueta
tam = tam - len(etiqueta)


#Obtengo la cadena de ADN
while(tam > 0):
    caracter = archivo.read(1)
    tam = tam - 1
    if(caracter != '\n'):
        ADN = ADN + caracter

star = "ATG"
sub_cadena = ''
proteina = ''

########################################33

archivo = open("diccionario.txt", "r")
datos = archivo.read()
tam = len(datos)
archivo.close()
archivo = open("diccionario.txt", "r")
diccionario = {}
secuencia = ''
caracter = ''
secuencia = archivo.read(3)
caracter = archivo.read(1)
caracter = archivo.read(1)
diccionario[secuencia] = caracter
tam = tam - 5

while (tam > 0):
    caracter = archivo.read(1)
    tam = tam - 1
    while (caracter == '\n' or caracter == ' '):
        caracter = archivo.read(1)
        tam = tam - 1

    secuencia = caracter + archivo.read(2)
    caracter = archivo.read(1)
    caracter = archivo.read(1)
    tam = tam - 4
    diccionario[secuencia] = caracter


########################################


print(proteina_normal)
#Proceso la cadena de ADN
for i in range(len(ADN)):
    if ((i + 3) <= len(ADN)):
        sub_cadena = ADN[i:i+3]
        if(sub_cadena == star):
            proteina = obtenerProteina(ADN,i)
            print(proteina)


ADN_invertido = ADN_inverso(ADN)


for j in range(len(ADN_invertido)):
    if (j+3) <= len(ADN_invertido):
        sub_cadena = ADN_invertido[j:j+3]
        if(sub_cadena == star):
            proteina = obtenerProteina(ADN_invertido,j)
            print(proteina)


archivo.close()