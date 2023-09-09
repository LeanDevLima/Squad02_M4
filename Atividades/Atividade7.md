# Atividades do Módulo 4 - QA NA PRÁTICA 📚

Esse [repositório](https://github.com/LeanDevLima/Squad02_M4) é dedicado às atividades realizadas durante o Módulo 4 - M4 - LÓGICA DE PROGRAMAÇÃO COM PYTHON do curso de Quality Assurance oferecido pelo [**Instituto JogaJunto**](https://www.jogajuntoinstituto.org/). 

## 🚀 Descrição da 7ª Atividade: 🌟
<br>

🔍Leiam o caso abaixo e executem usando Python. 
A loja "ROUPAS SA" tem 2000 clientes e quer enviar mensagens nominais a cada um. A mensagem seria a seguinte:

"Olá, PAULA MARTINS. Em JANEIRO você realizou uma compra no valor de R$500,00 e ganhou um desconto de 10% em sua próxima compra. Use o cupom PAULAÉ10."



```python

clientes = [
    {"nome": "Paula Martins", "mes_compra": "Janeiro", "valor_compra": 500.00},
    {"nome": "Lean Lima", "mes_compra": "Setembro", "valor_compra": 1000.00},
    {"nome": "Caique DesafioJJ", "mes_compra": "Dezembro", "valor_compra": 2000.00}
    # É possível adicionar mais clientes nessa parte, basta seguir a mesma formatação do exemplo acima.
]

for cliente in clientes:
    nome_completo = cliente["nome"]
    partes_nome = nome_completo.split()  
    primeiro_nome = partes_nome[0]  
    mes_compra = cliente["mes_compra"]
    valor_compra = cliente["valor_compra"]
    desconto = valor_compra * 0.10

    mensagem = f"Olá, {primeiro_nome}. Em {mes_compra} você realizou uma compra no valor de R${valor_compra:.2f} e ganhou um desconto de 10% em sua próxima compra. Use o cupom {primeiro_nome.upper()}É10."

    print(mensagem)


```

O arquivo dessa atividade está nesse repositório dentro da pasta Atividades: Atividades\Atividade7.py.


## Integrantes da Squad:

| Beatriz Souza  | [Bruno Soares](https://www.linkedin.com/in/bruno-soaresdev/)  | [Leanderson Lima](https://www.linkedin.com/in/leanderson-dias-de-lima/) | [Rebeca Borges](https://www.linkedin.com/in/rebecaborgess/) | Sara Cruz | 