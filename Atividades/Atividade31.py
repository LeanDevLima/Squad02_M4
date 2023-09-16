
numeros_de_matricula = []

while len(numeros_de_matricula) < 5:
    numero = input("Digite um número de matrícula ou 'q' para sair: ")
    
    if numero.lower() == 'q':
        break
    
    if numero.isdigit():
        numeros_de_matricula.append(int(numero))
    else:
        print("Por favor, insira um número válido.")

for numero in numeros_de_matricula:
    if numero % 2 == 0:
        print(f"{numero} é um número de matrícula par.")
    else:
        print(f"{numero} é um número de matrícula ímpar.")
