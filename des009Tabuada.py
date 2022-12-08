print('=' * 6, 'TABUADA DO NÚMERO DIGITADO', '=' * 6)
print('')
n = int(input('Quer ver a tabuada de qual número? '))
c = 1

while c <= 10:
    r = n * c
    print('A tabuada de {} x {} = {} '.format(n, c, r))
    c = c + 1
