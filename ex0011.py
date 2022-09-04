largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
dimensao = largura * altura
tinta = dimensao / 2
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(largura, altura, dimensao))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))
