def gerar_nome_completo(nome, sobrenome):
    print(f'Seja bem vindo {nome} {sobrenome}')

gerar_nome_completo('Gabriel', 'Araujo')

def calcular_valores(preco_produto, qtd_produto=1):
    print(f'Preço do produto é R${preco_produto}\nQuantidade de produto R${qtd_produto}\n')
    print(f'Valor a pagar: R${preco_produto * qtd_produto}')

calcular_valores(10, 3)

print('#' * 20)

def objeto_personalizado(cor, altura='10cm', formato='triangular'):
    print(f'Detalhes do objeto: {cor} | {altura} | {formato}')

objeto_personalizado('preto')