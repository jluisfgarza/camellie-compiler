# References:
#   https://www.dabeaz.com/ply/ply.html
#   https://www.youtube.com/watch?v=Hh49BXmHxX8&list=PLBOh8f9FoHHg7Ed_4yKhIbq4lIJAlonn8
# ----------------------------------------------
#
import sys

sys.path.insert(0, "../..")

if sys.version_info[0] >= 3:
  raw_input = input

tokens = [
  "PROGRAM",
  "PRINT",
  "VAR",
  "FLOAT_TYPE",
  "INT_TYPE",
  "INT",
  "FLOAT",
  "STRING",
  "IF",
  "ELSE",
  "ID",
  "COLON",
  "SEMICOLON",
  "GREATER_THAN",
  "LESS_THAN",
  "COMMA",
  "PLUS",
  "MINUS",
  "MULTIPLY",
  "DIVIDE",
  "EQUALS",
  "NOT_EQUAL",
  "LEFT_BRACE",
  "RIGHT_BRACE",
  "LEFT_PARENTHESIS",
  "RIGHT_PARENTHESIS",
]

t_PROGRAM    = r'program'
t_ignore = " \t"
t_PRINT = r'PRINT'
t_VAR = r'VAR'
t_FLOAT_TYPE = r'FLOAT'
t_INT_TYPE = r'INT'
t_STRING  = r'\"(\\.|[^"\\])*\"'
t_IF = r'IF'
t_ELSE = r'ELSE'
t_ID = r'[a-zA-Z][_a-zA-Z0-9]*'
t_COLON = r'\:'
t_SEMICOLON = r'\;'
t_GREATER_THAN = r'\>'
t_LESS_THAN = r'\<'
t_COMMA = r'\,'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'
t_EQUALS = r'\='
t_NOT_EQUAL = r'\<>'
t_LEFT_BRACE = r'\{'
t_RIGHT_BRACE = r'\}'
t_LEFT_PARENTHESIS = r'\('
t_RIGHT_PARENTHESIS = r'\)'

# cte_FLOAT
def t_FLOAT(t):
	r'[0-9]+\.[0-9]+'
	t.value = float(t.value)
	return t
# cte_INT
def t_INT(t):
	r'[0-9]+'
	t.value = int(t.value)
	return t
#  NEW LINW \n
def t_newline(t):
  r"\n+"
  t.lexer.lineno += t.value.count("\n")
#  COMMENT #
def t_COMMENT(t):
  r'\#.*'
  pass # Token discarded
# Error Handling
def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  t.lexer.skip(1)

# Build the lexer
import ply.lex as lex
lex.lex()
# 

def p_PROGRAM(p):
  """
  program : PROGRAM ID SEMICOLON VARS BLOQUE
    | PROGRAM ID SEMICOLON BLOQUE
  """
# 
def p_VARS(p):
  """
  VARS : VAR ID VARS_P
  """
def p_VARS_P(p):
  """
  VARS_P : COMMA ID VARS_P
    | COLON TYPE SEMICOLON
    | COLON TYPE SEMICOLON VARS_P
  """
# 
def p_TYPE(p):
  """
  TYPE : INT_TYPE
    | FLOAT_TYPE
  """
# 
def p_BLOQUE(p):
  """
  BLOQUE : LEFT_BRACE RIGHT_BRACE
    | LEFT_BRACE ESTATUTO BLOQUE_P
  """
def p_BLOQUE_P(p):
  """
  BLOQUE_P : ESTATUTO BLOQUE_P
    | RIGHT_BRACE
  """
# 
def p_ESTATUTO(p):
  """
  ESTATUTO : ASIGNACION
    | CONDICION
    | ESCRITURA
  """
# 
def p_ASIGNACION(p):
  """
  ASIGNACION : ID EQUALS EXPRESION SEMICOLON
  """
# 
def p_ESCRITURA(p):
  """
  ESCRITURA : PRINT LEFT_PARENTHESIS EXPRESION ESCRITURA_P
    | PRINT LEFT_PARENTHESIS STRING ESCRITURA_P
  """
def p_ESCRITURA_P(p):
  """
  ESCRITURA_P : COMMA EXPRESION ESCRITURA_P
    | COMMA STRING ESCRITURA_P
    | RIGHT_PARENTHESIS SEMICOLON
  """
# 
def p_EXPRESION(p):
  """
  EXPRESION : EXP EXPRESION_P
  """
def p_EXPRESION_P(p):
  """
  EXPRESION_P : GREATER_THAN EXP
    | LESS_THAN EXP
    | NOT_EQUAL EXP
    | EMPTY
  """
# 
def p_CONDICION(p):
  """
  CONDICION : IF LEFT_PARENTHESIS EXPRESION RIGHT_PARENTHESIS BLOQUE CONDICION_P
  """
def p_CONDICION_P(p):
  """
  CONDICION_P : ELSE BLOQUE SEMICOLON
    | SEMICOLON
  """
# 
def p_EXP(p):
  """
  EXP : TERMINO EXP_P
  """
def p_EXP_P(p):
  """
  EXP_P : PLUS TERMINO EXP_P
    | MINUS TERMINO EXP_P
    | EMPTY
  """
# 
def p_TERMINO(p):
  """
  TERMINO : FACTOR TERMINO_P
  """
def p_TERMINO_P(p):
  """
  TERMINO_P : MULTIPLY FACTOR TERMINO_P
    | DIVIDE FACTOR TERMINO_P
    | EMPTY
  """
# 
def p_FACTOR(p):
  """
  FACTOR : LEFT_PARENTHESIS EXPRESION RIGHT_PARENTHESIS
    | VARCTE
    | MINUS VARCTE
    | PLUS VARCTE
  """
# 
def p_VARCTE(p):
  """
  VARCTE : ID
    | INT
    | FLOAT
  """
# Empty
def p_EMPTY(p):
  "EMPTY :"
  pass
# ERROR
def p_error(p):
  if p:
      print("Syntax error at '%s'" % p.value)
  else:
      print("Syntax error at EOF")

import ply.yacc as yacc
yacc.yacc()

while 1:
    try:
        s = raw_input('>>> ')
    except EOFError:
        break
    if not s:
        continue
    yacc.parse(s)