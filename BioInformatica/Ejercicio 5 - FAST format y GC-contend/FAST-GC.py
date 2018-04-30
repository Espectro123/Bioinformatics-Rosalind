

# Abro el archivo para obtener la longuitud del nombre del identificador
archivo = open("rosalind_gc.txt","r")

linea = archivo.readline()
tam_nombre = len(linea) - 2 #Le resto dos porque le quito el simbolo > y el salto de linea
tam_archivo = archivo.read() # Leo el resto del archivo y averiguo el la longuitud del mismo
tam_archivo = len(tam_archivo) + len(linea)

archivo.close()

archivo = open("rosalind_gc.txt","r")
datos = ''
ADN = ''
etiqueta = ''
porcentaje = 0.0
contador = 0
mejor_etiqueta = ''
mejor_porcentaje = 0.0


while(tam_archivo != 0):

    #Leo la etiqueta
    if(datos != '>'):
        datos = archivo.read(1)
        tam_archivo = tam_archivo - 1
    datos = archivo.read(tam_nombre)
    tam_archivo = tam_archivo - tam_nombre
    etiqueta = datos

    while(datos != '>' and tam_archivo != 0):
        datos = archivo.read(1)
        tam_archivo = tam_archivo - 1
        if(datos != '>' and datos != '\n'):
            ADN = ADN + datos

    for i in ADN:
        if(i == 'C' or i == 'G'):
            contador = contador + 1

        porcentaje = (contador/len(ADN)) * 100

    if(porcentaje > mejor_porcentaje):
        mejor_porcentaje = porcentaje
        mejor_etiqueta = etiqueta


    contador = 0
    ADN = ''
    etiqueta = ''


print(mejor_etiqueta)
print(mejor_porcentaje)