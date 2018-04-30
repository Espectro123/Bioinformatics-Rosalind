from decimal import *
getcontext().prec = 9 # Ajusto la precision a 9

archivo = open("rosalind_prtm.txt","r") #Abro el archivo. Solo lectura

datos = archivo.read() # Leo el archivo entero hasta EOF

#Creo el diccionario con los pesos de las proteinas
#Si se solicita una letra que no esta explota
pesos_proteina = {
    'A': 71.03711,'C': 103.00919,
    'D': 115.02694,'E': 129.04259,
    'F': 147.0641,'G': 57.02146,
    'H': 137.05891,'I': 113.08406,
    'K': 128.09496,'L': 113.08406,
    'M': 131.04049,'N': 114.04293,
    'P': 97.05276,'Q': 128.05858,
    'R': 156.10111,'S': 87.03203,
    'T': 101.04768,'V': 99.06841,
    'W': 186.07931,'Y': 163.06333,
}

sumatoria = 0.0

#Recorro la cadena de la proteina
for i in datos:
    if(i != '\n'): #Ignoro los saltos de linea
        sumatoria = sumatoria + pesos_proteina[i] #Calculo la sumatoria

print(sumatoria) #Imprimo el resultado con una precision de 9 digitos