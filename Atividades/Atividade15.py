tupla = (1, 2, 3, 4, 5, 6)
lista = list(tupla)
lista.append(7)
lista.append(8)

del lista[0]
lista.pop()

print("Primeiro dado da lista:", lista[0])
print("Quantidade de dados na lista:", len(lista))

dicionario = {
    "Nome": "Lean",
    "Idade": 25,
    "Profissão": "Desenvolvedor"
}

print("Nome no dicionário:", dicionario["Nome"])
