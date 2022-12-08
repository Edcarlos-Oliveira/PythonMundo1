print('='*6, 'PREÇO DA VIAGEM', '='*6)
print('')
d = float(input('Qual a distância de sua viagem? '))
km = d * 0.50
km2 = d * 0.45

if d <= 200:
    print('O preço de sua viagem é: R${:.2f}'.format(km))
else:
    print('O preço de sua viagem é: R${:.2f}'.format(km2))





