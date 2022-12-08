print('='*6, 'Analisando Textos', '='*6)
print('')
nome = str(input('Digite seu nome completo: ')).strip() # '.strip ' Para eliminar os espaços antes e depois dos dados digitados.
pn = (nome.split()) # Primeiro nome.
print('O nome digitado foi: {} '.format(nome))
print('O nome com as letras MAIÚSCULAS é: {} '.format(nome.upper()))
print('O nome com as letras MINÚSCULAS é: {} '.format(nome.lower()))
print('A quantidade de letras SEM espaços é: {} '.format(len(nome) - nome.count(' ')))
print('A quantidade de letras COM espaços é: {} ' .format(len(nome)))
print('O primeiro nome é: ( {} ) e ele tem {} letras.'.format(pn[0], len(pn[0])))



















































