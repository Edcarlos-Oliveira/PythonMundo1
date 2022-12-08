print('='*6, 'Ordem de Apresentação', '='*6)
print('')
import random
a1 = str(input('Nome do Aluno 1: '))
a2 = str(input('Nome do Aluno 2 '))
a3 = str(input('Nome do Aluno 3 '))
a4 = str(input('Nome do Aluno 4: '))
lista = [a1, a2, a3, a4]
random.shuffle(lista) # Utiliza 'random.shuffle' para embaralhar os nomes digitados.
print('A ordem de apresentação do trabalho será: \n {} '.format(lista))




