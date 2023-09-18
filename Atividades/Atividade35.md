# Atividades do Módulo 4 - QA NA PRÁTICA 📚

Esse [repositório](https://github.com/LeanDevLima/Squad02_M4) é dedicado às atividades realizadas durante o Módulo 4 - M4 - LÓGICA DE PROGRAMAÇÃO COM PYTHON do curso de Quality Assurance oferecido pelo [**Instituto JogaJunto**](https://www.jogajuntoinstituto.org/). 

## 🚀 Descrição da 35ª Atividade: 🌟
<br>

🔍 Individualmente

Crie uma persona com a biblioteca Faker com nome, idade e cidade. Criando o atributo random.int para gerar valores aleatórios para idade.

- Para essa atividade limitei a idade para pessoas entre 15 e 65 anos.

```python

import sys
import os

root_dir = os.path.dirname(os.path.abspath(__file__))  
project_dir = os.path.join(root_dir, '..') 
sys.path.append(project_dir)  

import random
from faker import Faker

faker = Faker()

nome = faker.name()
idade = random.randint(15, 65)
cidade = faker.city()

print("Nome:", nome)
print("Idade:", idade)
print("Cidade:", cidade)


```

O arquivo correspondente a essa atividade está no seguinte local: Atividades\Atividade35.py.

## Integrantes da Squad:

| Beatriz Souza  | [Bruno Soares](https://www.linkedin.com/in/bruno-soaresdev/)  | [Leanderson Lima](https://www.linkedin.com/in/leanderson-dias-de-lima/) | [Rebeca Borges](https://www.linkedin.com/in/rebecaborgess/) | Sara Cruz | 