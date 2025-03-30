import ply.lex as lex

tokens = ['INT', 'FLOAT']

t_ignore = ' \t'

#Prueba de capturar enteros positivos
def t_INT(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t


def getLexer():
    return lex.lex()



