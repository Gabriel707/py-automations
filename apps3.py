import json

student_json = """{
 "name": "John Smith",
 "age": 30,
 "city": "New York",
 "isStudent": true,
 "gpa": 3.5 
}"""

data = json.loads(student_json)
print(data["name"])
with open('student_json', 'w', encoding="utf-8") as arquivo_json:
    json.dump(student_json, arquivo_json)

with open('student_json', encoding="utf-8") as arquivo_json:
    string_student_json = json.load(arquivo_json)
    dicionario_student_json = json.loads(string_student_json)
    print(dicionario_student_json["city"])
