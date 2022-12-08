print('='*6, 'Primeira e ultima Oc em uma String', '='*6)
print('')
fr = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(fr.count('A')))
print('A primeira letra A apareceu na posição: {}'.format(fr.find('A') + 1)) # Utiliza '+ 1', pois a contagem será sempre 1 a menos.
print('A última letra A apareceu na posição {}'.format(fr.rfind('A') + 1)) # 'rfind' procura a ultima letra do lado direito.

