# try:
#     valor = int(input('Digite um valor em dólares: '))
#     print(valor * 5.75)
# except:
#     print('Favor digite apenas numeros.')
try:
    meses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    print(meses[15])
except IndexError as erro:
    print('Favor acessar um indice válido de 0 a 11')
    print(erro)
