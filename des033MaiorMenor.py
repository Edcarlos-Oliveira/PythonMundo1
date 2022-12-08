print('='*6, 'MAIOR E MENOR', '='*6)
print('')
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número '))
n3 = int(input('Digite o terceiro número '))
print('')
# Verificando o MENOR valor:
me = n1
if n2 < n1 and n2 < n3:
    me = n2
if n3 < n1 and n3 < n2:
    me = n3
# Verificando o MAIOR valor:
ma = n1
if n2 > n1 and n2 > n3:
    ma = n2
if n3 > n1 and n3 > n2:
    ma = n3
print('O MENOR valor digitado foi {}.'.format(me))
print('O MAIOR valor digitado foi {}.'.format(ma))




































