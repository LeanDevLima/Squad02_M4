# Atividades do Módulo 4 - QA NA PRÁTICA 📚

Esse [repositório](https://github.com/LeanDevLima/Squad02_M4) é dedicado às atividades realizadas durante o Módulo 4 - M4 - LÓGICA DE PROGRAMAÇÃO COM PYTHON do curso de Quality Assurance oferecido pelo [**Instituto JogaJunto**](https://www.jogajuntoinstituto.org/). 

## 🚀 Descrição da 32ª Atividade: 🌟
<br>

🔍 EM SQUAD Leiam o case e resolvam a situação. A Loja do Joga Junto conta mais uma vez com a colaboração do seu squad! Desta vez, surge a necessidade de desenvolver um programa que analisa o CEP inserido pelo usuário e determina se ele é elegível para frete grátis. Para realizar essa tarefa, foi definida uma política de frete grátis abrangendo todos os estados das regiões Norte e Nordeste do país. 
- Faça um brainstorming com sua equipe sobre o fluxo e requisitos necessários para construção desse programa
- Desenvolva o programa
- Faça casos de teste para este cenário, documente os testes realizados e insira no Bitrix
- Caso seja encontrado algum bug no seu código, documente-o. 

---

**Brainstorming:**

1. **Requisitos Principais:**
   - O programa deve receber o CEP do usuário.
   - Deve verificar se o CEP pertence a um estado das regiões Norte ou Nordeste.
   - Se o CEP estiver nas regiões elegíveis, o frete deve ser marcado como grátis.
   - Caso contrário, o frete não deve ser grátis.

2. **Interface de Usuário:**
   - Criar uma interface simples para que o usuário possa inserir o CEP.
   - Exibir uma mensagem clara sobre a elegibilidade do frete grátis após a verificação.

3. **Lógica de Verificação:**
   - Criar uma lista de estados que fazem parte das regiões Norte e Nordeste.
   - Verificar se o estado associado ao CEP está na lista de estados elegíveis.

4. **Testes:**
   - Realizar testes com CEPs de diferentes estados e regiões para garantir que o programa esteja funcionando corretamente.
   - Documentar os casos de teste e os resultados esperados.

---

**Desenvolvimento do programa:**

```python

import requests

def verificar_frete_gratis(cep):
    cep_formatado = ''.join(filter(str.isdigit, cep))

    url = f"https://viacep.com.br/ws/{cep_formatado}/json/"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        estado = data.get("uf", "").upper()
        
        estados_elegiveis = ["AC", "AL", "AM", "AP", "BA", "CE", "MA", "PA", "PB", "PE", "PI", "RN", "RO", "RR", "TO"]

        if estado in estados_elegiveis:
            return True
        else:
            return False
    else:
        print("Erro ao consultar o CEP. Verifique se o CEP é válido.")
        return False

cep_usuario = input("Digite o CEP: ")

if verificar_frete_gratis(cep_usuario):
    print("Frete grátis disponível para o seu CEP!")
else:
    print("Não há frete grátis para o seu CEP.")

```

---

**Casos de teste:**

De acordo com a atividade, abaixo constam o que podem ser possíveis casos de testes para ess ecenário.

**Caso de Teste 1:**
- CEP: 69000-000 (Amazonas)
- Resultado Esperado: Frete grátis disponível para o seu CEP!

**Caso de Teste 2:**
- CEP: 87000-000 (Paraná)
- Resultado Esperado: Não há frete grátis para o seu CEP.

**Caso de Teste 3:**
- CEP: 60000-000 (Ceará)
- Resultado Esperado: Frete grátis disponível para o seu CEP!

**Caso de Teste 4:**
- CEP: 15000-000 (São Paulo)
- Resultado Esperado: Não há frete grátis para o seu CEP.

**Caso de Teste 5:**
- CEP: 58000-000 (Paraíba)
- Resultado Esperado: Frete grátis disponível para o seu CEP!

---

O arquivo dessa atividade está nesse repositório dentro da pasta Atividades: Atividades\Atividade32.py.

## Integrantes da Squad:

| Beatriz Souza  | [Bruno Soares](https://www.linkedin.com/in/bruno-soaresdev/)  | [Leanderson Lima](https://www.linkedin.com/in/leanderson-dias-de-lima/) | [Rebeca Borges](https://www.linkedin.com/in/rebecaborgess/) | Sara Cruz | 