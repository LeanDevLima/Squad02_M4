# Atividades do Módulo 4 - QA NA PRÁTICA 📚

Esse [repositório](https://github.com/LeanDevLima/Squad02_M4) é dedicado às atividades realizadas durante o Módulo 4 - M4 - LÓGICA DE PROGRAMAÇÃO COM PYTHON do curso de Quality Assurance oferecido pelo [**Instituto JogaJunto**](https://www.jogajuntoinstituto.org/). 

## 🚀 Descrição da 24ª Atividade: 🌟
<br>

🔍PARTE 3 Agora crie um script para com uma lista de frutas, e outra lista com o nome alergias. Insira uma fruta da lista de frutas na lista de alergias. Depois crie um for para cada item da lista passar por uma verificação em uma estrutura condicional para verificar se está essa fruta está contida na lista de alergias. Caso a fruta esteja na lista, imprima na tela o nome dela. 

```python

frutas_seguras = ["maçã", "banana", "laranja", "uva", "pêssego"]


frutas_alergicas = ["abacaxi", "morango", "kiwi", "melancia", "manga"]


fruta_alergia = input("Digite uma fruta que você seja alérgico(a): ")
frutas_alergicas.append(fruta_alergia)


fruta_usuario = input("Digite o nome de uma fruta: ")


if fruta_usuario in frutas_alergicas:
    print(f"Você é alérgico(a) a {fruta_usuario}. Não a consuma!")
elif fruta_usuario in frutas_seguras:
    print(f"Você pode consumir {fruta_usuario}.")
else:
    print(f"A fruta {fruta_usuario} não está na lista de alergias nem na lista de frutas seguras.")

```

O arquivo dessa atividade está nesse repositório dentro da pasta Atividades: Atividades\Atividade24.py.

## Integrantes da Squad:

| Beatriz Souza  | [Bruno Soares](https://www.linkedin.com/in/bruno-soaresdev/)  | [Leanderson Lima](https://www.linkedin.com/in/leanderson-dias-de-lima/) | [Rebeca Borges](https://www.linkedin.com/in/rebecaborgess/) | Sara Cruz | 