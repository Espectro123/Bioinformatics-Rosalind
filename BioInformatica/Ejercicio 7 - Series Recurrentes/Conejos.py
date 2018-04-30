def descendencia(meses,hijos):
    bebes = 2
    jovenes = 0
    adultos = 0

    for i in range(meses):
        adultos = adultos + jovenes
        jovenes = bebes
        if(adultos % 2 == 0):
            bebes = adultos * hijos
        else:
            bebes = (adultos-1) * hijos


    return (adultos + jovenes)/2





archivo = open("rosalind_fib.txt","r")
datos = archivo.read()
tam = len(datos)
archivo.close()


#Obtengo los datos
#Hay que borrar el ultimo caracter del archivo que nos da la pagina web. Es un espacio sin mas
if(tam == 4):
    meses = datos[0]
    meses = meses + datos[1]
    hijos = datos[3]
else:
    meses = datos[0]
    hijos = datos[2]

poblacion = descendencia(int(meses),int(hijos))

print(poblacion)
