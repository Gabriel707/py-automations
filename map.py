from operator import itemgetter

# numeros = []
# for i in range(5):
#     numeros.append(i)
# print(numeros)

# # Map function

# nomes = ['Larissa', 'Rafael', 'Marcos', 'John']


# def aprovar_pessoa(nome):
#     return nome + ' APROVADO'


# print(list(map(aprovar_pessoa, nomes)))

pinturas = [
    ['Pintura Classica', 'Azul', 1857],
    ['Pintura Medieval', 'Vermelha', 1867],
    ['Pintura Moderna', 'Verde', 1897]
]

cores = []
for cor in pinturas:
    cores.append(cor[1])
print(cores)
