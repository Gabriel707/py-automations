import os

# with open('celulares.txt', 'w') as arquivo:
#     arquivo.write('Celular 1')

# nomes = ['Lucas', 'Carol', 'Julio', 'Gabriella', 'Naluda']
# numeros = [1, 2, 3, 4, 5, 6]
# with open('nomes.txt', 'a', newline='') as arquivo:
#     for nome in nomes:
#         arquivo.write(nome + os.linesep)

with open('nomes.txt', 'r') as arquivo:
    for linha in arquivo:
        print(linha)
