frase = 'olá, bem-vindo a este treinamento'
print(frase.split())
print(frase.split(','))
print(frase.split('-'))
nomes = 'joao, rafael, gabriel, carol, amanda, jefferson'
print(nomes.split())
print(nomes.split(','))
hashtags = 'music #guitar #gamer #artist #coder #python'
print(hashtags.split())
print(hashtags.split('#'))
print(hashtags.split('#', 3))

hashtags_separadas_por_espaco = hashtags.split(' ')
print(hashtags_separadas_por_espaco)
print(','.join(hashtags_separadas_por_espaco))
print('.'.join(hashtags_separadas_por_espaco))
print(' '.join(hashtags_separadas_por_espaco))

frase1 = 'Desafio manipulacao de strings'
frase2 = 'jhonathan,rafael,carol,camilla'

palavras1 = frase1.split()
print(palavras1)

palavras2 = frase2.split(',')
print(palavras2)

desafio3 = ','.join(palavras1)
print(desafio3)

desafio4 = ' & '.join(palavras2)
print(desafio4)
