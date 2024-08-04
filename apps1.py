import json

with open('usuarios1.json', encoding='utf-8') as arquivo_json:
    data = json.load(arquivo_json)
    print('[nome]')

with open('usuarios2.json', encoding='utf-8') as arquivo_json:
    data = json.load(arquivo_json)
    print(data["permissões"][1])

with open('usuarios3.json', encoding='utf-8') as arquivo_json:
    data = json.load(arquivo_json)
    print(data["usuários"][0]["telefone"])
    print(data["usuários"][1]["admin"])

with open('usuarios4.json', encoding="utf-8") as arquivo_json:
    data = json.load(arquivo_json)
    print(data["usuários"][0]["plano"]["preco"])

with open('usuarios5.json', encoding="utf-8") as arquivo_json:
    data = json.load(arquivo_json)
    print(data[0]["admin"])

with open('desafio.json', encoding="utf-8") as arquivo_json:
    data = json.load(arquivo_json)
    print(data["user"][1]["email"])
    print(data["user"][0]["address"]['city'])
    print(data["user"][1]["orders"][0]["total"])
