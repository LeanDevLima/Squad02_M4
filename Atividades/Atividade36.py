import sys
import os

root_dir = os.path.dirname(os.path.abspath(__file__))  
project_dir = os.path.join(root_dir, '..') 
sys.path.append(project_dir)  

import random
import csv
from faker import Faker

def criar_persona():
    faker = Faker()
    nome = faker.name()
    idade = random.randint(18, 65)

    cidade = faker.city()

    return {'Nome': nome, 'Idade': idade, 'Cidade': cidade}

def salvar_personas_em_csv(numero_de_personas):
    personas = [criar_persona() for _ in range(numero_de_personas)]

    arquivo_csv = 'Atividades/atividade36.csv'

    with open(arquivo_csv, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Nome', 'Idade', 'Cidade'])
        
        writer.writeheader()
        
        for persona in personas:
            writer.writerow(persona)

    print(f"{numero_de_personas} personas foram salvas no arquivo CSV: {arquivo_csv}")

numero_de_personas = 25 
salvar_personas_em_csv(numero_de_personas)
