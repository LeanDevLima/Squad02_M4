# Atividades do Módulo 4 - QA NA PRÁTICA 📚

Esse [repositório](https://github.com/LeanDevLima/Squad02_M4) é dedicado às atividades realizadas durante o Módulo 4 - M4 - LÓGICA DE PROGRAMAÇÃO COM PYTHON do curso de Quality Assurance oferecido pelo [**Instituto JogaJunto**](https://www.jogajuntoinstituto.org/). 

## 🚀 Descrição da 31ª Atividade: 🌟
<br>

🔍 EM SQUADs Agora, criem um scritp para: 
- Ter um input de usuário para inserir os números de matrícula em uma lista. 
- Ter um validador nessa lista que permita a inserção de dados até ocupar 5 espaços index.
- Fazer um laço de repetição para passar todos os números da lista em uma função para verificar se o número é par ou ímpar. 

```python

numeros_de_matricula = []

while len(numeros_de_matricula) < 5:
    numero = input("Digite um número de matrícula ou 'q' para sair: ")
    
    if numero.lower() == 'q':
        break
    
    if numero.isdigit():
        numeros_de_matricula.append(int(numero))
    else:
        print("Por favor, insira um número válido.")

for numero in numeros_de_matricula:
    if numero % 2 == 0:
        print(f"{numero} é um número de matrícula par.")
    else:
        print(f"{numero} é um número de matrícula ímpar.")

```

O arquivo dessa atividade está nesse repositório dentro da pasta Atividades: Atividades\Atividade31.py.

## Integrantes da Squad:

| Beatriz Souza  | [Bruno Soares](https://www.linkedin.com/in/bruno-soaresdev/)  | [Leanderson Lima](https://www.linkedin.com/in/leanderson-dias-de-lima/) | [Rebeca Borges](https://www.linkedin.com/in/rebecaborgess/) | Sara Cruz | 