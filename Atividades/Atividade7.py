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
