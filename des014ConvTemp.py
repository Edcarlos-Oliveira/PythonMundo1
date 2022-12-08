print('=' * 6, 'CONVERSOR TEMPERATURA', '=' * 6)
print('')
c = float(input('Digite a temperatura em ºC: '))
f = c * 1.8 + 32  # Pode ser usada a formula '((9 * c) /5)+32
print('A temperatura de {} ºC , equivale a {} ºF '.format(c, f))
# Para converter de Fahrenheit para Celsius, utiliza a sintaxe c = (f -32)/1.8
print('')
fa = float(input('Digite a temperatura em ºF: '))
ca = (fa - 32) / 1.8
print('A temperatura de {} ºF, equivale a {} ºC '.format(fa, ca))
