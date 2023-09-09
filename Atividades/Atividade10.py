
def calcular_idade_cachorro():
    idade_humana = int(input("Digite a idade humana do seu pet: "))
    idade_cachorro = idade_humana * 7
    return idade_cachorro

def calcular_lucro_banho(porte, num_banhos):
    precos = {
        "grande": {"banho": 75.00, "custo": 20.00},
        "medio": {"banho": 60.00, "custo": 15.00},
        "pequeno": {"banho": 50.00, "custo": 5.00}
    }

    banho = precos[porte]["banho"]
    custo = precos[porte]["custo"]
    lucro = (banho - custo) * num_banhos
    return lucro

idade_cachorro = calcular_idade_cachorro()
print(f"Seu pet tem {idade_cachorro} anos.")

num_banhos = int(input("Quantos banhos seu pet tomou nos últimos 12 meses? "))
porte_pet = input("Qual é o porte do seu pet (grande, medio, pequeno)? ").lower()

lucro_total = calcular_lucro_banho(porte_pet, num_banhos)

print(f"Nos últimos 12 meses, o lucro com o pet foi de R${lucro_total:.2f}.")
