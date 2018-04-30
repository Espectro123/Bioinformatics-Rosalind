import urllib.request

archivo = open("rosalind_mprt.txt","r")

lista_IDs_string = archivo.read()

archivo.close()

lista_IDs = []
caracter = ''
etiqueta = ''

#Obtengo una lista con las IDS
for i in range(len(lista_IDs_string)):
    if(lista_IDs_string[i] != '\n'):
        etiqueta = etiqueta + lista_IDs_string[i]
    else:
        lista_IDs.append(etiqueta)
        etiqueta = ''
        etiqueta = ''

#lista_IDs.append(etiqueta)


url = "http://www.uniprot.org/uniprot/"
formato = ".fasta"

#El mofit a usar es:
# N,¬P,S o T, ¬P

#Obtengo los datos de la web y los guardo en ficheros de texto.
for i in range(len(lista_IDs)):
    link = url + lista_IDs[i] + formato # Creo el link al formato fasta de la proteina
    response = urllib.request.urlopen(link) # Abro la web
    raw_data = response.read() #Leo los datos
    datos = raw_data.decode('utf-8') #Transformo los datos en formato txt
    #Escribo los datos en un fichero de texto
    with open(lista_IDs[i]+".txt", 'w') as f:
        f.write(datos)

protein = ''
caracter = ''
etiqueta = ''
sub_cadena = ''
lista_indices = []
contador = 0

#Abro el archivo en el que se escribira la solucion
resultados = open("Resultados.txt",'w')

#Recorro todos los archivos creados
for i in range(len(lista_IDs)):
    #Obtengo el tamaño del archivo
    archivo = open(lista_IDs[i]+".txt","r")
    datos = archivo.read()
    tam = len(datos)
    archivo.close()

    #Obtengo la cadena de la proteina
    archivo = open(lista_IDs[i]+".txt","r")
    etiqueta = archivo.readline()
    tam = tam - len(etiqueta)
    while(tam > 0):
        caracter = archivo.read(1)
        tam = tam - 1
        if(caracter != '\n'):
            protein = protein + caracter


    #Busco el motif
    for j in range(len(protein)):
        sub_cadena = protein[j:j+4]
        if(len(sub_cadena) == 4):
            if(sub_cadena[0] == 'N' and sub_cadena[1] != 'P' and (sub_cadena[2] == 'S' or sub_cadena[2] == 'T') and sub_cadena[3] != 'P'):
                lista_indices.append(j+1)
        sub_cadena = ''

    print(lista_indices)
    #Convierto la lista de indices a un string
    indices = ''
    indices =   ''.join(str(e)+' ' for e in lista_indices)
    #Escribo en el archivo si hay algun mofit en la proteina
    if(len(indices) != 0):
        resultados.writelines(lista_IDs[i] + '\n')
        resultados.writelines(indices + '\n')

    indices = ''
    lista_indices = []
    protein = ''


resultados.close()











