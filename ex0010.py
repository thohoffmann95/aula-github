real = float(input('Quanto de dinheiro você tem na carteira? R$'))
dolar = real / 5.07
euro = real / 5.05
dolarcana = real / 3.89
iene = real / 0.03
print('Com R${:.2f} você pode comprar U${:.2f}, C${:.2f}, JPY {:.2f}'.format(real, dolar, dolarcana, iene))
