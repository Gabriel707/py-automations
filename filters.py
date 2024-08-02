# nomes = ['Larissa', 'rafael', 'marcus', 'john']


# def pessoa_aprovada(pessoa):
#     if pessoa == 'marcus':
#         return True
#     else:
#         return False


# print(list(filter(pessoa_aprovada, nomes)))
# print(list(map(pessoa_aprovada, nomes)))

# pinturas = [
#     ['Pintura Classica', 'Azul', 1857],
#     ['Pintura Medieval', 'Vermelha', 1867],
#     ['Pintura Moderna', 'Verde', 1897]
# ]


# def is_antique(pintura):
#     if pintura[2] < 1890:
#         return True
#     else:
#         return False


# print(list(filter(is_antique, pinturas)))

'''
Usando a lista abaixo, filtre apenas as vagas com salário acima de R$2500
'''

vagas = [
    ['vaga 1', 1200],
    ['vaga 2', 2550],
    ['vaga 3', 5000]
]


def acima_de_2500(salario):
    if salario[1] > 2500:
        return True
    else:
        return False


print(list(filter(acima_de_2500, vagas)))
