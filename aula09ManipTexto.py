print('='*6, 'Manipulando Textos', '='*6)
print('')
frase = 'Curso em Video Python.'
print('Mostrando a 4ª letra: ', frase[3]) # Nesse caso mostra a 4ª letra.
print('Mostrando da 4 até a 12ª letra: ',frase[3:13]) # mostra até a 12ª letra.
print('Mostrando do inicio até a 12ª letra: ', frase[:13]) # mostra apartir do ínicio.
print('Mostrando do final até a 13ª letra: ', frase[13:]) # mostra do final até a 13ª
print('Mostra da letra até a 15, pulando de 2 em 2: ', frase[1:15:2]) # Mostra com salto de 2 em 2 entre a 1 e 15.
print('Conta quantas letras tem na string: ', len(frase)) # Conta também os espaços.
print('Joga a frase para maiusculas e conta as letras selecionadas: ', frase.upper().count('O'))
print('Mostra o len com os espaços eliminados:  ', len(frase.strip())) # 'Strip' para eliminar os espaços.
print('Utlizando replace para trocar nomes: ', frase.replace('Python', 'Android')) # trocar as strings.
print('Mostra se a palavra está na frase: ', 'Curso' in frase) # Verifica se determinada palavra está na frase, não mostra a posição.
print('Mostra a posição da palavra na frase: ', frase.find('Video')) # Mostra a posição da palavra.
print('Mostra a lista das palavras splitadas: ', frase.split()) # Mostra em forma de lista, separadas.
print('Coloca a primeira letra em maiúsculas e as demais em minúsculas: ', frase.capitalize()) # Primeira letra maiuscula e demais minusculas
print('Analisa quantas palavras tem: ', frase.title()) # coloca as primeiras letras depois do espaço em maiusculas
print('Mostra os separador nas frase: ', '-'.join(frase.split())) # Junta a frase com separadores.

# As 3 aspas pode ser usada para transformar textos longos em str







