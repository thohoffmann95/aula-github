produto = float(input('Digite o preço do produto R$'))
novo = produto - (produto * 5 / 100)
print('O valor do produto que custava {}, na promoção de 5% de desconto vai custar R${}'.format(produto, novo))