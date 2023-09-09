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
