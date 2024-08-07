import os

# with open('celulares.txt', 'w') as arquivo:
#     arquivo.write('Celular 1')

nomes = ['Lucas', 'Carol', 'Julio', 'Gabriella', 'Naluda']

with open('nomes.txt', 'a', newline='') as arquivo:
    for nome in nomes:
        arquivo.write(nome + os.linesep)
