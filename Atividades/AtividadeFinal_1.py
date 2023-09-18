import requests
import json
import pandas as pd
from faker import Faker

base_url = 'http://apilivro.jogajuntoinstituto.org/api/'

def post_request(endpoint, data):
    response = requests.post(base_url + endpoint, json=data)
    if response.status_code == 201:
        print(f"Requisição POST para '{endpoint}' realizada com sucesso!")
        return response.json()
    else:
        print(f"Erro ao fazer a requisição POST para '{endpoint}'.")
        return None

faker = Faker()

autor_data = {"name": "Leanderson"}
autor_cadastrado = post_request('authors', autor_data)

genero_data = {"name": "Squad2", "squad": "Squad2"}
genero_cadastrado = post_request('genders', genero_data)

livros_data = []
for _ in range(4):
    livro_data = {
        "title": faker.catch_phrase(),
        "description": faker.paragraph(),
        "author": autor_cadastrado['id'],
        "gender": genero_cadastrado['id']
    }
    livro_cadastrado = post_request('books', livro_data)
    livros_data.append(livro_cadastrado)

response = requests.get(base_url + 'books')
if response.status_code == 200:
    livros_cadastrados = response.json()
    print("\nLivros cadastrados:")
    for livro in livros_cadastrados:
        print(f"Título: {livro['title']}, Descrição: {livro['description']}, Autor ID: {livro['author']}, Gênero ID: {livro['gender']}")
else:
    print("Erro ao buscar livros cadastrados.")

df = pd.DataFrame(livros_data)
print("\nDataFrame com os livros cadastrados:")
print(df)
