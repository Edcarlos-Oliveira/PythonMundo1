print('=' * 6, '\033[34mUtilizando Modulos\033[m', '=' * 6)
print('')
num = int(input('Digite um número: '))
# 'from math import sqrt' importa só a biblioteca específica, nesse caso a 'sqrt' não usa 'math.sqrt'.
# biblioteca de todas as funções de matemática 'math'.
# 'ceil' arredonda o número para cima.
# 'floor' arredonda para baixo.
# 'trunc' elimina os digitos da virgula para frente sem arredondamento.
# 'pow' potencia, usado como os dois '**'.
# 'sqrt' para calcular a raiz quadrada.
# 'factorial' para calcular fatorial.
import math
raiz = math.sqrt(num)  # Mostra a raiz quadrada do número digitado utilizando 'sqrt'.
print('A \033[36mRAIZ\033[m de {} é igual a: {:.1f}'.format(num, raiz))
# Nesse caso abaixo mostra a raiz arredondada para cima com a utilização do 'ceil'.
print('Mostrando a raiz de {} \033[4;33m usando <ceil>:\033[m {}' .format(num, math.ceil(raiz)))
# Nesse caso abaixo o arredondamento ocorre para baixo, utlizando 'floor'.
print('Mostrando a raiz de {} \033[4;33m usando <floor>:\033[m {}'.format(num, math.floor(raiz)))
print('')
# Utilizando biblioteca 'random' gera números aleatórios.
import random
nu = random.randint(1, 10)  # Nesse caso escreve os números aleatórios entre 1 e 10 inteiros.
print('Número gerado pela \033[4;33m biblioteca random:\033[m {} '.format(nu))
print('')
# Utlizando biblioteca de emoji.
import emoji
print(emoji.emojize('Olá Mundo, \033[4;33m emoji em Python:\033[m \U0001f30e'))



































