print('='*6, 'Parte Inteira Número', '='*6)
print('')
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
h = (co ** 2) + (ca ** 2)
from math import sqrt
print('O comprimento da hipotenusa é: {:.2f}'.format(sqrt(h)))
print('')
# No exemplo abaixo pode ser feito dessa outra forma:
# h = (co ** 2 + ca ** 2) ** (1/2)
# Pode também usar a formula (math.hypot(co, ca) com a biblioteca 'import math' ou somente com 'from math import hypot'.











