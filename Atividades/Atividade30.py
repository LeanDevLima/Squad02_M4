def verificar_grupo(numero_matricula):
    if numero_matricula % 2 == 0:
        print("VOCÊ ESTÁ NO TIME AZUL")
    else:
        print("VOCÊ ESTÁ NO TIME AMARELO")

numero_matricula = int(input("Digite o número da matrícula: "))

verificar_grupo(numero_matricula)
