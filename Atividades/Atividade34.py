import sys
import os

root_dir = os.path.dirname(os.path.abspath(__file__))  # 
project_dir = os.path.join(root_dir, '..') 
sys.path.append(project_dir)  

import pandas as pd

caminho_arquivo_csv = 'Atividades/atividade_dados.csv'
df = pd.read_csv(caminho_arquivo_csv)

filtro_idade_maior_40 = df['idade'] > 40
pessoas_idade_maior_40 = df[filtro_idade_maior_40]

filtro_renda_maior_5mil = df['renda'] > 5000
pessoas_renda_maior_5mil = df[filtro_renda_maior_5mil]

filtro_renda_maior_15mil = df['renda'] > 15000
pessoas_renda_maior_15mil = df[filtro_renda_maior_15mil]

print("Pessoas com idade maior que 40 anos:")
print(pessoas_idade_maior_40)

print("\nPessoas com renda maior que 5 mil:")
print(pessoas_renda_maior_5mil)

print("\nPessoas com renda maior que 15 mil:")
print(pessoas_renda_maior_15mil)