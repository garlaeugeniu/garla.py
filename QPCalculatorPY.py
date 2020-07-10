

# from colorama import Fore, Back, Style

op = input('Operatia ?  (+ , - , *, /, **, % ): ')
a =  float(input('a : '))
b =  float(input('b : '))
if op == '+':
    c = a+b
    print(' result = :' + ' ' + ' ' + str(c))
elif op == '-':
    c = a-b
    print(' result = :' + ' ' + ' ' + str(c))
elif op == '*':
    c = a*b
    print(' result = :' + ' ' + ' ' + str(c))
elif op == '/':
    c = a/b
    print(' result = :' + ' ' + ' ' + str(c))
elif op == '**':
    c = a**b
    print(' result = :' + ' ' + ' ' + str(c))
elif op == '%':
    c = a%b
    print(' result = :' + ' ' + ' ' + str(c))
else :
    print('operatie indescifrabila')