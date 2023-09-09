# Atividades do Módulo 4 - QA NA PRÁTICA 📚

Esse [repositório](https://github.com/LeanDevLima/Squad02_M4) é dedicado às atividades realizadas durante o Módulo 4 - M4 - LÓGICA DE PROGRAMAÇÃO COM PYTHON do curso de Quality Assurance oferecido pelo [**Instituto JogaJunto**](https://www.jogajuntoinstituto.org/). 

## 🚀 Descrição da 10ª Atividade: 🌟
<br>

🔍 Em SQUADs Mini Case 1: Idade do Pet e Lucro do PETSHOP A dona de um PETSHOP quer criar um programa para calcular a idade dos cachorros de seus clientes em "anos de cachorro". Como os pets envelhecem de maneira diferente dos humanos - cada ano humano corresponde a 7 do Cachorro. Desafio: Crie um programa Python que calcule a idade de cachorro com base na idade humana. O que seu programa deve conter: 

- Solicitar ao usuário a idade humana do pet (um número inteiro);
- Calcular a idade do pet, levando em consideração que cada ano da idade humana corresponde a 7;
- Exibir a idade do pet ao usuário;
- Além disso, ela deseja calcular, a cada 12 meses, o lucro obtido por banho e por cachorro. 

VALORES POR BANHO X CUSTO POR BANHO

- Cachorro de grande porte: BANHO: R$75,00 | CUSTO: R$20,00
- Cachorro de médio porte: BANHO: R$60,00 | CUSTO: 15,00
- Cachorro de médio porte: BANHO: R$50,00 | CUSTO: R$5,00
- Exemplo: Se um animal de grande porte tomar 10 banhos em 12 meses, no final, o programa deve imprimir a seguinte informação:

      Olá, Tuco tem 35 anos e nos últimos 12 meses o lucro com  este animal foi de R$550,00

```python

def calcular_idade_cachorro():
    idade_humana = int(input("Digite a idade humana do seu pet: "))
    idade_cachorro = idade_humana * 7
    return idade_cachorro

def calcular_lucro_banho(porte, num_banhos):
    precos = {
        "grande": {"banho": 75.00, "custo": 20.00},
        "medio": {"banho": 60.00, "custo": 15.00},
        "pequeno": {"banho": 50.00, "custo": 5.00}
    }

    banho = precos[porte]["banho"]
    custo = precos[porte]["custo"]
    lucro = (banho - custo) * num_banhos
    return lucro

idade_cachorro = calcular_idade_cachorro()
print(f"Seu pet tem {idade_cachorro} anos.")

num_banhos = int(input("Quantos banhos seu pet tomou nos últimos 12 meses? "))
porte_pet = input("Qual é o porte do seu pet (grande, medio, pequeno)? ").lower()

lucro_total = calcular_lucro_banho(porte_pet, num_banhos)

print(f"Nos últimos 12 meses, o lucro com o pet foi de R${lucro_total:.2f}.")

```
O arquivo dessa atividade está nesse repositório dentro da pasta Atividades: Atividades\Atividade10.py.


## Integrantes da Squad:

| Beatriz Souza  | [Bruno Soares](https://www.linkedin.com/in/bruno-soaresdev/)  | [Leanderson Lima](https://www.linkedin.com/in/leanderson-dias-de-lima/) | [Rebeca Borges](https://www.linkedin.com/in/rebecaborgess/) | Sara Cruz | 