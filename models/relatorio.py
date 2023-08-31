
def escrevendoRelatorio(data,dataJson):
    nome = "Rafael Nogueira Rodrigues"
    idade = 21
    texto = f"""
    Email do remetente: {dataJson['emailSender']}
    Email destinatário: {dataJson['emailRecipient']}
    Arquivo que foi executado: \n {data['nomeArquivo']}
    conteudo da mensagem é: {data['conteudo']}
    Tempo de execução do arquivo(em segundos): {data['tempoExecArquivo']}  
    Tempo que o App demorou para Copiar(em segundos): {data['tempoApp']}     
    """
    data = {
        "title" : "um novo email",
        "content" : texto
    }
    return data

def escreveTxt(data):
    with open("assets/arquivo.txt", "w", encoding="utf-8") as file:
        file.write(data['content'])