from models.usuario import Usuario
from carro import ligar_carro
from moto import ligar_moto
from banco_de_dados import buscar_usuarios


ligar_moto()
ligar_carro()
buscar_usuarios()

cliente_1 = Usuario('Gabriel', 'santana', 29)
usuario1 = Usuario("joao", "silva", 30)
usuario2 = Usuario("maria", "oliveira", 25)

print(cliente_1)
print(usuario1)
print(usuario2)


'''
5. Guarde informações sobre a data de aniversário do funcionário(dd/mm/aaaa)
'''
