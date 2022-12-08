print('='*6, 'Separando Números', '='*6)
print('')
n = int(input('Informe um número: '))
un = n // 1 % 10 # divisão inteira e resto da divisão para mostrar a unidade.
dz = n // 10 % 10
cen = n // 100 % 10
mi = n // 1000 % 10
print('O número digitado foi: {} '.format(n))
print('Unidade: {}'.format(un))
print('Dezena: {}'.format(dz))
print('Centena: {}'.format(cen))
print('Milhar: {}'.format(mi))












