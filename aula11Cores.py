# STYLE [0 = NONE, 1 = BOLD, 4 = UNDERLINE, 7 = NEGATIVE ou INVERSÃO]
# Text [30 = bco, 31 = ver, 32 = vde, 33 = Amr, 34 = Azu, 35 = rox, 36 = azu claro, 37 = cza]
# background [40 = bco, 41 = ver, 42 = vde, 43 = amr, 44 = azu, 45 = rox, 46 = azu claro, 47 = cza]
# '\033[0;33;44m' Código para usar nas cores.
# Também pode ser usada uma variável cores:
# 'cores = {'limpa':'\033[m, 'azul':'\033[34m' etc
print('\033[30;43mOlá, Mundo!\033[m') # Nesse código a cor da letra bco, background amr e \033[m no final para limitar a cor ao texto
nome = 'Edcarlos'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m',
         'verde':'\033[32m'}

print('Olá, Muito prazer! {}{}{}'.format('\033[4;34m', nome, '\033[m'))
print('Testando a variável de cores, {}{}{}'.format(cores['verde'], nome, cores['limpa']))





