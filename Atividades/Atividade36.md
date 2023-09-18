# Atividades do Módulo 4 - QA NA PRÁTICA 📚

Esse [repositório](https://github.com/LeanDevLima/Squad02_M4) é dedicado às atividades realizadas durante o Módulo 4 - M4 - LÓGICA DE PROGRAMAÇÃO COM PYTHON do curso de Quality Assurance oferecido pelo [**Instituto JogaJunto**](https://www.jogajuntoinstituto.org/). 

## 🚀 Descrição da 36ª Atividade: 🌟
<br>

🔍 EM SQUADs Crie um script com: 
- Uma função para criar personas, contendo nome, cidade, idade; 
- Salve os dados dessas personas em um arquivo CSV na pasta Atividades com o nome atividade36.csv;
- Suba todos os arquivos para seu repositório.

```python
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


```

Nessa atividade considerei criar um número de 25 pessoas e salvar os dados criados no arquivo Atividades\atividade36.csv.

O arquivo correspondente a essa atividade está no seguinte local: Atividades\Atividade36.py.

## Integrantes da Squad:

| Beatriz Souza  | [Bruno Soares](https://www.linkedin.com/in/bruno-soaresdev/)  | [Leanderson Lima](https://www.linkedin.com/in/leanderson-dias-de-lima/) | [Rebeca Borges](https://www.linkedin.com/in/rebecaborgess/) | Sara Cruz | 