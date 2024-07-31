from itertools import zip_longest

# CHALLENGE

produtos = ['produto 1', 'produto 2', 'produto 3', 'produto 4', 'produto 5']
precos = ['R$500,00', 'R$1500,00', 'R$2700,00', 'R$5000,00']

for produto, preco in zip_longest(produtos,precos):
    print(f"Produto: {produto.title()} encontrado no valor de {preco}")

# '''
# append()
# extends()
# pop()
# remove()
# clear()
# '''

# a_list =['A', 'B', 'C', 'D', 'E']
# b_list = [1, 2, 3, 4, 6]

# for a,b in zip(a_list, b_list):
#     print(a)
#     print(b)


# for a,b in zip(produtos, precos):
#     print(f"Salvando produto {a} valor R${b}")

# titulos = ['Titulo 1', 'Titulo 2', 'Titulo 3', 'Titulo 4']
# descricoes = ['Descricao 1', 'Descricao 2', 'Descricao 3']
# for titulo,descricao in zip_longest(titulos,descricoes):
#     print(f"Escontramos o {titulo} com descricao: {descricao}")