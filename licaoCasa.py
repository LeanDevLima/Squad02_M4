'''
Crie um script com as seguintes instruções, pesquisando na internet como fazer:


Crie uma tupla com 5 dados
Altere a tupla para uma lista
Insira 2 dados extras a essa lista
Remova o primeiro dado da lista
Remova o último dado da lista
Faça um print com o primeiro dado da lista
Faça um print com a quantidade de dados da lista
Crie um dicionário com os seguintes dados:
Nome, Idade, Profissão

Imprima somente o valor contido na chave Nome do dicionário

'''


# Crie uma tupla com 5 dados
tupla = (1, 2, 3, 4, 5, 6)

# Altere a tupla para uma lista
lista = list(tupla)

# Insira 2 dados extras na lista
lista.append(7)
lista.append(8)

# Remova o primeiro dado da lista
del lista[0]

# Remova o último dado da lista
lista.pop()

# Faça um print com o primeiro dado da lista
print("Primeiro dado da lista:", lista[0])

# Faça um print com a quantidade de dados da lista
print("Quantidade de dados na lista:", len(lista))

# Crie um dicionário com os seguintes dados: Nome, Idade, Profissão
dicionario = {
    "Nome": "Lean",
    "Idade": 25,
    "Profissão": "Desenvolvedor"
}

# Imprima somente o valor contido na chave Nome do dicionário
print("Nome no dicionário:", dicionario["Nome"])
