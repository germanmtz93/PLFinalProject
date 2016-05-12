
import ply.lex as lex

#reserved = { 'LET'     : 'let' }
names = {}

tokens = [
             'EQUALS',"DQUOTE", 'CLSTRING','IDENTIFIER','LBRACE', 'RBRACE', 'COMMA', 'DOT', 'RPAREN', 'LPAREN','INTEGER','BSLASH'
         ] #+ list(reserved.keys())

t_DQUOTE = r'"'
t_EQUALS = r'='
t_LBRACE = r'\['
t_RBRACE = r'\]'
t_COMMA  = r','
t_DOT = r'\.'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_BSLASH = r'\\'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore  = ' \t'

def t_CLSTRING(t):
    r'"[a-zA-Z0-9_+\*\- :,]*"'
    return t

def t_INTEGER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print "Line %d: Number %s is too large!" % (t.lineno,t.value)
        t.value = 0
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
  #  if t.value.upper() in reserved:
  #      print "In t_IDENTIFIER, saw: ", t.value
  #      t.type = t.value.upper()
    return t

def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)

# Build the lexer
lex.lex()

#def p_DISPLAY(p):
#    '''DISPLAY : IDENTIFIER LPAREN CLSTRING RPAREN'''
#    #print p[1]
#    if p[1] == 'print':
#        print(p[3])

def p_assignment(p):
    '''assignment : IDENTIFIER IDENTIFIER EQUALS CLSTRING
                  | IDENTIFIER IDENTIFIER EQUALS CLIST
                  | IDENTIFIER IDENTIFIER EQUALS COUNT
                  | IDENTIFIER LPAREN CLSTRING RPAREN
                  | IDENTIFIER LPAREN DQUOTE IDENTIFIER INTEGER IDENTIFIER BSLASH LPAREN IDENTIFIER LBRACE INTEGER RBRACE RPAREN DQUOTE RPAREN
                  '''
    if p[1] == 'let':
        names[p[2]] = p[4]
        print names[p[2]]
        p[0] = p[4]
    elif p[1] == 'print' and len(p) == 5:
        print(p[3])
        p[0] = p[3]
    elif p[1] == 'print' and len(p) == 16:
        listy = names[p[9]]
        toPrint = p[4] + " " + str(p[5]) + " " + p[6] + " " + listy[p[11]]
        print(toPrint)
    else:
        pass


def p_CLIST(p):
    '''CLIST :  LBRACE CLSTRING COMMA CLSTRING COMMA CLSTRING RBRACE'''
    a = []
    a.append(p[2].strip('"'))
    a.append(p[4].strip('"'))
    a.append(p[6].strip('"'))
    p[0]=a

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
with open('testkgb2.c', 'r') as content_file:
    content2 = content_file.read()
yacc.parse(content2)
with open('testkgb3.c', 'r') as content_file:
    content3 = content_file.read()
yacc.parse(content3)
with open('testkgb4.c', 'r') as content_file:
    content4 = content_file.read()
yacc.parse(content4)

