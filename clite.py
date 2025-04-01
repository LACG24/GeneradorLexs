import ply.lex as lex

tokens = ['FLOAT', 'INT', 'STRING']

t_ignore = ' \t'

def t_FLOAT(t):
    r'([0-9]*(_[0-9]+)?(\.([0-9]*|([0-9]+_[0-9]+))([eE][+-]?[0-9]+(_[0-9]+)?)?|[eE][0-9]+))'
    t.value = float(t.value)
    return t

# Numeros con guion bajo 'si', pero no dos consecutivos
def t_INT(t):
    r'[0-9]+(_[0-9]+)*'
    t.value = int(t.value.replace('_', ''))
    return t

# Si hay \", lo dejamos intacto; si no, quitamos las comillas
def t_STRING(t):
    r'^[a-zA-Z"|"][a-zA-Z\s%"\\]*$'
    t.value = t.value if '\\"' in t.value else t.value[1:-1]
    return t

# Funcion para manejar errores
def t_error(t):
    raise lex.LexError(f"Illegal character '{t.value[0]}'", t.value[0])


def getLexer():
    return lex.lex()
