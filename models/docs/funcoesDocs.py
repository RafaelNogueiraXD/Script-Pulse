from __future__ import print_function
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload

def cria_template_doc(service, document_id, data):
    
    escreve_paragrafo_docs(service, document_id, data['textConclusion'],acha_index(service,document_id))
    cria_titulo(service, document_id, "Conclusão",acha_index(service,document_id))
    
    escreve_output_docs(service, document_id, data['output'],acha_index(service,document_id))
    cria_subtitulo(service, document_id, "Output do programa",acha_index(service,document_id))
    
    escreve_paragrafo_docs(service, document_id, data['textMain'],acha_index(service,document_id))
    cria_titulo(service, document_id, "Desenvolvimento",acha_index(service,document_id))
    
    escreve_paragrafo_docs(service, document_id, data['textIntroduction'],acha_index(service,document_id))
    cria_titulo(service, document_id, "Introdução",acha_index(service,document_id))
    

def acha_index(service,document_id):
    document = service.documents().get(documentId=document_id).execute()
    index = len(document['body']['content'])
    for element in document['body']['content']:
        if 'paragraph' in element:
            for part in element['paragraph']['elements']:
                if 'textRun' in part:
                    if part['textRun']['content'] == "\n":
                        index = 1
    return index
# Função genérica para criar requisições de texto
def create_text_request(service, document_id, text, index, text_style, paragraph_style):
    requests = [
        {
            'insertText': {
                'location': {'index': index},
                'text': text
            }
        },
        {
            'updateTextStyle': {
                'range': {'startIndex': index, 'endIndex': index + len(text)},
                'textStyle': text_style,
                'fields': ','.join(text_style.keys())
            }
        },
        {
            'updateParagraphStyle': {
                'range': {'startIndex': index, 'endIndex': index + len(text)},
                'paragraphStyle': paragraph_style,
                'fields': ','.join(paragraph_style.keys())
            }
        }
    ]
    return service.documents().batchUpdate(documentId=document_id, body={'requests': requests}).execute()
#  'paragraphStyle': {'backgroundColor': {'color': {'rgbColor': {'red': 0.0,'green': 0.0,'blue': 0.0}}}}
#  'foregroundColor': {'backgroundColor': {'color': {'rgbColor': {'red': 1.0,'green': 1.0,'blue': 1.0}}}}
# Funções específicas usando a função genérica
def escreve_paragrafo_docs(service, document_id, text, index):
    text_style = {'fontSize': {'magnitude': 24, 'unit': 'PT'}, 'bold': False}
    paragraph_style = {'namedStyleType': 'NORMAL_TEXT', 'direction': 'LEFT_TO_RIGHT', 'alignment': 'JUSTIFIED'}
    return create_text_request(service, document_id, text, index, text_style, paragraph_style)

def escreve_output_docs(service, document_id, text, index):
    text_style = {
        'fontSize': {'magnitude': 40, 'unit': 'PT'},'bold': False,
        'foregroundColor': {'color': {'rgbColor': {'red': 1.0, 'green': 1.0, 'blue': 1.0}}},
        'backgroundColor': {'color': {'rgbColor': {'red': 0.0, 'green': 0.0, 'blue': 0.0}}}
    }
    paragraph_style = {
        'namedStyleType': 'NORMAL_TEXT','direction': 'LEFT_TO_RIGHT','alignment': 'JUSTIFIED'
    }
    return create_text_request(service, document_id, text, index, text_style, paragraph_style)


def cria_titulo(service, document_id, text, index):
    text_style = {'bold': True}
    paragraph_style = {'namedStyleType': 'TITLE', 'direction': 'LEFT_TO_RIGHT', 'alignment': 'CENTER'}
    return create_text_request(service, document_id, text, index, text_style, paragraph_style)

def cria_subtitulo(service, document_id, text, index):
    text_style = {'bold': False}
    paragraph_style = {'namedStyleType': 'SUBTITLE', 'direction': 'LEFT_TO_RIGHT', 'alignment': 'START'}
    return create_text_request(service, document_id, text, index, text_style, paragraph_style)
