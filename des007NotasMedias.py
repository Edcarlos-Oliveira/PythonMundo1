print('='*6, 'Notas e Médias', '='*6)
print('')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print('A média entre {} e {} é igual a: {} '.format(n1, n2, m))

# Nesse caso abaixo com a escolha dos números de dígitos ':.1f' ocorre o arredondamento.
print('')
print('A média entre {:.1f} e {:.1f} é igual a: {:.1f} '.format(n1, n2, m))





