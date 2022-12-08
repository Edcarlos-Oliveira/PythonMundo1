print('='*6, 'ANO BISSEXTO', '='*6)
print('')
from datetime import date # Biblioteca para capturar o ano atual do sistema.
a = int(input("Qual ano quer analisar? Ou digite 0 para o ano atual: "))
# Se o ano for divisível por 4 e tiver resto igual 0,
# ou divisível por 100 tiver resto diferente de 0,
# ou divisível por 400 tiver resto igual a 0.
if a == 0:
    a = date.today().year # Para capturar o ano atual com o usuário digitando 0.
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('O Ano {} é BISSEXTO.'.format(a))
else:
    print('O Ano {} NÃO é BISSEXTO.'.format(a))



