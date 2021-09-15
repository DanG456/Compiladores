#Practica 1

#Se abren ambos archivos txt para obtener los datos para crear los autómatas correspondientes
with open("1.txt","r") as f:
    linea = [lin.rstrip() for lin in f] #rstrip para limpiar las listas de los saltos de linea

with open("2.txt","r") as f2:
    linea2 = [lin2.rstrip() for lin2 in f2] #rstrip para limpiar las listas de los saltos de linea

#Funciones
#Funcion para separar cada segmento de los indices de las lineas y meterlos en listas correspondientes
def separarLista(nombre_lista):
    cnombre_lista = str(nombre_lista)
    cadena_lista = []
    for elemento in cnombre_lista:
        cadena_lista.append(elemento)
        if(elemento == "," or elemento == "'" or elemento == "[" or elemento == "]"):
            cadena_lista.remove(elemento)
    return cadena_lista

#Funcion para leer la cadena y recorrerla
def Automata(estado_inicial):
    edo_inicial = estado_inicial
    cadena_caracter = []
    for caracter in cadena:
        cadena_caracter.append(caracter)
    #Se comprueba con el metodo que el caracter pertenezca al alfabeto
    caracter_valido = comprobarCaracter(cadena_caracter)
    #Se meten los datos de la tabla de transiciones en un diccionario con las keys Actual, Valor y Siguiente
    diccionario_tablas = asignarTransiciones(tablatrans_limpia)
    #Se comienza a analizar la cadena y el camino que debe tomar el automata
    if (edo_inicial == '0'):
        for key, value in diccionario_tablas:
            print(key, value)
        print("Estado inicial Q0")
        #for CC in cadena_caracter:
         #   if(CC == ):



def comprobarCaracter(caracter):
    for car in caracter:
        if(car == alfabetolimpio[0] or car == alfabetolimpio[1]):
            caracter_valido = True
        else:
            print("El caracter "+ car + " no pertenece al alfabeto")
            caracter_valido = False
    return caracter_valido

def asignarTransiciones(listatransiciones):
    edoactual = []
    valortrans = []
    edosiguiente = []
    diccionario = {'actual': edoactual,'valor': valortrans,'siguiente': edosiguiente}
    indice_actual = 0
    indice_valor = 1
    indice_siguiente = 2
    for listrans in listatransiciones: #La cantidad de elementos en listatransiciones es de 35
        if(indice_actual <= 35):
            edoactual.append(listatransiciones[indice_actual])
            valortrans.append(listatransiciones[indice_valor])
            edosiguiente.append(listatransiciones[indice_siguiente])
            diccionario['actual'] = edoactual
            diccionario['valor'] = valortrans
            diccionario['siguiente'] = edosiguiente
            indice_actual = indice_actual + 4
            indice_valor = indice_valor + 4
            indice_siguiente = indice_siguiente + 4

    return diccionario

#1.- Guarda la cantidad de estados en un arreglo y la forma en que se denomina a los mismos
estados = []
estados.append(linea[0])
estados_limpios = separarLista(estados)

#2.- Guardar los componentes del alfabeto en una lista para su uso
alfabetolist = []
alfabetolist.append(linea[1])
alfabetolimpio = separarLista(alfabetolist)

#3.- Guarda el estado inicial para comenzar el autómata
edo_ini = []
edo_ini.append(linea[2])
edo_ini_limpio = separarLista(edo_ini)
#5.- Guardar la tabla de transiciones en una lista para su uso
tablatrans = []
transiciones = 4
numtrans = 4

while(numtrans < 13):
    tablatrans.append(linea[transiciones])
    transiciones = transiciones + 1
    numtrans = numtrans + 1
tablatrans_limpia = separarLista(tablatrans)
print(linea)
#print(estados_limpios)
#print(alfabetolimpio)
#print(edo_ini_limpio)
print(tablatrans)
print(tablatrans_limpia)
print(edo_ini_limpio)
cadena = input("Ingresa la cadena que debe evaluar el autómata")
Automata(edo_ini_limpio)

f.close()
f2.close()

