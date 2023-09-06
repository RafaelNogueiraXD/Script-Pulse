import re
from models.relatorio import *
def filtraTexto(text, word1, word2=None):
    if word2:
        pattern = re.compile(rf'{re.escape(word1)}.*?{re.escape(word2)}')
        result = re.sub(pattern, word2, text)
    else:
        pattern = re.compile(rf'{re.escape(word1)}.*')
        result = re.sub(pattern, '', text)

    return result

def remove_epoch(texto,word):
    return texto.split(word)[0]

string = leTxt("assets/arquivo.txt")
dicionario = {
    "texto": string,
    "Conditional1": "Epoch"
}


print(remove_epoch(dicionario["texto"],dicionario["Conditional1"]))