# '**' utilizado para potenciação
# '//' utilizado para divisão inteira, exemplo 5//2 = 2, o número q fica abaixo do divisor.
# '%' utilizado para pegar o resto da divisão, no caso acima o "1"
# Ordem de Precedência dos operadores (1º (), 2º **, 3º *, /, //, %, 4º +, -)
# Para juntar dois 'print' na mesma linha utiliza ' end='' ' no final do print
# Para quebrar a linha utiliza ' \n '
print('====== \033[34mOPERADORES ARITIMÉTICOS e INSTRUÇÕES\033[m ======')
print('')
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor´: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A \033[36mSOMA\033[m é: {} '.format(s))
print('O \033[36mPRODUTO\033[m é: {} '.format(m))
print('A \033[36mDIVISÃO\033[m é: {:.2f} '.format(d))  # Utiliza ':.2f' para escrever o número com 2 casas decimais.
print('A \033[36mDIVISÃO INTEIRA\033[m é: {} '.format(di))
print('A \033[36mPOTÊNCIA\033[m é: {} '.format(e))
print('')
print('Testando a escrita sem quebra utilizando a \033[4;33msintaxe end=\033[m'' ', end=' ')
print('Esse texto foi do print abaixo')
print('')
print('Testando a quebra de linhas \n utilizando nesse texto a sintaxe \n ')

