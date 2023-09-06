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
    with open("assets/arquivo.txt", "w", encoding="utf-8") as file:
        file.write(data['content'])

def leTxt(arquivo):
    with open(arquivo, "r", encoding="utf-8") as file:
        contet = file.read()
        

def remove_text_between_words(text, word1, word2=None):
    if word2:
        pattern = re.compile(rf'{re.escape(word1)}.*?{re.escape(word2)}')
        result = re.sub(pattern, word2, text)
    else:
        pattern = re.compile(rf'{re.escape(word1)}.*')
        result = re.sub(pattern, '', text)
    
    return result
