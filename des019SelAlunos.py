print('='*6, 'Seleção Alunos', '='*6)
print('')
a1 = str(input('Nome do Aluno 1: '))
a2 = str(input('Nome do Aluno 2 '))
a3 = str(input('Nome do Aluno 3 '))
a4 = str(input('Nome do Aluno 4: '))
lista = [a1, a2, a3, a4] # Listas são criadas entre colchetes.
import random
esc = random.choice(lista) # Utliza 'random.choice' para escolher um item da lista.
print("Entre os alunos, o sorteado foi o: {} ".format(esc))















