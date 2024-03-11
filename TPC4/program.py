import ply.lex as lex
import re


tokens = [
    'SELECT',
    'FROM',
    'WHERE',
    'VARIABLE',
    'COMMA',
    'COMP',
    'NUMBER'
]



t_SELECT = r'SELECT'
t_FROM = r'FROM'
t_WHERE = r'WHERE'
t_VARIABLE = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_COMMA =r','
t_COMP = r'(<=?|=|>=?)'
t_ignore = ' \t'


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t
    
def t_error(t):
    print(f"Error")
    t.lexer.skip(1)
    
def main():
    lexer = lex.lex()
    data = input()
    lexer.input(data)

    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)
        
if __name__ == '__main__':
    main()

