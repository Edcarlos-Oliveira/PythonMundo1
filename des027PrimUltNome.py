print('='*6, 'Primeiro e último nome', '='*6)
print('')
nome = str(input('Digite seu nome completo: ')).strip()
n = nome.split()
print('Prazer em te conhecer!')
print('Seu primeiro nome é: {}'.format(n[0]))
print('Seu último nome é: {}'.format(n[len(n) - 1])) # Para achar o último nome digitado.








