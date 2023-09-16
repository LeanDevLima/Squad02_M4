import requests
import os
import subprocess

integrantes = {
    "Leanderson": "06412-140",
    "Beatriz Souza": "01302-000",
    "Bruno Soares": "70002-900",
    "Rebeca Borges": "04571-060",
    "Sara Cruz": "22031-000"
}

def obter_dados_do_cep(cep):
    url = f"http://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get("localidade")
    else:
        return "CEP não encontrado"

for nome, cep in integrantes.items():
    cidade = obter_dados_do_cep(cep)
    print(f"Nome: {nome}, Cidade: {cidade}")

atividades_path = os.path.join(os.path.dirname(__file__), "atividade28_requirements.txt")

with open(atividades_path, "w") as file:
    result = subprocess.run(["pip", "freeze"], stdout=subprocess.PIPE, text=True)
    file.write(result.stdout)
