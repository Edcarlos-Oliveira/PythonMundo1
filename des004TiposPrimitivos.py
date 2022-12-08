print('======= TIPOS PRIMITIVOS ======')
d = input('Digite algo: ')  # Nesse caso 'd' é considerado como string.
print('O tipo primitivo desse valor é: ', type(d))  # Escreve o tipo do dado digitado
print('Só tem espaços? ', (d.isspace()))  # Escreve se foi digitados espaços
print('O dado digitado foi: ', d)  # Escreve o dado digitado
print('É um número? ', d.isnumeric())  # Escreve se o dado digitado é númerico ou não.
print('É alfabético? ', d.isalpha())  # Escreve se o dado digitado é letra
print('É alfanúmerico? ', d.isalnum())  # Escreve se o dado tem letras e números
print('Está em maiúsculo? ', d.isupper())  # Escreve se o dado digitado são com letras maiusculas
print('Está em minúsculo? ', d.islower())  # Escreve se o dado digitado são com letras minusculas
print('Está capitalizada? ', d.istitle())  # Escreve 'true' quando umas das letras está em maiúscula

print('')
d1 = float(input('Digite outro valor: '))  # Nesse caso é escrito números float ex'0.0'
print(type(d1))
print(d1)
# Nesse caso abaixo qualquer número digitado fica como 'true', pedindo para escrever (d2),
# caso não seja digitado nada fica como 'false'
print('')
d2 = bool(input('Digite novamente: '))
print(type(d2))
print(d2)
