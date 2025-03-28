import ply.lex as lex

tokens = ['INT', 'FLOAT']

t_ignore = ' \t'

# Numeros con guion bajo 'si', pero no dos consecutivos
def t_INT(t):
    r'[0-9]+(_[0-9]+)*'
    t.value = int(t.value.replace('_', '')) # Reemplazar guiones bajos
    return t

#Para que no salga el warning
def t_error(t):
    raise lex.LexError(f"Illegal character '{t.value[0]}'", t.value[0]) #no se si esta bien


def getLexer():
    return lex.lex()



