# numeros = [2, 2, 5, 8]
# frutas = ['maça', 'uva', 'banana', 'maça', 'morango']

# set_numeros = set(numeros)
# set_frutas = set(frutas)

# print(set_numeros)
# print(set_frutas)

# set_numeros.add(10)
# print(set_numeros)

numeros1 = [2, 2, 5, 8]
numeros2 = [2, 2, 3, 9]
a = set(numeros1)
b = set(numeros2)
c = a.symmetric_difference(b)  # Diferença dos sets
print(a.intersection(b))  # encontra valores em comum entre sets
print(a.union(b))  # Remove as duplicadas e une os conjuntos
