print('====== \033[34mSOMANDO OS NÚMEROS DIGITADOS PELO USUÁRIO\033[m ======')
# 'int' refere-se aos números inteiros.
# 'print'sintaxe para escrever na tela.
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número? '))
s = (n1 + n2)
print('')
print('A \033[36mSOMA\033[m dos números digitados foram:', '\033[34m',s,'\033[34m')
# 'print' também pode ser escrito da seguinte forma:
# "print('A soma dos números digitados foram{}' .format (s))

