# Atividades do Módulo 4 - QA NA PRÁTICA 📚

Esse [repositório](https://github.com/LeanDevLima/Squad02_M4) é dedicado às atividades realizadas durante o Módulo 4 - M4 - LÓGICA DE PROGRAMAÇÃO COM PYTHON do curso de Quality Assurance oferecido pelo [**Instituto JogaJunto**](https://www.jogajuntoinstituto.org/). 

## 🚀 Descrição da 29ª Atividade: 🌟
<br>

🔍 DESAFIO DO CAIQUE Vamos explorar o poder da biblioteca OS! Prepare-se para mergulhar no mundo da interação entre o Python e o seu sistema operacional. Vamos aprender a usar a biblioteca OS em conjunto com funções nativas do Python para criar algo. O desafio é o seguinte: você vai criar uma lista de dados e, usando a biblioteca OS, interagir com o seu sistema operacional. Além disso, também criará uma nova pasta para salvar o arquivo de texto txt.

Para essa atividade, tomei como base o arquivo Atividades\atividade29_dados.csv que está nesse repositório. Aqui está o início do conteúdo desse arquivo.

```csv
,nome,endereco,email,idade,renda
0,Rafaela Rezende,"Avenida de Ribeiro
Santa Helena
14342136 Caldeira das Pedras / SP",mouraheitor@example.org,46,15594.52
1,Srta. Beatriz das Neves,"Loteamento de Fogaça, 61
Vila Novo São Lucas
11233-022 Monteiro / SC",luiz-otaviocorreia@example.org,24,16478.26
2,Ana Clara das Neves,"Favela Pinto, 97
São José
60325-119 Rodrigues / MS",isisalmeida@example.org,28,13729.48
3,Olivia Silva,"Vereda de Duarte, 12
Vila Satélite
91893-339 Souza / RN",lpeixoto@example.org,23,18478.46
4,Alexia Martins,"Conjunto João Pedro Caldeira, 888
Sion
81988-738 Azevedo da Mata / MA",carvalhoana-beatriz@example.com,54,9988.47
5,Lorena Almeida,"Morro Luiz Gustavo Castro, 61
Liberdade
02189859 Pereira / PI",mdas-neves@example.com,66,2224.67
6
.
.
.
```
---
Para executar o que essa tarefa pedia, executei o seguinte código:

---

```python
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
        arquivo_txt.write(f"Nome: {linha['nome']}, Idade: {linha['idade']}\n")


```

Este código, primeiro, importa algumas ferramentas úteis para lidar com informações em um formato chamado CSV. 

Em seguida, pega as informações do arquivo que está guardado em 'Atividades/atividade29_dados.csv' e guarda essas informações em uma lista chamada 'dados'. 

Antes de fazer isso, o código verifica se esse arquivo existe para não ter problemas. 

Depois, o código verifica se há uma pasta chamada 'Atividades', caso ela não exista ela será criada. Como ela já existe nesse repositório, não será executada nenhuma ação.

Com um tipo de repetição, mostramos no terminal os nomes e idades das informações do arquivo CSV. Como nesse exemplo:

```bash
$ python -u "c:\Users\...\GitHub\Squad02_M4\Atividades\Atividade29.py"
Nome: Rafaela Rezende, Endereco: Avenida de Ribeiro
Santa Helena
14342136 Caldeira das Pedras / SP, Email: mouraheitor@example.org, Idade: 46, Renda: 15594.52
Nome: Srta. Beatriz das Neves, Endereco: Loteamento de FogaÃ§a, 61
Vila Novo SÃ£o Lucas
11233-022 Monteiro / SC, Email: luiz-otaviocorreia@example.org, Idade: 24, Renda: 16478.26
Nome: Ana Clara das Neves, Endereco: Favela Pinto, 97
SÃ£o JosÃ©
60325-119 Rodrigues / MS, Email: isisalmeida@example.org, Idade: 28, Renda: 13729.48
Nome: Olivia Silva, Endereco: Vereda de Duarte, 12
Vila SatÃ©lite
91893-339 Souza / RN, Email: lpeixoto@example.org, Idade: 23, Renda: 18478.46
Nome: Alexia Martins, Endereco: Conjunto JoÃ£o Pedro Caldeira, 888
Sion
81988-738 Azevedo da Mata / MA, Email: carvalhoana-beatriz@example.com, Idade: 54, Renda: 9988.47
Nome: Lorena Almeida, Endereco: Morro Luiz Gustavo Castro, 61
Liberdade
02189859 Pereira / PI, Email: mdas-neves@example.com, Idade: 66, Renda: 2224.67
.
.
.
```

Para terminar, o código cria um novo arquivo de texto ('Atividades/atividade29_dados.txt') e coloca essas mesmas informações nele. 

```txt
Nome: Rafaela Rezende, Endereco: Avenida de Ribeiro
Santa Helena
14342136 Caldeira das Pedras / SP, Email: mouraheitor@example.org, Idade: 46, Renda: 15594.52
Nome: Srta. Beatriz das Neves, Endereco: Loteamento de Fogaça, 61
Vila Novo São Lucas
11233-022 Monteiro / SC, Email: luiz-otaviocorreia@example.org, Idade: 24, Renda: 16478.26
Nome: Ana Clara das Neves, Endereco: Favela Pinto, 97
São José
60325-119 Rodrigues / MS, Email: isisalmeida@example.org, Idade: 28, Renda: 13729.48
Nome: Olivia Silva, Endereco: Vereda de Duarte, 12
Vila Satélite
91893-339 Souza / RN, Email: lpeixoto@example.org, Idade: 23, Renda: 18478.46
Nome: Alexia Martins, Endereco: Conjunto João Pedro Caldeira, 888
Sion
81988-738 Azevedo da Mata / MA, Email: carvalhoana-beatriz@example.com, Idade: 54, Renda: 9988.47
.
.
.
```

O arquivo dessa atividade está nesse repositório dentro da pasta Atividades: Atividades\Atividade29.py.

## Integrantes da Squad:

| Beatriz Souza  | [Bruno Soares](https://www.linkedin.com/in/bruno-soaresdev/)  | [Leanderson Lima](https://www.linkedin.com/in/leanderson-dias-de-lima/) | [Rebeca Borges](https://www.linkedin.com/in/rebecaborgess/) | Sara Cruz | 