print('='*6, 'TRIÂNGULO', '='*6)
print('')
l1 = float(input('Digite o valor do primeiro lado: '))
l2 = float(input('Digite o valor do segundo lado: '))
l3 = float(input('Digite o valor do terceiro lado '))

if l1 < l2 +l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os valores digitados \033[36mFORMAM um TRIÂNGULO.\033[m')
else:
    print('Os valores digitados \033[31mNÃO FORMAM um TRIÂNGULO.\033[m')


# Pode ser escrito com a seguinte fórmula:
# 'if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 +l2:'


