import re

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
    with open("assets/saida.txt", "w+", encoding="utf-8") as file:
        file.write(data['content'])

def leTxt(arquivo):
    with open(arquivo, "r", encoding="utf-8") as file:
        content = file.read()
    return content

        

def filtraTexto(text, word1, word2=None):
    if word2:
        pattern = re.compile(rf'{re.escape(word1)}.*?{re.escape(word2)}')
        result = re.sub(pattern, word2, text)
    else:
        pattern = re.compile(rf'{re.escape(word1)}.*')
        result = re.sub(pattern, '', text)
    
    return result
def remove(texto,word):
    return texto.split(word)[0]


def criaContent(dicionario):
    conteudo_arquivo  = {
        "nomeArquivo": None,
        "conteudo": None,
        "tempoExecArquivo": None,
        "tempoApp": None
    }

    if dicionario["path"] is not None:
        conteudo_arquivo["conteudo"] = leTxt(dicionario["path"])
        print(conteudo_arquivo["conteudo"])
    
    if dicionario["texto"] is not None:
        conteudo_arquivo["conteudo"] = dicionario["texto"]

    if dicionario["Conditional1"] is not None:
        conteudo_arquivo["conteudo"]  = remove(conteudo_arquivo["conteudo"], dicionario["Conditional1"])
        # print(filtraTexto(conteudo_arquivo["conteudo"], dicionario["Conditional1"]))
        if dicionario["Conditional2"] != " ":
            conteudo_arquivo["conteudo"]  = filtraTexto(conteudo_arquivo["conteudo"], dicionario["Conditional1"], dicionario["Conditional2"])
            # print("valor do conditional: ", dicionario["Conditional2"])
            # print(filtraTexto(conteudo_arquivo["conteudo"], dicionario["Conditional1"],dicionario["Conditional2"]))
    return conteudo_arquivo
