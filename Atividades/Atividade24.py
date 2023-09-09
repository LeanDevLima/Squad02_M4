
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
