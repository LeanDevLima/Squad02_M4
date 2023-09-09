# Atividades do Módulo 4 - QA NA PRÁTICA 📚

Esse [repositório](https://github.com/LeanDevLima/Squad02_M4) é dedicado às atividades realizadas durante o Módulo 4 - M4 - LÓGICA DE PROGRAMAÇÃO COM PYTHON do curso de Quality Assurance oferecido pelo [**Instituto JogaJunto**](https://www.jogajuntoinstituto.org/). 

## 🚀 Descrição da 19ª Atividade: 🌟
<br>

🔍 EM SQUADS Leiam o texto abaixo e resolvam. Na "FashionStyle", para um cliente obter 10% de desconto em suas compras, a compra deve ser de pelo menos R$250,00 e para obter 30%, a compra deve ser acima de R$500,00. Caso contrário, nenhum desconto é aplicado. No caixa, haverá uma tela voltada para o cliente. Ao passar o produto, caso cumpra o requisito da promoção, aparecerá a mensagem:

- Caso o cliente não cumpra o requisito, deve aparecer "POXA, FALTA POUCO PARA VOCÊ GANHAR 10% DE DESCONTO EM SUA COMPRA."

- Caso o cliente faça uma compra acima de R$250,00 "PARABÉNS. VOCÊ GANHOU 10% DE DESCONTO, MAS PODE GANHAR 30% SE SUA COMPRA FOR ACIMA DE R$500,00"

- Caso o cliente faça uma compra acima de R$500,00 "PARABÉNS. VOCÊ GANHOU SUPER DESCONTO DE 30%"

```python

valor_compra = float(input("Digite o valor da compra: R$"))

mensagem_desconto = ""

if valor_compra >= 500.0:
    mensagem_desconto = "Você ganhou 30% de desconto! PARABÉNS!"
    valor_compra = valor_compra * 0.7
elif valor_compra >= 250.0:
    mensagem_desconto = "Você ganhou 10% de desconto! PARABÉNS!"
    valor_compra = valor_compra * 0.9
else:
    mensagem_desconto = "Quase lá! Com mais R$%.2f, você ganha 10%% de desconto." % (250.0 - valor_compra)

print(mensagem_desconto)

print("Total a pagar: R$%.2f" % valor_compra)

```
O arquivo dessa atividade está nesse repositório dentro da pasta Atividades: Atividades\Atividade19.py.


## Integrantes da Squad:

| Beatriz Souza  | [Bruno Soares](https://www.linkedin.com/in/bruno-soaresdev/)  | [Leanderson Lima](https://www.linkedin.com/in/leanderson-dias-de-lima/) | [Rebeca Borges](https://www.linkedin.com/in/rebecaborgess/) | Sara Cruz | 