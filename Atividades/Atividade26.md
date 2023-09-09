# Atividades do Módulo 4 - QA NA PRÁTICA 📚

Esse [repositório](https://github.com/LeanDevLima/Squad02_M4) é dedicado às atividades realizadas durante o Módulo 4 - M4 - LÓGICA DE PROGRAMAÇÃO COM PYTHON do curso de Quality Assurance oferecido pelo [**Instituto JogaJunto**](https://www.jogajuntoinstituto.org/). 

## 🚀 Descrição da 26ª Atividade: 🌟
<br>

🔍EM SQUADS Leiam o texto abaixo e resolvam. O instituto Joga Junto vai checar todos os emails existentes utilizados pelos usuários. Para isso sua equipe precisará criar  um código para verificar se o email inserido pelo usuário tem o @jogajuntoinstituto.org no texto. Crie um input para verificar esse texto. Crie casos de teste escritos em BDD, um com sucesso, e outro com falha. Execute os testes, documente e suba os resultados no Bitrix da sua equipe. 


```python

email = input("Digite o seu email: ")

if "@jogajuntoinstituto.org" in email:
    print("Email válido do Instituto Joga Junto.")
else:
    print("Email não pertence ao Instituto Joga Junto.")

```

O arquivo dessa atividade está nesse repositório dentro da pasta Atividades: Atividades\Atividade26.py.

- Aqui estão algumas sugestões de casos de teste aplicáveis neste cenário:
---

### Caso de Teste 1 (Sucesso):

**Dado** que o usuário insira o email "joao@jogajuntoinstituto.org"

**Quando** o código for executado

**Então** o código deve imprimir "Email válido do Instituto Joga Junto."

---

### Caso de Teste 2 (Sucesso):

**Dado** que o usuário insira o email "alice@jogajuntoinstituto.org"

**Quando** o código for executado

**Então** o código deve imprimir "Email válido do Instituto Joga Junto."

---
### Caso de Teste 3 (Falha):

**Dado** que o usuário insira o email "maria@gmail.com"

**Quando** o código for executado

**Então** o código deve imprimir "Email não pertence ao Instituto Joga Junto."

---
### Caso de Teste 4 (Sucesso):

**Dado** que o usuário insira o email "contato@jogajuntoinstituto.org"

**Quando** o código for executado

**Então** o código deve imprimir "Email válido do Instituto Joga Junto."

---
### Caso de Teste 5 (Falha):

**Dado** que o usuário insira o email "pedro@outrodominio.com"

**Quando** o código for executado

**Então** o código deve imprimir "Email não pertence ao Instituto Joga Junto."

---
### Caso de Teste 6 (Sucesso):

**Dado** que o usuário insira o email "info@jogajuntoinstituto.org"

**Quando** o código for executado

**Então** o código deve imprimir "Email válido do Instituto Joga Junto."

---



## Integrantes da Squad:

| Beatriz Souza  | [Bruno Soares](https://www.linkedin.com/in/bruno-soaresdev/)  | [Leanderson Lima](https://www.linkedin.com/in/leanderson-dias-de-lima/) | [Rebeca Borges](https://www.linkedin.com/in/rebecaborgess/) | Sara Cruz | 