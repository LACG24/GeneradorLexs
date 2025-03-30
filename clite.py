import ply.lex as lex

tokens = ['INT', 'FLOAT']

t_ignore = ' \t'

def t_FLOAT(t):
    r'([0-9]*(_*[0-9]+)?\.[0-9]*([0-9]+_*)?([eE][+-]?[0-9_]+)?)|([0-9_]+[eE][0-9_]+)'
    t.value = float(t.value)
    return t

# Numeros con guion bajo 'si', pero no dos consecutivos
def t_INT(t):
    r'[0-9]+(_[0-9]+)*'
    t.value = int(t.value.replace('_', ''))
    return t

# Funcion para manejar errores
def t_error(t):
    raise lex.LexError(f"Illegal character '{t.value[0]}'", t.value[0])


def getLexer():
    return lex.lex()
