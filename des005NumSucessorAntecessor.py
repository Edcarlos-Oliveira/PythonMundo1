print('=' * 6, 'NÚMERO INTEIRO COM SUCESSOR E ANTECESSOR', '=' * 6)
n = int(input('Digite um número: '))
su = n + 1
an = n - 1
print('O sucessor de {} é: {} '.format(n, su))
print('O antecessor de {} é: {} '.format(n, an))

# Caso não necessite das variáveis, pode ser reescrito da seguinte maneira:
print('')
nb = int(input('Digite outro número: '))
print('Analizando nesse segundo exemplo, o valor {}, seu antecessor é {} e o sucessor é {}'.format(nb, (nb - 1),(nb + 1)))

