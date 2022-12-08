print('='*6, 'Verificando Letras', '='*6)
print('')
cid = str(input('Em qual cidade você nasceu? ')).strip()
# No exemplo abaixo o que for digitado pelo usuário e não começar com 'SANTO' será 'false'.
print('Sua cidade não começa com SANTO: {}'.format(cid[:5].upper() == 'SANTO'))









