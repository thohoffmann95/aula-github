salario = float(input('Qual o valor do salario do funcionário? R$'))
aumento = salario + (salario * 15 / 100)
print('O funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salario, aumento))