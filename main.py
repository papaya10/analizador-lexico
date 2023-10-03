import ply.lex as lex

reserved = {
    'SELECT': 'SELECT',
    'FROM': 'FROM',
    'WHERE': 'WHERE'
}

tokens = [
    'ID',
    'OPREL',
    'NUMERO'
] + list(reserved.values())

t_OPREL = r'[=<>!]+'
t_ignore = ' \t'

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value.upper(), 'ID')
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Carácter inválido '{t.value[0]}'")
    t.lexer.skip(1)

# Construcción del lexer
lexer = lex.lex()

# Prueba del lexer
data = "SELECT col1, col2 from mi_Tabla wHERE col1 < 20 $"
lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(f"TOKEN: {tok.type}, VALOR: {tok.value}")

