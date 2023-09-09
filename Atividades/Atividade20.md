# Atividades do Módulo 4 - QA NA PRÁTICA 📚

Esse [repositório](https://github.com/LeanDevLima/Squad02_M4) é dedicado às atividades realizadas durante o Módulo 4 - M4 - LÓGICA DE PROGRAMAÇÃO COM PYTHON do curso de Quality Assurance oferecido pelo [**Instituto JogaJunto**](https://www.jogajuntoinstituto.org/). 

## 🚀 Descrição da 20ª Atividade: 🌟
<br>

🔍 EM SQUADS Leiam o texto abaixo e resolvam. Na "JUNTOFIT", se um aluno tiver frequência de 21 vezes, sem interrupções, ele ganha um mês de aulas gratuitas para presentear um acompanhante. Caso contrário, ele não se qualifica para o benefício. Na catraca de acesso, haverá uma tela voltada para o cliente. Todos os dias, quando ele passar, deve aparecer a mensagem:

         "VOCÊ ESTÁ PARTICIPANDO DA NOSSA PROMO TREINA JUNTO"

Quando ele completar 21 identificações seguidas, deve aparecer a mensagem:

         "UHUU. AGORA VOCÊ PODE PRESENTEAR UM AMIGO OU AMIGA PARA TREINAR COM VOCÊ".

Caso o cliente tenha uma certa frequência, mas falte algum dia, quando retornar, deve aparecer:

         "QUE BOM VER VOCÊ DE VOLTA. A PARTIR DE AGORA INICIAMOS MAIS UMA CONTAGEM DE 21 DIAS PARA A PROMO TREINA JUNTO."



```python

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

```
O arquivo dessa atividade está nesse repositório dentro da pasta Atividades: Atividades\Atividade20.py.


## Integrantes da Squad:

| Beatriz Souza  | [Bruno Soares](https://www.linkedin.com/in/bruno-soaresdev/)  | [Leanderson Lima](https://www.linkedin.com/in/leanderson-dias-de-lima/) | [Rebeca Borges](https://www.linkedin.com/in/rebecaborgess/) | Sara Cruz | 