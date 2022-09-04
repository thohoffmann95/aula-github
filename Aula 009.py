#frase = str(input('Opa Bão?'))
#len(frase)
#frase.count('o')
#frase.find('deo')
#'Opa' in frase


#Transformação
#frase.replace('Opa','Fala')
#frase.upper()
#OPA BÃO?
#frase.lower()
#opa bão?
#frase.capitalize()
#Opa bão? Primeira letra em maisculo e resto em minusculo
#frase.title()
#Opa Bão? Quebra de palavras para iniciarem maiusculas
#frase.strip()
#Remove todos os espaços inuteis
#frase.rstrip()
#Remove somente os espaços na direita
#frase.lstrip()
#Remove os espaços da esquerda'''


#Divisão
#frase.split()
#Cada palavra recebe indexação nova, divide em listas
#'-'.join(frase)
#Junta a indexação'''

frase = 'Curso em Vídeo Python'
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[1:15:2])
print('''Vamos criar um app de consulta de vendas, no qual você poderá buscar vendas em um dado intervalo de datas, 
e poderá notificar via SMS os dados dos melhores vendedores. Vamos construir o back end com Java e Spring, e o front 
end com React. Veja calendário abaixo.''')
print(frase.count('o'))
print(frase.upper().count('o'))
print(frase.replace('Python', 'Putaria'))