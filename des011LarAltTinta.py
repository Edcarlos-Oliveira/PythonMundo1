print('='*6, 'CALCULAR QUANTIDADE TINTA PARA PINTAR UMA PAREDE', '='*6)
print('')
l = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
ar = l * alt
t = ar/2
print('A área total da parede é: {:.2f} m², você vai precisar de: {:.1f} litros de tinta.  '.format(ar, t))
print('')
print('*** Sabendo que cada litro de tinta faz 2m².')







