import requests
from pprint import pprint

# API Verbs - Get
resultado_get = requests.get('https://jsonplaceholder.typicode.com/todos')
# pprint(resultado_get.json())

# Get com ID
resultado_get_com_id = requests.get(
    'https://jsonplaceholder.typicode.com/todos/2')
pprint(resultado_get_com_id.json())

nova_tarefa = {'completed': False,
               'title': 'Lavar o carro',
               'userId': 1}
resultado_post = requests.post(
    'https://jsonplaceholder.typicode.com/todos', nova_tarefa)
pprint(resultado_post.json())

# PUT - Alterar um recurso existente
tarefa_alterada = {'complete': False,
                   'title': 'Lavar a moto',
                   'userId': 1}
resultado_put = requests.put(
    'https://jsonplaceholder.typicode.com/todos/2', tarefa_alterada)
pprint(resultado_put.json())

# DELETE API

resultado_delete = requests.delete(
    'https://jsonplaceholder.typicode.com/todos/2')
pprint(resultado_delete.json())
