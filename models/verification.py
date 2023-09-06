
import os
import json
from datetime import datetime

def check_and_remove_expired_token(file_path="assets/token.json"):
    # Verifique se o arquivo existe
    if not os.path.exists(file_path):
        print(f"O arquivo {file_path} não foi encontrado.")
        return

    # Abra e leia o arquivo JSON
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Converta a string de data/hora de expiração para um objeto datetime
    expiry_date = datetime.strptime(data["expiry"], "%Y-%m-%dT%H:%M:%S.%fZ")

    # Obtenha a hora atual em UTC
    current_date = datetime.utcnow()

    # Verifique se o token expirou
    if current_date > expiry_date:
        os.remove(file_path)
        print(f"O token no arquivo {file_path} expirou e o arquivo foi removido.")
    else:
        print("O token ainda não expirou.")
# Lê os dados de um arquivo JSON
def carregaJson():
    with open('assets/dados.json', 'r') as f:
        data = json.load(f)
    return data
