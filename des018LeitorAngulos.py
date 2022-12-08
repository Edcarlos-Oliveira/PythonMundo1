print('='*6, 'Leitor Ângulos', '='*6)
print('')
import math
a = float(input('Digite o valor do ângulo: '))
sen = math.sin(math.radians(a)) # 'math.sin' calcula o seno, 'math.radians' converte o valor em radianos.
cos = math.cos(math.radians(a)) # 'math.cos' calcula o cosseno.
tan = math.tan(math.radians(a)) # 'math.tan' calcula a tangente
print('O ângulo de {:.0f}º tem o SENO de {:.2f} '.format(a, sen))
print('O ângulo de {:.0f}º tem o COSSENO de {:.2f} '.format(a, cos))
print('O ângulo de {:.0f}º tem a TANGENTE de {:.2f} '.format(a, tan))







