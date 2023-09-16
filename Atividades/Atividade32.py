import requests

def verificar_frete_gratis(cep):
    cep_formatado = ''.join(filter(str.isdigit, cep))

    url = f"https://viacep.com.br/ws/{cep_formatado}/json/"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        estado = data.get("uf", "").upper()
        
        estados_elegiveis = ["AC", "AL", "AM", "AP", "BA", "CE", "MA", "PA", "PB", "PE", "PI", "RN", "RO", "RR", "TO"]

        if estado in estados_elegiveis:
            return True
        else:
            return False
    else:
        print("Erro ao consultar o CEP. Verifique se o CEP é válido.")
        return False

cep_usuario = input("Digite o CEP: ")

if verificar_frete_gratis(cep_usuario):
    print("Frete grátis disponível para o seu CEP!")
else:
    print("Não há frete grátis para o seu CEP.")
