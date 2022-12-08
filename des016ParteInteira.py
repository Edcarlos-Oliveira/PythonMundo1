print('='*6, 'Parte Inteira Número', '='*6)
print('')
n = float(input('Digite um número qualquer: '))
from math import trunc # Biblioteca utilizada para escrever apenas a parte inteira do número digitado.
print('O número {} tem  a parte Inteira: {} '.format(n, trunc(n)))
print('')
# Nesse caso abaixo também mostra somente a parte inteira do número sem precisar do 'trunc'
print('O número {} tem a parte Inteira: {} '.format(n,int(n)))








