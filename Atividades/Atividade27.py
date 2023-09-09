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