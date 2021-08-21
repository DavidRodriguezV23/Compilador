import ply.lex as lex

result_lexema = []

lines = []
res = []
reserved = ('INCLUDE', 'USING', 'NAMESPACE', 'STD', 'COUT',
            'CIN', 'GET', 'CADENA', 'RETURN', 'VOID', 'INT', 'FLOAT', 'ENDL',)
tokens = reserved + ('IDENTIFICADOR', 'ENTERO', 'ASIGNAR', 'SUMA', 'RESTA', 'PUNTO',
                     'MULT', 'DIV', 'POTENCIA', 'MODULO', 'MINPLUS', 'PLUSPLUS',
                     'SI', 'SINO', 'MIENTRAS', 'PARA', 'AND', 'OR', 'NOT', 'MINUSMINUS',
                     'MENORQUE', 'MAYORQUE', 'MENORIGUAL', 'MAYORIGUAL', 'IGUAL', 'DISTINTO', 'NUMERAL',
                     'PARIZQ', 'PARDER', 'CORIZQ', 'CORDER', 'LLAIZQ', 'LLADER', 'PUNTOCOMA',
                     'COMA', 'COMDOB', 'MAYORDER', 'MAYORIZQ')

t_SUMA = r'\+'
t_RESTA = r'-'
t_MINUSMINUS = r'\-\-'
t_MULT = r'\*'
t_DIV = r'/'
t_MODULO = r'\%'
t_PUNTO = r'\.'
t_POTENCIA = r'(\*{2} | \^)'
t_ASIGNAR = r'='
t_AND = r'\&{2}'
t_OR = r'\|{2}'
t_NOT = r'\!'
t_MENORQUE = r'<'
t_MAYORQUE = r'>'
t_PUNTOCOMA = r';'
t_COMA = r','
t_PARIZQ = r'\('
t_PARDER = r'\)'
t_CORIZQ = r'\['
t_CORDER = r'\]'
t_LLAIZQ = r'\{'
t_LLADER = r'\}'
t_COMDOB = r'\"'


def t_INCLUDE(t):
    r'include'
    return t


def t_USING(t):
    r'using'
    return t


def t_NAMESPACE(t):
    r'namespace'
    return t


def t_STD(t):
    r'std'
    return t


def t_COUT(t):
    r'cout'
    return t


def t_CIN(t):
    r'cin'
    return t


def t_GET(t):
    r'get'
    return t


def t_ENDL(t):
    r'endl'
    return t


def t_SINO(t):
    r'else'
    return t


def t_SI(t):
    r'if'
    return t


def t_RETURN(t):
    r'return'
    return t


def t_VOID(t):
    r'void'
    return t


def t_MIENTRAS(t):
    r'while'
    return t


def t_PARA(t):
    r'for'
    return t


def t_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_IDENTIFICADOR(t):
    r'\w+(_\d\w)*'
    return t


def t_CADENA(t):
    r'\"?(\w+ \ *\w*\d* \ *)\"?'
    return t


def t_NUMERAL(t):
    r'\#'
    return t


def t_PLUSPLUS(t):
    r'\+{2}'
    return t


def t_MENORIGUAL(t):
    r'<='
    return t


def t_MAYORIGUAL(t):
    r'>='
    return t


def t_IGUAL(t):
    r'=='
    return t


def t_MAYORDER(t):
    r'<<'
    return t


def t_MAYORIZQ(t):
    r'>>'
    return t


def t_comments_ONELINE(t):
    r'\/\/(.)*\n'
    t.lexer.lineno += 1
    print('Comentario de una linea')


def t_comments_MULTIPLELINE(t):
    r'[/]\*[^/**/]+\*[/]'
    t.lexer.lineo += t.value.count('\n')


t_ignore = '\t'


def t_error(t):
    global result_lexema
    estate = '** Token invalido en la linea {:4} Valor {:6} Posicion {:4}'.format(
        str(t.lineno), str(t.value), str(t.lexpos)
    )
    result_lexema.append(estate)
    t.lexer.skip(1)


def load_file(path):

    global lines

    with open(path, 'r') as f:
        lines = f.readlines()
    '''
    print("El código a analizar será:\n")
    for line in lines:
        print(line)
    '''
    return lines


def analize(lines):
    global result_lexema
    count = 0

    for line in lines:
        temp = []
        print(line)
        analizador = lex.lex()
        analizador.input(line)
        while True:
            tok = analizador.token()
            if not tok:
                break
            estado = "Linea {:4} Tipo {:16} Valor {:16} Posicion {:4}".format(str(tok.lineno + count), str(tok.type),
                                                                             str(tok.value), str(tok.lexpos))
            temp.append(estado)
            result_lexema.append(estado)

        if(temp != []):
            print(temp)
            print('\n')

        count += 1

    return result_lexema
