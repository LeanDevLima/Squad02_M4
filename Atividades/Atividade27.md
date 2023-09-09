# Atividades do Módulo 4 - QA NA PRÁTICA 📚

Esse [repositório](https://github.com/LeanDevLima/Squad02_M4) é dedicado às atividades realizadas durante o Módulo 4 - M4 - LÓGICA DE PROGRAMAÇÃO COM PYTHON do curso de Quality Assurance oferecido pelo [**Instituto JogaJunto**](https://www.jogajuntoinstituto.org/). 

## 🚀 Descrição da 27ª Atividade: 🌟
<br>

🔍EM SQUADS Leiam o texto abaixo e resolvam. Desenvolvam um programa que conte quantas vogais (a, e, i, o, u) existem em uma palavra fornecida pelo usuário. Implementem uma função que receba uma palavra qualquer (string) como entrada.
O programa deve imprimir o número total de vogais na palavra.

Solicitação de Entrada: 
- Implementem a solicitação de entrada de uma palavra (string).

Contagem de Vogais:
- Implemente um loop "for" ou "while" para percorrer cada caractere da palavra.
Verifique se cada caractere é uma vogal (a, e, i, o, u) e conte-as.
Imprima o número total de vogais na palavra.

```python

def contar_vogais(palavra):
    vogais = "aeiouAEIOU"  
    contador = 0

    for caractere in palavra:
        if caractere in vogais:
            contador += 1

    return contador

palavra = input("Digite uma palavra: ")

total_vogais = contar_vogais(palavra)

print(f"Total de vogais na palavra '{palavra}': {total_vogais}")

```


O arquivo dessa atividade está nesse repositório dentro da pasta Atividades: Atividades\Atividade27.py.

## Integrantes da Squad:

| Beatriz Souza  | [Bruno Soares](https://www.linkedin.com/in/bruno-soaresdev/)  | [Leanderson Lima](https://www.linkedin.com/in/leanderson-dias-de-lima/) | [Rebeca Borges](https://www.linkedin.com/in/rebecaborgess/) | Sara Cruz | 