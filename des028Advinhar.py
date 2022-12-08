print('-=-'*20)
print('| Vou pensar em um número entre 0 e 5. Tente adivinhar.... |')
print('-=-'*20)
from random import randint
from time import sleep
n = int(input('Qual número estou pensando? '))
nu = randint(0,5)
print('\033[33mProcessando....\033[m')
sleep(3)
print('O número que pensei foi: {}'.format(nu))
if nu == n:
    print('\033[36mParabéns, você ACERTOU!\033[m')
else:
    print('\033[31mVocê ERROU, tente novamente.\033[m')




