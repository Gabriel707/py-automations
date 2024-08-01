# Enumerate
# for indice, numero in enumerate(range(1, 11), 1):
#     print(indice, numero)
#     if indice == 5:
#         print('Estamos na metade da lista')

# nomes = ['nome1', 'nome2', 'nome3', 'nome4']

# for nome in enumerate(nomes):
#     print(nome)

frutas = ['Maça', 'Laranja', 'Morango', 'Limão']

for indice, fruta in enumerate(frutas, 0):
    if indice == 3:
        print(f"{indice} {fruta} EM PROMOÇÃO")
    else:
        print(indice, fruta)
