
import ply.lex as lex

#reserved = { 'LET'     : 'let' }

tokens = [
             'EQUALS',"DQUOTE", 'CLSTRING','IDENTIFIER','LBRACE', 'RBRACE', 'COMMA', 'DOT', 'RPAREN', 'LPAREN'
         ] #+ list(reserved.keys())

t_DQUOTE = r'"'
t_EQUALS = r'='
t_LBRACE = r'\['
t_RBRACE = r']'
t_COMMA  = r','
t_DOT = r'\.'
t_RPAREN = r'\)'
t_LPAREN = r'\('

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore  = ' \t'

def t_CLSTRING(t):
    r'"[a-zA-Z0-9_+\*\- :,]*"'
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
  #  if t.value.upper() in reserved:
  #      print "In t_IDENTIFIER, saw: ", t.value
  #      t.type = t.value.upper()
    return t

names = {}

def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)

# Build the lexer
lex.lex()

def p_assignment(p):
    '''assignment : IDENTIFIER IDENTIFIER EQUALS CLSTRING
                  | IDENTIFIER IDENTIFIER EQUALS CLIST
                  | IDENTIFIER IDENTIFIER EQUALS COUNT
                  '''
    if p[1] == 'let':
        names[p[2]] = p[4]
    else:
        pass
    p[0] = p[4]
    print names[p[2]]

def p_DISPLAY(p):
    '''DISPLAY : IDENTIFIER LPAREN CLSTRING RPAREN'''
    #print p[1]
    if p[1] == 'print':
        print(p[3])
    else:
        pass

def p_CLIST(p):
    '''CLIST :  LBRACE CLSTRING COMMA CLSTRING COMMA CLSTRING RBRACE'''
    a = []
    a.append(p[2].strip('"'))
    a.append(p[4].strip('"'))
    a.append(p[6].strip('"'))
    p[0]=a
    print a

def p_COUNT(p):
    '''COUNT : IDENTIFIER DOT IDENTIFIER'''
    if p[3] == 'count':
        p[0] = len(names[p[1]])
    else:
        pass
    print(p[0])

def emptyline(self):
    """Do nothing on empty input line"""
    pass# Error handling rule

def p_error(p):
    print "At line: ", p.lexer.lineno,
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

import ply.yacc as yacc
yacc.yacc()

with open('testkgb.c', 'r') as content_file:
    content = content_file.read()
yacc.parse(content)

