'''num = float(input('Digite o valor do cateto oposto: '))
num2 = float(input('Digite o valor do cateto adjacente: '))
hipo = (num ** 2 + num2 ** 2) ** (1/2)

print('A hipotenusa é {:.2f}'.format(hipo))'''
from math import hypot

num = float(input('Digite o valor do cateto oposto: '))
num2 = float(input('Digite o valor do cateto adjacente: '))
hipo = hypot(num, num2)
print('A hipotenusa é {:.2f}'.format(hipo))