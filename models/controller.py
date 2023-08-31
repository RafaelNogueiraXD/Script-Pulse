from models.fileData import *
from telas.notifica import *
from models.relatorio import *
from models.email.enviaEmail import *
from datetime import datetime
import tkinter as tk
from tkinter import messagebox
import json

# Lê os dados de um arquivo JSON
def carregaJson():
    with open('assets/dados.json', 'r') as f:
        data = json.load(f)
    return data
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

# Teste a função
check_and_remove_expired_token()
check_and_remove_expired_token("assets/token1.json")


dataJson = carregaJson()
conteudo_arquivo = ''

def btn_select_file(ssh=0):
    global conteudo_arquivo 
    conteudo_arquivo = open_file_dialog(ssh)
    btn_submit_file(ssh)
    
def btn_submit_file(ssh=0):
    if conteudo_arquivo != '':
        format_text = escrevendoRelatorio(conteudo_arquivo,dataJson)
        print(format_text)
        escreveTxt(format_text)
        envia_email(conteudo=format_text, addr=dataJson)
        # print("\n\nemail 'enviado' hehe \n\n")
        if ssh == 0:
            aviso("success")
        else:
            print("\n\ntarefa completada\n\n")
    else: 
        if ssh == 0:
            aviso("erro")
        else:
            print("\n\n erro ao completar a tarefa, verifique as configuracoes\n")
            

def btn_configure(ssh=0):
    global dataJson
    if ssh == 0:
        configure_data(dataJson)
    else:
        print(f"\nEmail Remetente : {dataJson['emailSender']}")
        print(f"\nEmail Destinatario : {dataJson['emailRecipient']}")
        print(f"\nDeseja mesmo alterar essas informações?(1 - sim/2 - nao)")
        if input() == 1:
            data = {"emailSender":input(), "emailRecipient":input()}
            escreveJson(data)
    dataJson = carregaJson()




