print('='*6, 'AUMENTO DE SÁLARIO', '='*6)
print('')
s = float(input('Qual seu sálario atual? R$ '))
ns = s + (s * 15/100)
print('Considerando o sálario atual de R${:.2f}, seu novo sálario com 15% de aumento é: R${:.2f} '.format(s, ns))





