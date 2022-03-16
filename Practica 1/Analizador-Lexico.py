from pickletools import optimize
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

#Construcción del analisis lexico
lexer = lex.lex(optimize = 1)

#Prueba
data = '''
    3 + 4 * 10
      + -20 *2
'''

lexer.input(data)

#Tokenizacion
while True:
    tok = lexer.token()
    if not tok:
        break #Fin a la entrada de información para el analizador
    print(tok)