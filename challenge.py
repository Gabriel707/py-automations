import os

frutas = ['morango', 'uva', 'maça', 'banana', 'abacate']
cores = ['Vermelho', 'verde', 'azul', 'branco', 'preto']
linguagens_prog = ['C++', 'java', 'python', 'go', 'javascript']

with open('frutas.txt', 'a', newline='') as arquivo:
    for fruta in frutas:
        arquivo.write(fruta + os.linesep)

with open('frutas.txt', 'r') as arquivo:
    for linha in arquivo:
        print(linha)

with open('frutas.txt', 'a', newline='') as arquivo:
    for cor in cores:
        arquivo.write(os.linesep + cor)

with open('top 5 linguagens.txt', 'w', newline='') as arquivo:
    for linguagem in linguagens_prog:
        arquivo.write(linguagem.title() + os.linesep)
