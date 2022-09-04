dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos km rodados? '))
pagar = dias * 60 + km * 0.15
print('O valor a pagar é {:.2f}'.format(pagar))