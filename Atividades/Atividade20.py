
frequencia = 0
dias_seguidos = 0

while True:

    input("Pressione Enter para registrar sua presença hoje: ")

    frequencia += 1

    if frequencia == 21:
        print("UHUU. AGORA VOCÊ PODE PRESENTEAR UM AMIGO OU AMIGA PARA TREINAR COM VOCÊ.")
        dias_seguidos = 0  
    else:
        print("VOCÊ ESTÁ PARTICIPANDO DA NOSSA PROMO TREINA JUNTO")

    escolha = input("Deseja continuar treinando? (S para sim, qualquer outra tecla para sair): ").strip().lower()

    if escolha != 's':
        break

    if frequencia < 21:
        dias_seguidos += 1
        if dias_seguidos == 1:
            print("QUE BOM VER VOCÊ DE VOLTA. A PARTIR DE AGORA INICIAMOS MAIS UMA CONTAGEM DE 21 DIAS PARA A PROMO TREINA JUNTO.")
        else:
            print(f"QUE BOM VER VOCÊ DE VOLTA. CONTINUE ASSIM! Mais {21 - dias_seguidos} dias para a promoção.")
            dias_seguidos = 0
