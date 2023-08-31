from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from models.docs.funcoesDocs import *
# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/documents']
# The ID of a sample document.
DOCUMENT_ID = '1M8993QV8YrkSSYCX08pPgndboWSO2FR0M6wZcceFrNw'
introducao = """
Em uma cidade esquecida pelo tempo, onde as sombras dançam ao ritmo do vento e os rios cantam canções antigas, as pessoas vivem em harmonia com a natureza. Cada amanhecer traz consigo promessas de novas aventuras e cada pôr do sol, reflexões sobre os mistérios da vida. Neste lugar, as histórias não são apenas contadas, elas são vividas. E é aqui que nossa jornada começa, entre sonhos entrelaçados e realidades paralelas, buscando entender o verdadeiro significado da existência.
"""
desenvolvimento = """
Nas ruas estreitas e sinuosas da cidade, as crianças corriam descalças, seus risos ecoando como uma melodia alegre. Os anciãos, sentados à sombra das árvores centenárias, compartilhavam histórias de tempos passados, transmitindo sabedoria e tradição de geração em geração. No mercado central, vendedores exibiam suas mercadorias coloridas, desde tecidos tecidos à mão até frutas exóticas, cada item contando sua própria história.
Lena, uma jovem curiosa da cidade, sempre se sentiu atraída pelas lendas que ouvia. Ela cresceu ouvindo falar do "Espelho do Tempo", um artefato místico que diziam possuir o poder de revelar o futuro. Movida por uma combinação de coragem e curiosidade, Lena decidiu embarcar em uma missão para encontrar este espelho. Sua busca a levou por florestas densas, montanhas imponentes e vales profundos. Ao longo do caminho, ela encontrou personagens fascinantes, cada um contribuindo com uma peça do quebra-cabeça.
"""
conclusao = """
Depois de meses de busca, Lena finalmente encontrou o Espelho do Tempo em uma caverna escondida, protegida por um velho guardião. No entanto, em vez de revelar o futuro, o espelho mostrou a Lena reflexos de suas próprias experiências, escolhas e as pessoas que ela encontrou em sua jornada. O guardião, vendo a decepção no rosto de Lena, disse-lhe: "O verdadeiro poder do espelho não é mostrar o futuro, mas sim refletir a riqueza de nossas próprias vidas e as lições aprendidas ao longo do caminho."

Lena voltou para sua cidade com uma compreensão mais profunda de si mesma e do mundo ao seu redor. Ela percebeu que a verdadeira jornada não estava em buscar respostas em artefatos místicos, mas em viver plenamente e aprender com cada experiência. E assim, a lenda do Espelho do Tempo tornou-se uma história de autodescoberta, lembrando a todos na cidade que o verdadeiro valor está nas jornadas que escolhemos empreender e nas memórias que criamos ao longo do caminho.
"""
output = """
    conteudo da mensagem é: Compilação bem-sucedida
Taxa de compressao: 96.94%
Arquivo convertido com sucesso. Resultados salvos nos arquivos outros/desconprimi-Image1.TIFF
Taxa de compressao: 98.72%
Arquivo convertido com sucesso. Resultados salvos nos arquivos outros/desconprimi-Image1.bmp
Taxa de compressao: -30.29%
Arquivo convertido com sucesso. Resultados salvos nos arquivos outros/desconprimi-usaDoc.docx
Taxa de compressao: -31.82%
Arquivo convertido com sucesso. Resultados salvos nos arquivos outros/desconprimi-usaMp3.mp3
Taxa de compressao: -25.78%
Arquivo convertido com sucesso. Resultados salvos nos arquivos outros/desconprimi-usaWav.wav
Taxa de compressao: 56.26%
Arquivo convertido com sucesso. Resultados salvos nos arquivos IMAGENS/desconprimi-debbiewarhol.ppm
Taxa de compressao: -32.62%
Arquivo convertido com sucesso. Resultados salvos nos arquivos IMAGENS/desconprimi-EricWSchwartz.ppm
Taxa de compressao: 49.03%
Arquivo convertido com sucesso. Resultados salvos nos arquivos IMAGENS/desconprimi-louis.ppm
Taxa de compressao: -17.28%
Arquivo convertido com sucesso. Resultados salvos nos arquivos IMAGENS/desconprimi-magazines.ppm
Taxa de compressao: 92.31%
Arquivo convertido com sucesso. Resultados salvos nos arquivos IMAGENS/desconprimi-maxresdefault.ppm
"""

def escreveDocs():
    """Shows basic usage of the Docs API.
    Prints the title of a sample document.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('assets/token1.json'):
        creds = Credentials.from_authorized_user_file('assets/token1.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('assets/token1.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('docs', 'v1', credentials=creds)
        # Retrieve the documents contents from the Docs service.
        document = service.documents().get(documentId=DOCUMENT_ID).execute()

        data = {
            "textConclusion" : conclusao,
            "textMain" : desenvolvimento,
            "output" : output,
            "textIntroduction" : introducao
        }
        cria_template_doc(service,DOCUMENT_ID, data)
        
        
        print("feito !")
    except HttpError as err:
        print(err)


if __name__ == '__main__':      
    escreveDocs()