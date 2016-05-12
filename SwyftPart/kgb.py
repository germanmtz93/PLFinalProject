#------------------------------------------------------------
# HMM tokenizer
# ------------------------------------------------------------

import ply.lex as lex

# Reserved words
reserved = {
    'IF'     : 'if',
    'FOR'    : 'for',
    'IN'     : 'in',
    'LET'    : 'let',
    'COUNT'  : 'count',
    'PRINT'  : 'print',
    'INT'    : 'int',
    'FLOAT'  : 'float',
    'BOOL'   : 'bool',
    'LIST'   : 'list',
    'TUPLE'  : 'tuple',
    'OBJECT' : 'object',
    'STRING' : 'string',
}

# List of token names.
tokens = [
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'LCURLY', 'RCURLY', 'DOT', 'DDL', 'EQUALS',\
    'BSLASH', 'DQUOTE', 'COMMA', 'INTEGER', 'IDENTIFIER', 'CLFLOAT', 'CLSTRING',\
    ] + list(reserved.keys())

t_LET = r'let'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\['
t_RBRACE = r']'
t_LCURLY = r'{'
t_RCURLY = r'}'
t_DOT = r'\.'
t_DDL = r'\.\.<'
t_BSLASH = r'\\'
t_DQUOTE = r'"'
t_COMMA = r','
t_EQUALS = r'='

def t_INTEGER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print "Line %d: Number %s is too large!" % (t.lineno,t.value)
        t.value = 0
    return t

def t_CLFLOAT(t):
    r'[0-9]+[\.][0-9]*'
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value.upper() in reserved:
        # print "In t_IDENTIFIER, saw: ", t.value
        t.type = t.value.upper()
    return t

def t_CLSTRING(t):
    r'"[a-zA-Z0-9_+\*\- :,]*"'
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)

# Build the lexer
lex.lex()

# BNF Parsing rules

names = {}

def p_assignment(p):
    '''assignment : IDENTIFIER expression EQUALS expression'''
    names[p[2]] = p[4]
    p[0] = p[4]

def p_expression(p):
    '''expression : INT
            | FLOAT
            | BOOL
            | LIST
            | TUPLE
            | OBJECT
            | STRING'''

def p_function (p):
    '''function : expression DOT IDENTIFIER'''
    names[p[3]] = len(names[p[1]])
    p[0] = len(p[1])

import ply.yacc as yacc
yacc.yacc()

with open('testkgb.c', 'r') as content_file:
    content = content_file.read()
yacc.parse(content)