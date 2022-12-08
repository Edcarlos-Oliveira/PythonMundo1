print('='*6, 'REAJUSTE SALARIAL', '='*6)
print('')
s = float(input('Qual o valor do seu salário? '))
r10 = s + (s * 10/100)
r15 = s + (s * 15/100)

if s > 1250:
    print('Seu novo salário com 10% de aumento: R${:.2f}'.format(r10))
else:
    print('Seu novo salário com 15% de aumento: R${:.2f}'.format(r15))







