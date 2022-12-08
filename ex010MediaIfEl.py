print('='*3,'\033[34mUSANDO IF e ELSE\033[m', '='*3)
print('')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua \033[36mMÉDIA\033[m foi: {:.1f} '.format(m))
if m >= 7.0:
    print('Sua média foi boa! \033[4;34mPARABÉNS.\033[m')
else:
    print('Sua média foi ruim! \033[4;31mESTUDE MAIS.\033[m')



