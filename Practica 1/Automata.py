import re
import ply.lex as lex

#Lista de palbras reservadas
reservadas = (
    'INCLUDE',
    'STD',
    'PRINT',
    'IMPORT',
    'RETURN',
    'VOID',
    'INT',
    'FLOAT',
)

#Lista de tokens
tokens = reservadas + (
    'PARIZQ',
    'PARDER',
    'SUMA',
        'RESTA',
        'MULT',
        'DIV',
        'POTENCIA',
        'MODULO',
        'CORIZQ',
        'CORDER',
        'LLAIZQ',
        'LLADER',
        'ENTERO',
    )

#Expresiones regulares

t_SUMA = r'\+'
t_RESTA = r'-'
t_MULT = r'\*'
t_DIV = r'/'
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_CORIZQ = r'\['
t_CORDER = r'\]'
t_LLAIZQ = r'{'
t_LLADER = r'}'
t_MODULO = r'\%'
t_ASIGNAR = r'='

#Definición de Reglas

def t_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

#Definicion de regla que permite rastrear numeros de linea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

#Cadena que contiene caracteres a ignorar, en este caso espacios y tabulaciones
t_ignore = ' \t'

#Definición de manejo de errores
def t_error(t):
    print("Caracter no permitido '%s'" % t.value[0])
    t.lexer.skip(1)

def t_IDENTIFICADOR(t):
    r'\w+(_\d\w)*'
    return t

def t_CADENA(t):
    r'\"?(\w+ \ *\w*\d* \ *)\"?'
    return t

def t_comments(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')
    print("Comentario de multiple linea")

def t_comments_ONELine(t):
    r'\/\/(.)*\n'
    t.lexer.lineno += 1
    print("Comentario de una linea")

lexer = lex.lex(optimize = 1)

#Definimos la funcion caracter 
def caracter(character):
    global simbolo
    simbolo=""
    global Fin
    Fin=""
    digito="[0-9]"
    operador="[(+|\-|*|/)]"
    
    #comparamos si es digito u operador
    if(re.match(digito,character)):
        simbolo=" Digito "
        return 0
    else:
        if(re.match(operador,character)):
            simbolo="Operador"
            return 1
        else:
            if(character==Fin):
                return 2
        
        #si no es ni un digito ni un operador entonces es un caracter no valido
        print("Error el ",character,"no es valido")
        exit()

#definimos al la funcion  encabezado
def encabezado():
    print("""|  Edo. Actual |Caracter |  Simbolo  |Edo. Siguiente |""")
    body()

#definimos la funcion contenido donde guarda cada valor despues de encontrarlo en un ciclo
def contenido(estadosig,character,simbolo,estado):
    print("|     ",estadosig,"      |  ",character,"    |",simbolo," |     ",estado,"       |")
    body()

#solo muestra la linea que se repetira cada vez que la mandemos a llamar
def body():
    print("+--------------+---------+-----------+---------------+")

#MAIN
#Este es la tabla de transiciones del automata AFD creado
tabla=[[1,"E","E"],[1,2,"E"],[3,"E","E"],[3,2,"A"]]
estado = 0

print ("""+-------------------------------------+
|    Ingrese una cadena a evaluar:    |
+-------------------------------------+""")
cadena = input()
body()
encabezado()

#ciclo para recorrer la cadena
for  character in cadena:
    estadosig=estado
    
    #llamamos al metodo para saber si es un caracter valido y el valor retornado se guarda en charcaracter
    charcaracter= caracter(character)
    
    #guardamos en estado el valor obtenido en la tabla segun las cordenadas que recibio anteriormente
    estado=tabla[estado][charcaracter]
    
    #Si el valor obtenido es una E imprimimos cadena no valida
    if (estado=="E"):
        print("|     ",estadosig,"      |  ",character,"    |",simbolo," |     ",estado,"       |")
        body()
        print("""|              Cadena No Valida                      |
+----------------------------------------------------+""")
        exit()
    contenido(estadosig,character,simbolo,estado)

#al concluir si el estado no es 3 (el de aceptacion) imprimimos cadena no valida    
if(estado!=3):
        print("""|              Cadena No Valida                      |
+----------------------------------------------------+""")

#si el estado es 3 es una cadena de aceptacion
if(estado==3):
    print("|     ",estado,"      |         |    FND    |               |")
    body()
    print("""|                Cadena Valida                       |
+----------------------------------------------------+""")
    lexer.input(cadena)
    #Tokenizacion
    while True:
        tok = lexer.token()
        if not tok:
            break #Fin a la entrada de información para el analizador
        print(tok)
