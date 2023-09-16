import csv
import os

dados = []

caminho_csv = 'Atividades/atividade29_dados.csv'

if os.path.exists(caminho_csv):
    with open(caminho_csv, newline='') as csvfile:
        leitor = csv.DictReader(csvfile)
        for linha in leitor:
            dados.append(linha)
else:
    print(f"O arquivo CSV '{caminho_csv}' não foi encontrado.")

nome_pasta = 'atividade29'
caminho_pasta = 'Atividades'  
if not os.path.exists(caminho_pasta):
    os.mkdir(caminho_pasta)

for linha in dados:
    print(f"Nome: {linha['nome']}, Endereco: {linha['endereco']}, Email: {linha['email']}, Idade: {linha['idade']}, Renda: {linha['renda']}")

caminho_arquivo_txt = os.path.join(caminho_pasta, 'atividade29_dados.txt')

with open(caminho_arquivo_txt, 'w') as arquivo_txt:
    for linha in dados:
        arquivo_txt.write(f"Nome: {linha['nome']}, Endereco: {linha['endereco']}, Email: {linha['email']}, Idade: {linha['idade']}, Renda: {linha['renda']}\n")
