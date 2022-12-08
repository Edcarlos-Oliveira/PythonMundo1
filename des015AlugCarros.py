print('=' * 6, 'ALUGUEL DE CARROS', '=' * 6)
print('')
d = int(input('Quantos dias alugado? '))
km = float(input('Quantos Km rodados? '))
cd = 60 * d  # Custo por dia
ck = 0.15 * km  # Custo por Km
tp = cd + ck  # Total a pagar
print('O total a pagar é de R$ {:.2f} '.format(tp))
