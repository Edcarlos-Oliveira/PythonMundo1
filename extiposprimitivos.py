print('='*6,'\033[34mTIPOS PRIMITIVOS\033[m', '='*6)
print('')
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
# print('A soma de', n1, '+', n2, 'é:', s) formato antigo
# #Pode ser reescrito da seguinte forma no formato novo.
print('A \033[36mSOMA\033[m de {} + {} é: {}'.format(n1, n2, s))


