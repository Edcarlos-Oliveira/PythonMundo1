print('='*6, 'VELOCIDADE', '='*6)
print('')
v = float(input('Qual a sua velocidade? '))
km = (v - 80) * 7

if v > 80:
    print('Você ULTRAPASSOU a velocidade permitida de 80Km/h. \nE será MULTADO em: R${:.2f}'.format(km))
else:
    print('PARABÉNS, continue digirindo com segurança.')










