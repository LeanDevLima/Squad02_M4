# Atividades do Módulo 4 - QA NA PRÁTICA 📚

Esse [repositório](https://github.com/LeanDevLima/Squad02_M4) é dedicado às atividades realizadas durante o Módulo 4 - M4 - LÓGICA DE PROGRAMAÇÃO COM PYTHON do curso de Quality Assurance oferecido pelo [**Instituto JogaJunto**](https://www.jogajuntoinstituto.org/). 

## 🚀 Descrição da 33ª Atividade: 🌟
<br>


🔍 PARTE 1 Crie um DataFrame com os seguintes dados: 
Nome, idade e cidade. Sendo 3 pessoas moradoras de Recife, 2 de Salvador, 1 de são paulo e 1 de Manaus. Depois, filtre os dados para exibir na tela apenas os moradores do Recife. 

```python

import sys
import os

root_dir = os.path.dirname(os.path.abspath(__file__))  # 
project_dir = os.path.join(root_dir, '..') 
sys.path.append(project_dir)  

import pandas as pd

data = {
    'Nome': ['Leanderson', 'Beatriz', 'Bruno', 'Rebeca', 'Sara', 'Mateus', 'Michele'],
    'Idade': [25, 25, 28, 22, 35, 23, 27],
    'Cidade': ['Recife', 'Recife', 'Recife', 'Salvador', 'Salvador', 'São Paulo', 'Manaus']
}

df = pd.DataFrame(data)

moradores_recife = df[df['Cidade'] == 'Recife']

print(moradores_recife)

```
Esse código eu inseri o 'import sys' e o 'import os' e as informações das linhas 4, 5 e 6, para que esse código pudesse ser executado dentro da pasta 'Atividades' conforme o padrão adotado nesse repositório.

O arquivo correspondente a essa atividade está no seguinte local: Atividades\Atividade33.py.

## Integrantes da Squad:

| Beatriz Souza  | [Bruno Soares](https://www.linkedin.com/in/bruno-soaresdev/)  | [Leanderson Lima](https://www.linkedin.com/in/leanderson-dias-de-lima/) | [Rebeca Borges](https://www.linkedin.com/in/rebecaborgess/) | Sara Cruz | 