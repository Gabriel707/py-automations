import datetime


class Usuario():

    usuarios = []

    def __init__(self, nome, sobrenome, idade):
        self._nome = nome.title()
        self._sobrenome = sobrenome.title()
        self._idade = idade
        Usuario.usuarios.append(self)

    ''''
    Function to register a datetime of everyuser    
    '''
