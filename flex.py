
import ply.lex as lex
import ply.yacc as yacc
import time


tokens = (
    'NAME', 'NUMBER',  'SEMICOLON', 'EQUALS', 'LPAREN', 'RPAREN', 'COMMA', 'SNAME', 'INCORRECT',
)

# Tokens


t_EQUALS = r'='
t_SEMICOLON = r';$'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r'\,'
t_SNAME = r'^[a-zA-Z][a-zA-Z0-9]{,20}'
t_NAME = r'[a-zA-Z][a-zA-Z0-9]{,20}'
t_NUMBER = r'[0-9]+'
t_INCORRECT = r'[^(a-zA-Z0-9=;\)\(\,)]'



# Ignored characters
t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    #print("Illegal character '%s'" % t.value[0])
    f.write(t.lexer.lexdata + ' is incorrect\n')
    t.lexer.skip(1)




lexer = lex.lex()




def p_statement_assign(t):
    '''statement : SNAME EQUALS NAME LPAREN endparameter RPAREN SEMICOLON
                 | SNAME EQUALS NAME LPAREN RPAREN SEMICOLON'''
    #print(t[3])
    f.write(t.lexer.lexdata + ' is correct\n')
    if d.get(t[3]) == None:
        d[t[3]] = 1
    else:
        d[t[3]] = d[t[3]] + 1

def p_statement_sparameter(t):
    '''simpleparameter : NAME COMMA
                       | NUMBER COMMA'''


def p_statement_parameter(t):
    '''parameter : simpleparameter
                 | parameter simpleparameter'''


def p_statement_eparameter(t):
    '''endparameter : parameter NUMBER
                    | parameter NAME
                    | NAME
                    | NUMBER'''



def p_error(t):
    #print("Syntax error at '%s'" % t.value)
    f.write(t.lexer.lexdata + ' is incorrect\n')







parser = yacc.yacc()


def inputt():
    try:
        k = int(input())
    except (TypeError, ValueError):
        print ("You entered incorrect data! Enter again!")
        k=inputt()
    return k


start_time = time.time()
f=open('result.txt', 'w')
print("Do you want to use file(1) or console(2)?")
n=inputt()
str=" "
d={}
if n==2:
    print("Enter new string or 0 to finish")
    str=input()
    while str != "0":
        parser.parse(str)
        print("Enter new string or 0 to finish")
        str = input()
elif n==1:
    start_time = time.time()
    try:
        file = open('C:/Users/user/PycharmProjects/generator/voc.txt', 'r')
    except IOError as e:
        print(u'file is not exist')
    else:
        while True:
            line = file.readline()
            if not line:
                break
            parser.parse(line)
        file.close()
        print("--- %s seconds ---" % (time.time() - start_time))
else:
    print("You entered incorrect number!")
a=0
b=0
with open('functions.txt','w') as i:
    for key,val in d.items():
        i.write('{}:{}\n'.format(key,val))
        a=a+val
        b=b+1
print(a," lines were correct")
print(b," functions were correct")
f.close()