print('=' * 6, 'DOBRO, TRIPLO E RAIZ QUADRADADA', '=' * 6)
print('')
n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1 / 2)  # Para achar a raiz quadrada, pode ser usado tbm 'pow(n,(1/2), para a cúbica usa (1/3)
print('O dobro de {} é {}. '.format(n, d))
print('O triplo de {} é: {}. '.format(n, t))
print('A raiz quadrada de {} é: {:.2f}. '.format(n, r))



