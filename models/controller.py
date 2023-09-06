from models.fileData import *
from telas.notifica import *
from models.relatorio import *
from models.email.enviaEmail import *
from models.verification import *
from datetime import datetime
import tkinter as tk
from tkinter import messagebox
import os
import json
from datetime import datetime


# Verifica se os tokens precisam ser restaurados 
check_and_remove_expired_token()
check_and_remove_expired_token("assets/token1.json")

# carrega dados do usuario
dataJson = carregaJson()
conteudo_arquivo = ''

def btn_select_file(ssh=0):
    global conteudo_arquivo 
    conteudo_arquivo = open_file_dialog(ssh)
    btn_submit_file(ssh)
    
def btn_submit_file(ssh=0,outputExterno=None,path=None):
    # caso usuario deseje usar um output de um programa que não foi processado pelo PulseScript(esse app)
    if path != None:
        conteudo_arquivo  = {
            "nomeArquivo": "sem info",
            "conteudo": leTxt(path),
            "tempoExecArquivo": "sem info",
            "tempoApp": "sem informação"
        }
    
    if outputExterno != None:
        conteudo_arquivo = {
            "nomeArquivo": "sem info",
            "conteudo": outputExterno,
            "tempoExecArquivo": "sem info",
            "tempoApp": "sem informação"    
        }

    if conteudo_arquivo != '':
        format_text = escrevendoRelatorio(conteudo_arquivo,dataJson)
        print(format_text)
        escreveTxt(format_text)
        # envia_email(conteudo=format_text, addr=dataJson)
        print("\n\nemail 'enviado' hehe \n\n")
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




