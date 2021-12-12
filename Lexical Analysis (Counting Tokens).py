import ply.lex as lex

tokens = (
"KEYWORD",
"VARNAME",
"INVNAME",
"INT",
"FLOAT",
"LPAREN",
"RPAREN",
"OPERATOR",
"SEPARATOR",
"PRTSTR"
)

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEPARATOR = r';|,'
t_PRTSTR = r'".*"'
t_ignore = ' '

def t_KEYWORD(t):
    r'int|return'
    return t

def t_VARNAME(t):
    r'[a-zA-Z][a-zA-Z_0-9]*'
    return t

def t_INVNAME(t):
    r'[0-9]+[a-zA-Z]+[0-9]*';
    print('Invalid character %s'%t.value)
    t.lexer.skip(1)
    
def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_OPERATOR = r'\+=|-=|\*=|/=|\+\+|--|==|\+|-|\*|/|='

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
     
def t_error(t):
    print("Illegal character %s"%t.value[0])
    t.lexer.skip(1)
    
lexer = lex.lex()

statements = ['printf("Lex Analysis (lex token) is",ans);',
              '34+ 4 * 10 + x -20 *2'
		'289 * 324 / (29+36)-345*(100/2)']

for statement in statements:
    print('\nLexical analysis of: '+statement)
    TT = 0
    lexer.input(statement)
    while True:
        tok = lexer.token()
        if not tok: break
        TT+=1
        print(tok)
    
    print('Total tokens =',TT)
