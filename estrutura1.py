# Solicitar ao usuário um valor para a tabuada
numero = int(input("Digite um número para a tabuada: "))

# Imprimir a tabuada
print(f"Tabuada do {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
