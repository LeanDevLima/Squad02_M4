import sys
import os

root_dir = os.path.dirname(os.path.abspath(__file__))  
project_dir = os.path.join(root_dir, '..') 
sys.path.append(project_dir)  

import requests
import json
import pandas as pd
from faker import Faker


base_url = 'http://apilivro.jogajuntoinstituto.org/api/'


def post_request(endpoint, data):
    response = requests.post(base_url + endpoint, json=data)
    if response.status_code == 201:
        return response.json()
    else:
        print(f"Erro ao fazer a requisição POST para '{endpoint}': {response.status_code}")
        return None


faker = Faker()


autor_id = 28  
genero_id = 14  


livros_data = []


for _ in range(4):
    livro_data = {
        "title": faker.catch_phrase(),
        "description": faker.paragraph(),
        "author": autor_id,
        "gender": genero_id
    }
    livro_cadastrado = post_request('books', livro_data)
    if livro_cadastrado:
        livros_data.append(livro_cadastrado)

if livros_data:
    df = pd.DataFrame(livros_data)
    print("\nDataFrame com os livros cadastrados:")
    print(df)
else:
    print("Não foi possível cadastrar os livros.")
