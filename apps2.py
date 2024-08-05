import json

computador_json = """{
 "marca": "Dell",
 "preço": 15000
}"""

data = json.loads(computador_json)
print(data["preço"])
with open('computador.json', 'w', encoding="utf-8") as arquivo_json:
    json.dump(computador_json, arquivo_json)

with open('computador.json', encoding="utf-8") as arquivo_json:
    string_computador_json = json.load(arquivo_json)
    dicionario_computador_json = json.loads(string_computador_json)
    print(dicionario_computador_json["marca"])
