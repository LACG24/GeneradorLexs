import ply.lex as lex

tokens = ['INT', 'FLOAT']

t_ignore = ' \t'

#Prueba de capturar enteros positivos con guiones bajos intermedios
def t_INT(t):
    r'\d+(?:_\d+)*'
    t.value = int(t.value.replace('_', ''))
    return t


def getLexer():
    return lex.lex()



