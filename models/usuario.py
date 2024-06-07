import datetime
import random


class Usuario:

    usuarios = []

    def __init__(self, nome, sobrenome, idade):
        self._nome = nome.title()
        self._sobrenome = sobrenome.title()
        self._idade = idade
        self._creation_date = self.register_datetime()
        self._coupon = self.assign_coupon()
        Usuario.usuarios.append(self)

    def register_datetime(self):
        return datetime.datetime.now()

    def assign_coupon(self):
        coupons = ['$50.00', '$250.00', '$120.00']
        return random.choice(coupons)

    def __str__(self):
        return f"Olá: {self._nome} {self._sobrenome}, Idade: {self._idade}, seu registro foi concluído com sucesso no dia: {self._creation_date}, Parabéns, houve um sorteio e você ganhou um cartão de compras no valor de: {self._coupon}"
