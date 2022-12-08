print('='*6, 'TRIÂNGULO', '='*6)
print('')
l1 = float(input('Digite o valor do primeiro lado: '))
l2 = float(input('Digite o valor do segundo lado: '))
l3 = float(input('Digite o valor do terceiro lado '))

t = (l1 + l2)

if t > l3:
    print('Os valores digitados FORMAM um TRIÂNGULO.')
else:
    print('Os valores digitados NÃO FORMAM um TRIÂNGULO.')

# Pode ser escrito com a seguinte fórmula:
# 'if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 +l2:'


